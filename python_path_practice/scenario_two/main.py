import os, sys
sys.path.append(os.path.abspath('../../scenario_three'))
from package_one.script_one import dummy_function

def this_is_mains_main():
    print("mooohahaha")
    
if __name__ == "__main__":
    print("You are in scenario two")
    print(sys.path)
    dummy_function()