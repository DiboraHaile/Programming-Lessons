import os, sys
# sys.path.append(os.path.join(os.path.dirname(__file__)))
print(os.path.join(os.path.dirname(__file__)))
print(__file__)
print("Dirname : ",os.path.dirname(os.path.abspath(__file__)))
print("Absolute path: ", os.path.abspath(__file__))
print("Base name: ", os.path.basename(__file__))
