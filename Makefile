.PHONY: help install dev-install test-install lint format typecheck test test-unit test-integration clean run run-server

# デフォルトターゲット - ヘルプを表示
help:
	@echo "利用可能なコマンド:"
	@echo "  make install        - 本番用依存関係をインストール"
	@echo "  make dev-install    - 開発用依存関係をインストール"
	@echo "  make test-install   - テスト用依存関係をインストール"
	@echo "  make lint           - ruffでコード品質チェック"
	@echo "  make format         - ruffでコードフォーマット"
	@echo "  make typecheck      - mypyで型チェック"
	@echo "  make check          - lint + typecheck を実行"
	@echo "  make fix            - format + lint --fix を実行"
	@echo "  make test           - 全テストを実行"
	@echo "  make test-unit      - 単体テスト(pytest)を実行"
	@echo "  make test-integration - 統合テスト(MCP)を実行"
	@echo "  make clean          - キャッシュファイルを削除"
	@echo "  make run            - hello.pyを実行"
	@echo "  make run-server     - MCPサーバーを起動"

# 依存関係のインストール
install:
	uv sync

# 開発用依存関係のインストール
dev-install:
	uv sync --group dev

# テスト用依存関係のインストール
test-install:
	uv sync --group test

# コード品質チェック
lint:
	uv run ruff check .

# コードフォーマット
format:
	uv run ruff format .

# 型チェック
typecheck:
	uv run mypy .

# 全チェック実行
check: lint typecheck

# フォーマット + 自動修正
fix: format
	uv run ruff check . --fix

# 全テスト実行
test: test-unit test-integration

# 単体テスト実行
test-unit:
	uv run pytest tests/test_math_functions.py -v

# 統合テスト実行（MCP）
test-integration:
	uv run python tests/test_mcp_server.py

# キャッシュファイル削除
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".mypy_cache" -delete
	find . -type d -name ".ruff_cache" -delete

# MCPサーバー起動
run-server:
	uv run python -m src.main
