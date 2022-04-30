import sys, time, os
from script_two import dummy_function_two

def dummy_function():
    print("This is dummy function one")
    dummy_function_two()


class DummyClass:
    def __init__(self):
        print("This is dummy class")
    