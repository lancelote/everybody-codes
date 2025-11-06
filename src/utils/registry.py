import re
from collections.abc import Callable

type Solution = Callable[[str], str]

SOLUTIONS: dict[str, Solution] = {}


def register_solution(name: str) -> Callable[[Solution], Solution]:
    # e.g., `2025-1a`
    assert not is_valid_solution_name(name), f"invalid solution name={name}"

    def decorator(func: Solution) -> Solution:
        assert name not in SOLUTIONS

        SOLUTIONS[name] = func
        return func

    return decorator


def is_valid_solution_name(name: str) -> bool:
    return re.match(r"\d{4}-\d{1,2}[abc]", name) is None
