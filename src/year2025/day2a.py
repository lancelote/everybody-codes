import math
import re
from dataclasses import dataclass

from src.utils.registry import register_solution


@dataclass
class Complex:
    x: int
    y: int

    def __add__(self, other: object) -> Complex:
        if not isinstance(other, Complex):
            raise NotImplementedError

        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other: object) -> Complex:
        if not isinstance(other, Complex):
            raise NotImplementedError

        return Complex(
            self.x * other.x - self.y * other.y,
            self.x * other.y + self.y * other.x,
        )

    def __truediv__(self, other: object) -> Complex:
        if not isinstance(other, Complex):
            raise NotImplementedError

        return Complex(
            math.trunc(self.x / other.x),
            math.trunc(self.y / other.y),
        )

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Complex)
            and self.x == other.x
            and self.y == other.y
        )

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    @classmethod
    def from_str(cls, line: str) -> Complex:
        first, second = re.findall(r"-?\d+", line)
        return Complex(int(first), int(second))


@register_solution(name="2025-2a")
def solve(task: str) -> str:
    result = Complex(0, 0)
    a = Complex.from_str(task)

    for _ in range(3):
        result *= result
        result /= Complex(10, 10)
        result += a

    return f"[{result.x},{result.y}]"
