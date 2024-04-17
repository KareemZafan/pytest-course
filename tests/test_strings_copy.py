from src import strings as st
import pytest

@pytest.mark.order(1)
def test_capitalize():
    assert st.capitalize("kareem") == "Kareem"

@pytest.mark.order(3)
def test_end_With():
    assert st.end_with("kareem","eem") 
    assert st.end_with("Hello my team, nice to meet you today.","today.") 


a = 20 
payment= 100
#@pytest.mark.skipif(a<=15, reason="It should work only after day 15")
@pytest.mark.order(2)
def test_payment():
    assert payment == 89