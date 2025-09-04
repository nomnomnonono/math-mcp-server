"""
数学計算関数モジュール
"""

import math


def add(a: float, b: float) -> float:
    """2つの数値を足し算します。

    Args:
        a: 最初の数値
        b: 2番目の数値

    Returns:
        a + b の結果
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """2つの数値を引き算します。

    Args:
        a: 被減数
        b: 減数

    Returns:
        a - b の結果
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """2つの数値を掛け算します。

    Args:
        a: 最初の数値
        b: 2番目の数値

    Returns:
        a * b の結果
    """
    return a * b


def divide(a: float, b: float) -> float:
    """2つの数値を割り算します。

    Args:
        a: 被除数
        b: 除数

    Returns:
        a / b の結果

    Raises:
        ValueError: bが0の場合
    """
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b


def power(base: float, exponent: float) -> float:
    """べき乗を計算します。

    Args:
        base: 底
        exponent: 指数

    Returns:
        base^exponent の結果
    """
    return math.pow(base, exponent)


def sqrt(x: float) -> float:
    """平方根を計算します。

    Args:
        x: 平方根を求める数値

    Returns:
        √x の結果

    Raises:
        ValueError: xが負の数の場合
    """
    if x < 0:
        raise ValueError("負の数の平方根は計算できません")
    return math.sqrt(x)


def sin(x: float) -> float:
    """正弦（サイン）を計算します。

    Args:
        x: 角度（ラジアン）

    Returns:
        sin(x) の結果
    """
    return math.sin(x)


def cos(x: float) -> float:
    """余弦（コサイン）を計算します。

    Args:
        x: 角度（ラジアン）

    Returns:
        cos(x) の結果
    """
    return math.cos(x)


def tan(x: float) -> float:
    """正接（タンジェント）を計算します。

    Args:
        x: 角度（ラジアン）

    Returns:
        tan(x) の結果
    """
    return math.tan(x)


def log(x: float, base: float = math.e) -> float:
    """対数を計算します。

    Args:
        x: 真数
        base: 底（デフォルトは自然対数）

    Returns:
        log_base(x) の結果

    Raises:
        ValueError: xまたはbaseが無効な値の場合
    """
    if x <= 0:
        raise ValueError("真数は正の数である必要があります")
    if base <= 0 or base == 1:
        raise ValueError("底は正の数で1以外である必要があります")

    return math.log(x) / math.log(base)


def factorial(n: int) -> int:
    """階乗を計算します。

    Args:
        n: 階乗を求める非負整数

    Returns:
        n! の結果

    Raises:
        ValueError: nが負の整数の場合
    """
    if n < 0:
        raise ValueError("階乗は非負整数に対してのみ定義されます")
    return math.factorial(n)


def evaluate_expression(expression: str) -> float:
    """数学式を評価します（安全な式のみ）。

    Args:
        expression: 評価する数学式（例: "2 + 3 * 4"）

    Returns:
        式の計算結果

    Raises:
        ValueError: 無効な式の場合
    """
    # 安全な文字のみを許可
    allowed_chars = set("0123456789+-*/.() ")
    if not all(c in allowed_chars for c in expression):
        raise ValueError("無効な文字が含まれています")

    try:
        result = eval(expression)
        if isinstance(result, int | float):
            return float(result)
        else:
            raise ValueError("結果が数値ではありません")
    except Exception as e:
        raise ValueError(f"式の評価エラー: {str(e)}") from e
