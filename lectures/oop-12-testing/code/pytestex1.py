#!/usr/bin/env python3

def test_int_float():
    assert 1 == 1.0

def poink():
    print("foo")
    assert 2 == 3

class TestFoo():
    def test_int_float(self):
        assert 1 == 1.0
    def test_int_str(self):
        pass
        #assert 1 == "1"
