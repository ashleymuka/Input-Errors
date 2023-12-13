'''
Description: output the largest of three input integers.
Use a try block to perform all the statements. 
Use an except block to catch any EOFErrors caused by missing inputs, 
output the number of inputs read, and output the largest value or "No max" if no inputs are read.

'''

try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
   
    inputs_read = 3
   
    max_num = max(num1, num2, num3)
    print(max_num)

except EOFError:
    inputs_read = 0
    max_num = None

except ValueError:
    try:
        num1 
        inputs_read = 1
        max_num = num1
        
    except NameError:
        inputs_read = 0
        max_num = None

if inputs_read == 0:
    print(f"{inputs_read} input(s) read:")
    print("No max")
    
elif inputs_read == 1:
    print(f"{inputs_read} input(s) read:")
    print(f"Max is {max_num}")
    

