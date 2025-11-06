from dataclasses import dataclass
from enum import StrEnum
from typing import Self

from src.utils.registry import register_solution

type Name = str


class Direction(StrEnum):
    LEFT = "L"
    RIGHT = "R"


@dataclass
class Instruction:
    direction: Direction
    steps: int

    @classmethod
    def from_str(cls, text: str) -> Self:
        first, rest = text[0], text[1:]
        return cls(Direction(first), int(rest))


def process_data(data: str) -> tuple[list[Name], list[Instruction]]:
    first, last = data.split("\n\n")

    names = first.split(",")
    instructions = [Instruction.from_str(x) for x in last.split(",")]

    return names, instructions


@register_solution(name="2025-1a")
def solve(task: str) -> str:
    names, instructions = process_data(task)

    i = 0

    for instruction in instructions:
        shift = +1

        if instruction.direction is Direction.LEFT:
            shift = -1

        i = max(i + shift * instruction.steps, 0)

        if i >= len(names):
            i = len(names) - 1

    return names[i]
