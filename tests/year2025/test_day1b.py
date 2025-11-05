from src.year2025.day1b import solve


def test_solve():
    data = "Vyrdax,Drakzyph,Fyrryn,Elarzris\n\nR3,L2,R3,L1"
    assert solve(data) == "Elarzris"
