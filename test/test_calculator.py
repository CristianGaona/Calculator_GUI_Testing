# Testing with pytest

from src.operaciones import Calculator
import pytest

@pytest.fixture(name="obj1")
def obj1_fixture():
    return Calculator()

def test_addResult(obj1):
    assert obj1.addResult(2, 5) == 7

def test_subtractResult(obj1):
    assert obj1.subtractResutl(2,-5) == 7

def test_divideResult(obj1):
    assert obj1.divideResult(10,5) == 2
    with pytest.raises(ValueError):
        obj1.divideResult(20, 0)

def test_multiplicationResult(obj1):
    assert obj1.multiplicationResult(2,8)==16
