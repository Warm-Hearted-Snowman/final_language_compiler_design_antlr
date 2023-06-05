from code_execute import code_execute
import os
import sys
# Import necessary modules
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
file_name = input("Enter Your file name: \n")
with open(f'{BASE_DIR}/user_code/{file_name}.txt', 'r') as f:
    code = f.read()
print("Your Result:")
code_execute(code)
