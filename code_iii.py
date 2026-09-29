# =============================================================================
# IMPORTS
# =============================================================================
import pprint as p
import math
import copy
# =============================================================================
# FUNCTIONS
# =============================================================================




# =============================================================================
# DEBUGGING
# =============================================================================

# =============================================================================
# PROCESS
# =============================================================================
def process(input_f, func):
    # SANITISING INPUT
    with open(input_f, "r") as f:
        def get_line():
            return f.readline().strip()
        params = []
        # str input
        if (func == ""):
            pass
        else:
            result = "fail"
        result = func(*params)

    # SANITISING OUTPUT
    with open("output.txt", "w") as o:
        # list output
        if type(result) == list:
            # list of cyclopeptides
            if type(result[0]) == list:
                output = []
                for l in result:
                    output.append("-".join(map(str, l)))
                output = " ".join(output)
            # singular cyclopeptide
            else:
                output = "-".join(map(str, result))
        # str output
        elif type(result) == str:
            output = result
        # int output
        elif type(result) == int:
            output = str(result)
        # dict output
        elif type(result) == dict:
            # dict: list output
            if all(isinstance(v, list) for v in result.values()):
                output = ""
                for i in result:
                    result[i] = " ".join(map(str, result[i]))
                    output += f"{i}: {result[i]}\n"

        o.write(output)
    print("Output written")
    
# === MODIFY THIS BEFORE RUNNING ===
input_f = ""
func = ""
# process(input_f, func)
# ==================================

