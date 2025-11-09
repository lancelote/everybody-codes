from src.utils.registry import register_solution
from src.year2025.day2a import Complex

LIMIT = 100_0000
DIVISOR = Complex(100_000, 100_000)


def is_engraved(point: Complex) -> tuple[bool, int, Complex]:
    r = Complex(0, 0)

    for i in range(1, 101):
        r *= r
        r /= DIVISOR
        r += point

        if r.x > LIMIT or r.x < -LIMIT or r.y > LIMIT or r.y < -LIMIT:
            return False, i, r

    return True, -1, r


def count_engraved(start: Complex) -> int:
    count = 0

    for i in range(101):
        for j in range(101):
            point = start + Complex(10 * i, 10 * j)
            engraved, _, _ = is_engraved(point)

            if engraved:
                count += 1

    return count


@register_solution(name="2025-2b")
def solve(task: str) -> str:
    point = Complex.from_str(task)
    return str(count_engraved(point))
