import re
from typing import Callable

type Solution = Callable[[str], str]

SOLUTIONS: dict[str, Solution] = {}


def register_solution(name: str) -> Callable[[Solution], Solution]:
    # e.g., `2025-1a`
    assert valid_solution_name(name), f"invalid solution name={name}"

    def decorator(func: Solution) -> Solution:
        assert name not in SOLUTIONS

        SOLUTIONS[name] = func
        return func
    return decorator


def valid_solution_name(name: str) -> bool:
    if re.match(r"\d{4}-\d{1,2}[abc]", name) is None:
        return False
    return True
