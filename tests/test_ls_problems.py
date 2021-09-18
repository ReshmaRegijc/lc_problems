from src.lc_problems import add1,add2
from src.addbinary import addBinary

def test_add1():
    assert add1(7)==8

def test_add1_fail():
    assert add1(6)==7

def test_add2():
    assert add2(6)==8

def test_add2_fail():
    assert add2(6)==8

def test_addBinary():
    assert addBinary("11","1") == "100"

def test_addBinary1():
    assert addBinary("1010","1011") == "10101"