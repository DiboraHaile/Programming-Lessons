import sys
import os
sys.path.append(os.path.abspath("../../"))
import main
from scenario_two import main as main_two

print(sys.path)
if __name__ == "__main__":
    main_two.this_is_mains_main()