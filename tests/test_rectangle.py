import pytest
from src.rectangle import Rectangle

@pytest.fixture()
def before_testcase():
        rect=Rectangle()
        rect.set_length(20)
        rect.set_width(3)
        return rect

class TestRectanlge:
    def test_area(self,before_testcase):
        assert before_testcase.area() == 60
    
    #@pytest.mark.xfail(reason="IF we run, a pronblem will be raised")
    def test_premieter(self,before_testcase):
        assert before_testcase.permieter() == 46
            