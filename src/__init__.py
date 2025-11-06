import importlib
from pathlib import Path


def import_all_solution_modules() -> None:
    years = Path(__file__).parent

    for year in years.iterdir():
        if not year.is_dir() or year.stem.startswith("_"):
            continue

        package_name = year.stem

        for file in year.glob("day*.py"):
            module_name = file.stem
            import_path = f".{package_name}.{module_name}"
            importlib.import_module(import_path, package="src")


import_all_solution_modules()
