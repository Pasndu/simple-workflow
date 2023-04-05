import pytest

import src.hello as h

@pytest.mark.parametrize("test_input1,test_input2,expected",[
    (5,5,10)
])
def test_add(test_input1, test_input2, expected):
    assert h.add(test_input1, test_input2) is expected
