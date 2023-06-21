"""Testcases for the Einstein Problem."""
# Import the function(s) we want to test
from einstein import compute_energy, SPEED_OF_LIGHT

def test_main_output():
    assert compute_energy(1, SPEED_OF_LIGHT) == 90000000000000000
    assert compute_energy(14, SPEED_OF_LIGHT) == 1260000000000000000
    assert compute_energy(50, SPEED_OF_LIGHT) == 4500000000000000000

