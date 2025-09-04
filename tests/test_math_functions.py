"""
数学関数の単体テスト
"""

import math

import pytest

from src.math_functions import (
    add,
    cos,
    divide,
    evaluate_expression,
    factorial,
    log,
    multiply,
    power,
    sin,
    sqrt,
    subtract,
    tan,
)


class TestBasicArithmetic:
    """基本算術演算のテストクラス"""

    def test_add(self) -> None:
        assert add(5, 3) == 8
        assert add(-1, 1) == 0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_subtract(self) -> None:
        assert subtract(10, 4) == 6
        assert subtract(0, 5) == -5
        assert subtract(-1, -1) == 0

    def test_multiply(self) -> None:
        assert multiply(7, 6) == 42
        assert multiply(-3, 4) == -12
        assert multiply(0, 100) == 0

    def test_divide(self) -> None:
        assert divide(15, 3) == 5
        assert divide(10, 4) == 2.5
        assert divide(-6, 2) == -3

    def test_divide_by_zero(self) -> None:
        with pytest.raises(ValueError, match="0で割ることはできません"):
            divide(10, 0)


class TestAdvancedMath:
    """高度な数学関数のテストクラス"""

    def test_power(self) -> None:
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(4, 0.5) == 2

    def test_sqrt(self) -> None:
        assert sqrt(16) == 4
        assert sqrt(0) == 0
        assert sqrt(2) == pytest.approx(1.414, rel=1e-3)

    def test_sqrt_negative(self) -> None:
        with pytest.raises(ValueError, match="負の数の平方根は計算できません"):
            sqrt(-1)

    def test_trigonometric(self) -> None:
        assert sin(0) == pytest.approx(0)
        assert sin(math.pi / 2) == pytest.approx(1)
        assert cos(0) == pytest.approx(1)
        assert cos(math.pi) == pytest.approx(-1)
        assert tan(0) == pytest.approx(0)

    def test_log(self) -> None:
        assert log(math.e) == pytest.approx(1)
        assert log(100, 10) == pytest.approx(2)
        assert log(8, 2) == pytest.approx(3)

    def test_log_invalid_input(self) -> None:
        with pytest.raises(ValueError, match="真数は正の数である必要があります"):
            log(-1)
        with pytest.raises(ValueError, match="底は正の数で1以外である必要があります"):
            log(10, 1)
        with pytest.raises(ValueError, match="底は正の数で1以外である必要があります"):
            log(10, -1)

    def test_factorial(self) -> None:
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(10) == 3628800

    def test_factorial_negative(self) -> None:
        with pytest.raises(ValueError, match="階乗は非負整数に対してのみ定義されます"):
            factorial(-1)


class TestExpressionEvaluation:
    """数式評価のテストクラス"""

    def test_basic_expressions(self) -> None:
        assert evaluate_expression("2 + 3") == 5
        assert evaluate_expression("10 - 4") == 6
        assert evaluate_expression("3 * 7") == 21
        assert evaluate_expression("15 / 3") == 5

    def test_complex_expressions(self) -> None:
        assert evaluate_expression("2 + 3 * 4") == 14
        assert evaluate_expression("(2 + 3) * 4") == 20
        assert evaluate_expression("10 / 2 + 3") == 8
        assert evaluate_expression("2.5 * 4") == 10

    def test_invalid_expressions(self) -> None:
        with pytest.raises(ValueError, match="無効な文字が含まれています"):
            evaluate_expression("import os")
        with pytest.raises(ValueError, match="無効な文字が含まれています"):
            evaluate_expression("2 + a")
        with pytest.raises(ValueError, match="式の評価エラー"):
            evaluate_expression("2 / 0")
