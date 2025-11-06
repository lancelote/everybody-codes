from typing import Literal

from src.utils.registry import register_solution
from src.year2025.day1a import Direction
from src.year2025.day1a import Instruction
from src.year2025.day1a import process_data


def get_shift(instruction: Instruction) -> Literal[-1, +1]:
    if instruction.direction is Direction.LEFT:
        return -1
    return +1


@register_solution(name="2025-1c")
def solve(task: str) -> str:
    names, instructions = process_data(task)

    for instruction in instructions:
        shift = get_shift(instruction)
        i = (instruction.steps % len(names)) * shift
        names[0], names[i] = names[i], names[0]

    return names[0]
