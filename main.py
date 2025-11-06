import sys
from pathlib import Path

from src.utils.registry import SOLUTIONS

EXPECTED_ARGV_LEN = 4
ERR_BAD_ARG = r"want: year[\d+] day[\d+] part[abc]"


def get_task(year: str, day: str, part: str) -> str:
    path = Path() / "notes" / f"year{year}" / f"day{day}{part}.txt"
    with path.open("r") as file:
        return file.read()


def main() -> None:
    assert len(sys.argv) == EXPECTED_ARGV_LEN, ERR_BAD_ARG

    year, day, part = sys.argv[1:]
    key = f"{year}-{day}{part}"
    solve = SOLUTIONS[key]
    task = get_task(year, day, part)
    result = solve(task)

    print(result)


if __name__ == "__main__":
    main()
