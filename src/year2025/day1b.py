from src.utils.registry import register_solution
from src.year2025.day1a import Direction
from src.year2025.day1a import process_data


@register_solution(name="2025-1b")
def solve(task: str) -> str:
    names, instructions = process_data(task)

    i = 0

    for instruction in instructions:
        shift = +1

        if instruction.direction is Direction.LEFT:
            shift = -1

        i = (i + shift * instruction.steps) % len(names)

    return names[i]
