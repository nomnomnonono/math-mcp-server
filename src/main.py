"""
数学計算を行うMCPサーバー
"""

import math

import fastmcp

from . import math_functions

# MCPサーバーアプリケーションを作成
app = fastmcp.FastMCP("Math Evaluation Server")


@app.tool()
def add(a: float, b: float) -> float:
    """2つの数値を足し算します。

    Args:
        a: 最初の数値
        b: 2番目の数値

    Returns:
        a + b の結果
    """
    return math_functions.add(a, b)


@app.tool()
def subtract(a: float, b: float) -> float:
    """2つの数値を引き算します。

    Args:
        a: 被減数
        b: 減数

    Returns:
        a - b の結果
    """
    return math_functions.subtract(a, b)


@app.tool()
def multiply(a: float, b: float) -> float:
    """2つの数値を掛け算します。

    Args:
        a: 最初の数値
        b: 2番目の数値

    Returns:
        a * b の結果
    """
    return math_functions.multiply(a, b)


@app.tool()
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
    return math_functions.divide(a, b)


@app.tool()
def power(base: float, exponent: float) -> float:
    """べき乗を計算します。

    Args:
        base: 底
        exponent: 指数

    Returns:
        base^exponent の結果
    """
    return math_functions.power(base, exponent)


@app.tool()
def sqrt(x: float) -> float:
    """平方根を計算します。

    Args:
        x: 平方根を求める数値

    Returns:
        √x の結果

    Raises:
        ValueError: xが負の数の場合
    """
    return math_functions.sqrt(x)


@app.tool()
def sin(x: float) -> float:
    """正弦（サイン）を計算します。

    Args:
        x: 角度（ラジアン）

    Returns:
        sin(x) の結果
    """
    return math_functions.sin(x)


@app.tool()
def cos(x: float) -> float:
    """余弦（コサイン）を計算します。

    Args:
        x: 角度（ラジアン）

    Returns:
        cos(x) の結果
    """
    return math_functions.cos(x)


@app.tool()
def tan(x: float) -> float:
    """正接（タンジェント）を計算します。

    Args:
        x: 角度（ラジアン）

    Returns:
        tan(x) の結果
    """
    return math_functions.tan(x)


@app.tool()
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
    return math_functions.log(x, base)


@app.tool()
def factorial(n: int) -> int:
    """階乗を計算します。

    Args:
        n: 階乗を求める非負整数

    Returns:
        n! の結果

    Raises:
        ValueError: nが負の整数の場合
    """
    return math_functions.factorial(n)


@app.tool()
def evaluate_expression(expression: str) -> float:
    """数学式を評価します（安全な式のみ）。

    Args:
        expression: 評価する数学式（例: "2 + 3 * 4"）

    Returns:
        式の計算結果

    Raises:
        ValueError: 無効な式の場合
    """
    return math_functions.evaluate_expression(expression)


if __name__ == "__main__":
    app.run()
