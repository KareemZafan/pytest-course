import pytest

# open DB 

@pytest.fixture(autouse=True, scope="module")
def open_db():
    print("\nOpenning our DB...")


def test_deleting_from_db():
    print("\nChecking in DB\n")
    assert 1 > 0 

def test_inserting_into_db():
    print("\nAdding a new row in DB\n")
    assert 1 > 0 


def test_updating_row_db():
    print("\nMaintaing a row in DB\n")
    assert 1 > 0 


# close DB 
@pytest.fixture(autouse=True, scope="module")
def close_db():
    yield
    print("\nClosing our DB...")

@pytest.fixture(autouse=True,scope="module")
def mix_post_pre():
    print("\nBefore .. testcase")
    yield
    print("\nAfter.. testcase")
    
    


