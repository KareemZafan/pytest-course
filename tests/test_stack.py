from src.stack import Stack
import pytest
class TestStack:
    def test_push(self):
        stc= Stack()
        stc.push(1)
        stc.push(2)
        stc.push(44)

        assert stc.peek() == 44
        assert stc.size() == 3
        assert stc.current_stack() == [1,2,44]
        
    def test_pop(self):

        #Arrange 
        stc= Stack()
        stc.push(1)
        stc.push(2)
        stc.push(44)
        stc.push(49)
        
        assert stc.size()==4 
        #Acion
        value = stc.pop()
        

        #Assert
        assert stc.peek() == 44
        assert value == 49
        assert stc.size() == 3
        assert stc.current_stack() == [1,2,44]
    
    def test_peek(self):

        #Arrange 
        stc= Stack()
        stc.push(1)
        stc.push(2)
        stc.push(44)
        stc.push(49)
        stc.push(78)
        
     
        #Acion
        value = stc.peek()
        

        #Assert
        assert value == 78
        
        
        
