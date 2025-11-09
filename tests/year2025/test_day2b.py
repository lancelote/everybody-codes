import pytest

from src.year2025.day2a import Complex
from src.year2025.day2b import count_engraved
from src.year2025.day2b import is_engraved


@pytest.mark.parametrize(
    "point,result",
    (
        (Complex(35630, -64880), Complex(-2520, -5355)),
        (Complex(35630, -64870), Complex(5021, 6454)),
        (Complex(35640, -64860), Complex(-3291, -684)),
        (Complex(36230, -64270), Complex(-7266, 3234)),
        (Complex(36250, -64270), Complex(162903, -679762)),
    ),
)
def test_engraved(point, result):
    assert is_engraved(point) == (True, -1, result)


@pytest.mark.parametrize(
    "point,result,cycle",
    (
        (Complex(35460, -64910), Complex(1265017, 932533), 27),
        (Complex(35470, -64910), Complex(-1724836, 19302), 28),
        (Complex(35480, -64910), Complex(-575306, 8705296), 30),
        (Complex(35680, -64850), Complex(-7919169, 5303832), 95),
        (Complex(35630, -64830), Complex(-6387697, -1621945), 100),
    ),
)
def test_not_engraved(point, result, cycle):
    assert is_engraved(point) == (False, cycle, result)


def test_count_engraved():
    expected_count = 4076
    assert count_engraved(Complex(35300, -64910)) == expected_count
