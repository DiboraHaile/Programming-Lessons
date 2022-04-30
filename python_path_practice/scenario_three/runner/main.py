import os, sys
sys.path.append(os.path.abspath('../'))
from package_one.script_one import dummy_function

if __name__ == "__main__":
    print(sys.path)
    dummy_function()