from src.year2025.day1c import solve


def test_solve():
    data = "Vyrdax,Drakzyph,Fyrryn,Elarzris\n\nR3,L2,R3,L3"
    assert solve(data) == "Drakzyph"
