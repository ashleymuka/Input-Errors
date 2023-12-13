'''
Author: Ashley Muka
Assignment Title: Input Errors
Assignment Description: output the largest of three input integers
Due Date:09/15/2023
Date created:09/15/2023
Date Last Modified:09/15/2023

'''

#input
try:
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
   
    inputs_read = 3
   
    max_num = max(num1, num2, num3)
    print(max_num)

#process

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

#output
if inputs_read == 0:
    print(f"{inputs_read} input(s) read:")
    print("No max")
    
elif inputs_read == 1:
    print(f"{inputs_read} input(s) read:")
    print(f"Max is {max_num}")
    

