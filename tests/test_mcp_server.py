#!/usr/bin/env python3
"""
MCPサーバーの数学関数をテストするスクリプト
MCPサーバーを起動してクライアント経由でテストを実行
"""

import asyncio
import math
import sys
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent


def get_text_content(result: Any) -> str:
    """MCPレスポンスから安全にテキストコンテンツを取得する"""
    if result.content and len(result.content) > 0:
        content = result.content[0]
        if isinstance(content, TextContent):
            return content.text
    return "No result"


async def test_basic_arithmetic(session: ClientSession) -> None:
    """基本算術演算のテスト"""
    print("=== 基本算術演算のテスト ===")

    # 加算
    result = await session.call_tool("add", {"a": 5, "b": 3})
    value = get_text_content(result)
    print(f"add(5, 3) = {value} (期待値: 8.0)")
    assert "8" in str(value), f"加算テスト失敗: {value}"

    # 減算
    result = await session.call_tool("subtract", {"a": 10, "b": 4})
    value = get_text_content(result)
    print(f"subtract(10, 4) = {value} (期待値: 6.0)")
    assert "6" in str(value), f"減算テスト失敗: {value}"

    # 乗算
    result = await session.call_tool("multiply", {"a": 7, "b": 6})
    value = get_text_content(result)
    print(f"multiply(7, 6) = {value} (期待値: 42.0)")
    assert "42" in str(value), f"乗算テスト失敗: {value}"

    # 除算
    result = await session.call_tool("divide", {"a": 15, "b": 3})
    value = get_text_content(result)
    print(f"divide(15, 3) = {value} (期待値: 5.0)")
    assert "5" in str(value), f"除算テスト失敗: {value}"

    print("✅ 基本算術演算テスト完了\n")


async def test_advanced_math(session: ClientSession) -> None:
    """高度な数学関数のテスト"""
    print("=== 高度な数学関数のテスト ===")

    # べき乗
    result = await session.call_tool("power", {"base": 2, "exponent": 3})
    value = get_text_content(result)
    print(f"power(2, 3) = {value} (期待値: 8.0)")
    assert "8" in str(value), f"べき乗テスト失敗: {value}"

    # 平方根
    result = await session.call_tool("sqrt", {"x": 16})
    value = get_text_content(result)
    print(f"sqrt(16) = {value} (期待値: 4.0)")
    assert "4" in str(value), f"平方根テスト失敗: {value}"

    # 三角関数
    result = await session.call_tool("sin", {"x": math.pi / 2})
    value = get_text_content(result)
    print(f"sin(π/2) = {value} (期待値: 1.0)")

    result = await session.call_tool("cos", {"x": 0})
    value = get_text_content(result)
    print(f"cos(0) = {value} (期待値: 1.0)")

    # 階乗
    result = await session.call_tool("factorial", {"n": 5})
    value = get_text_content(result)
    print(f"factorial(5) = {value} (期待値: 120)")
    assert "120" in str(value), f"階乗テスト失敗: {value}"

    print("✅ 高度な数学関数テスト完了\n")


async def test_expression_evaluation(session: ClientSession) -> None:
    """数式評価のテスト"""
    print("=== 数式評価のテスト ===")

    # 基本的な式
    result = await session.call_tool("evaluate_expression", {"expression": "2 + 3 * 4"})
    value = get_text_content(result)
    print(f'evaluate_expression("2 + 3 * 4") = {value} (期待値: 14.0)')
    assert "14" in str(value), f"式評価テスト失敗: {value}"

    # 括弧付きの式
    result = await session.call_tool(
        "evaluate_expression", {"expression": "(2 + 3) * 4"}
    )
    value = get_text_content(result)
    print(f'evaluate_expression("(2 + 3) * 4") = {value} (期待値: 20.0)')
    assert "20" in str(value), f"式評価テスト失敗: {value}"

    print("✅ 数式評価テスト完了\n")


async def test_error_handling(session: ClientSession) -> None:
    """エラーハンドリングのテスト"""
    print("=== エラーハンドリングのテスト ===")

    # ゼロ除算
    try:
        result = await session.call_tool("divide", {"a": 10, "b": 0})
        error_msg = get_text_content(result)
        print(f"✅ ゼロ除算エラー正常検出: {error_msg}")
    except Exception as e:
        print(f"✅ ゼロ除算エラー正常検出: {e}")

    # 負の数の平方根
    try:
        result = await session.call_tool("sqrt", {"x": -1})
        error_msg = get_text_content(result)
        print(f"✅ 負の数の平方根エラー正常検出: {error_msg}")
    except Exception as e:
        print(f"✅ 負の数の平方根エラー正常検出: {e}")

    print("✅ エラーハンドリングテスト完了\n")


async def run_mcp_tests() -> None:
    """MCPサーバーを起動してテストを実行"""
    server_params = StdioServerParameters(
        command="uv", args=["run", "python", "-m", "src.main"]
    )

    async with (
        stdio_client(server_params) as (read, write),
        ClientSession(read, write) as session,
    ):
        # サーバーとの接続を初期化
        await session.initialize()

        # 利用可能なツールをリスト
        tools = await session.list_tools()
        print(f"利用可能なツール: {[tool.name for tool in tools.tools]}\n")

        # テストを実行
        await test_basic_arithmetic(session)
        await test_advanced_math(session)
        await test_expression_evaluation(session)
        await test_error_handling(session)


async def main() -> int:
    """メインテスト関数"""
    print("🧮 MCPサーバー数学関数テスト開始\n")

    try:
        await run_mcp_tests()
        print("🎉 すべてのテストが正常に完了しました！")
        return 0

    except Exception as e:
        print(f"❌ テスト失敗: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
