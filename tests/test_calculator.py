from src import calculator as calc
import pytest

ls = [(1,1,2),(2,-7,-5),(22,9,31), (0,-8,-8),(3,2,5),(2000,4000,6000)]
@pytest.mark.parametrize("a, b ,expected_value",ls)
def test_add(a,b,expected_value):
    assert calc.add(a,b) == expected_value

@pytest.mark.March_Release
def test_sub():
    assert calc.sub(3,9) == -6
    assert calc.sub(-3,-6) == 3
    assert calc.sub(12,-6) == 18

def test_mul():
    assert calc.mul(3,9) == 27
    assert calc.mul(-3,-6) == 18
    assert calc.mul(12,-6) == -72   

@pytest.mark.March_Release
def test_div_negative_scenario():
    with pytest.raises(ZeroDivisionError):
        calc.div(1,0)
    with pytest.raises(ZeroDivisionError):
        calc.div(2,0)

@pytest.mark.parametrize("a,b,exp_val",[(2,2,1),(2,1,2),(-2,-2,1),(1,2,0.5), (3,-2,-1.5), (-90,2,-45)])
def test_div_happy_scenario(a,b,exp_val):
    assert calc.div(a,b) == exp_val


@pytest.mark.skip(reason="Not implemented yet")
def test_square_root():
    assert calc.square_root(625) == 25
    assert calc.square_root(9) == 3
    assert calc.square_root(64) == 8
        
def test_su_string():
    assert "hello".title() == 'Hello'


