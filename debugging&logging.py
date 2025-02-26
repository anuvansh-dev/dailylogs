"""
Debugging using pdb module
"""

import pdb

def add(a, b):
    pdb.set_trace()
    return a + b

result = add(2, 5)
print(f"result: {result}")


"""
Exercise 1:

- Write a function to calculate area and perimeter of circle.
- Set a breakpoint at the beginning of the area, perimeter function using pdb.
- Run the code and use the debugger to inspect the values of radius, area, and perimeter.
- Step through the code to understand how the variables are calculated.
- After inspecting the variables, continue execution and observe the final output.

Question:
- What are the values of area and perimeter when the program reaches the breakpoint?  
Answer: The area and perimeter are not defined yet at the breakpoint but after stepping through, area=78.5 and perimeter=31.4
- What is the final output?
Answer: 'Area and perimeter of the circle is (78.5, 31.4).'
"""
import pdb

def calculate_circle(radius):
    pdb.set_trace() # breakpoint
    PI = 3.14
    area = round(PI * radius ** 2, 2)
    perimeter = round(2 * PI * radius, 2)
    return area, perimeter

def main():
    radius = 5
    result = calculate_circle(radius)
    print(f"Area and perimeter of the circle is {result}.")
    
main()



"""
Logging 
"""


import logging

logging.basicConfig(level=logging.DEBUG)

def add(a, b):
    logging.debug(f"Adding {a} and {b}")
    return a + b

result = add(2, 5)
logging.info(f"Result: {result}")


"""
Exercise 2:

- Write a function to divide two numbers with a condition to handle zero division.
- Add logging messages at the debug level: 
logging the arguments on each call, for error and for result.
- Run the code and observe the output of logging messages.
- Add more logging messages to track the flow of execution. 
For example, log entry and exit points of the main() function to track func calls.
- Change the log level to logging.WARNING and observe how it affects the result.

Question:
- What is logged when dividing by zero?
Answer: ERROR:root:Division by zero!
- How does changing the log level to WARNING affect the output?
Answer: It filters out all the low security level log like debug and info,
and shows only the critical security level logs like error.
- Add a log entry for successful division.
Answer: Done

"""

import logging

# Set up logging config
logging.basicConfig(level=logging.WARNING)

def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    if b == 0:
        logging.error("Division by zero!")
        return None
    logging.info(f"Successful division: {a} / {b}")
    return a / b

def main():
    logging.info("Entering the main function")
    result1 = divide(10, 2)
    logging.info(f"Result of division: {result1}")
    
    result2 = divide(10, 0)
    logging.info(f"Result of division: {result2}")
    
    logging.info("Exiting the main function")

main()
