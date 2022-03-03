from sympy import python
from ez_cipher import *


if __name__ == "__main__":
    print("RUNNING TESTS:")
    python(test())

    print("\n\nCHECKING FOR CLOSURE:")
    print(f'm_desired: {run(["jagdeep", "robertcc", "vluo"], 2**24)}')
