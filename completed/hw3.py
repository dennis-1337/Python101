''' 
hw3.py
Course: ECE 2210 - Python Programming for ECE
Semester: Fall 2025 
Name: You Know Who (Replace it with your name)
CUID: (Insert your CUID here)
Known Bugs: If your code contains any mistakes, please list them here.
'''

# You CANNOT import other modules
import math
import sys

redirectIOtoFile = True

if(redirectIOtoFile):
    # redirect stdin to a file
    sys.stdin = open('input', 'r')

############ Your input starts here. Do NOT change the above code!!! #################

spacing = "  "
# Problem 1.(a)
# Complete the function below following the requirements given in hw3.pdf.
def rhombus():
    """ Draw a rhombus of h=5.
    """
    draw_rhombus(5,"*") 
    pass # Replace pass with your code


# Problem 1.(b)
# Complete the function below following the requirements given in hw3.pdf
def draw_rhombus(h, s):
    """ Draw a rhombus of height h using symbol s.
    """
    size = h
    s = s+" "
    leg = int((size-1)/2)
    for i in range(leg,0,-1):
        print((i*spacing) + (s*(2*(leg-i)+1)))
    print((s*size))
    for i in range(1,leg+1,1):
        print((i*spacing) + (s*(2*(leg-i)+1)))
    pass # Replace pass with your code


# Problem 2.(a)
# Complete the function below following the requirements given in hw3.pdf
def is_triangle(a, b, c):
    """ Check if three lengths can form a triangle.
    """
    if c>(a+b) or b>(a+c) or a>(b+c):
        print("No")
        return
    print("Yes")
    pass # Replace pass with your code


# Problem 2.(b)
# Complete the function below following the requirements
# given in hw3.pdf
def interative_is_triangle():
    """ Check if user-entered three lengths can form a triangle.
    """
    a = int(input("Enter l1> "))
    print(a)
    b = int(input("Enter l2> "))
    print(b)
    c = int(input("Enter l3> "))
    print(c)
    is_triangle(a,b,c)
    pass # Replace pass with your code


# Problem 3
# Complete the function below following the requirements given in hw3.pdf
def guess_number(k):
    """ Guess number k in [1, 9999].
    """
    guess = -1
    while guess != k:
        guess = int(input("Enter number> "))
        if guess < 1 or guess > 9999:
           print("Invalid input!")
           pass
        elif k == guess:
            print("Well guessed!")
        else:
           print(guess)
            
    pass # Replace pass with your code


# Problem 4
# Complete the function below following the requirements given in hw3.pdf
def estimate_pi():
    constant = (2*(2**0.5))/9801
    k=0
    term = (math.factorial(4*k)*(1103+26390*k))/((math.factorial(k)**4)*(396**(4*k)))
    newTerm = 1
    while(newTerm > 10**(-15)):
        k=k+1
        newTerm = (math.factorial(4*k)*(1103+26390*k))/((math.factorial(k)**4)*(396**(4*k)))
        term = term + newTerm
    pi = (term * constant)**-1
    return(pi)
    pass # Replace pass with your code


# Problem 5.a)
# Complete the function below following the requirements given in hw3.pdf
def check_digit(n):
    while(n > 0):
        div = divmod(n,10)
        n = div[0]
        if div[1]%2==1:
            return False
    return True
    pass # Replace pass with your code


# Problem 5.b)
# Complete the function below following the requirements given in hw3.pdf
def find_odd_digit_numbers(a, b):
    r = range(a, b+1)
    for i in r:
        if check_digit(i):
            print(i)
    pass # Replace pass with your code


################# Your input ends here. Do NOT change the following code!!! ######################
if __name__ == '__main__':
    print("P1.(a): The following is the output of rhombus():")
    rhombus()

    print()
    print()
    print("P1.(b): The following is the output of draw_rhombus():")
    draw_rhombus(7, '%')
    draw_rhombus(9, '$')

    print()
    print()
    print("P2.(a): The following is the output of is_triangle():")
    is_triangle(1, 4, 6)
    is_triangle(6, 16, 20)
    is_triangle(6, 6, 6)

    print()
    print()
    print("P2.(b): The following is the output of interactive_is_triangle():")
    interative_is_triangle()
    interative_is_triangle()
    interative_is_triangle()

    print()
    print()
    print("P3: The following is the output of guess_number():")
    guess_number(56)
    guess_number(3467)
    guess_number(1)

    print()
    print()
    print("P4: The return value of estimate_pi() is", estimate_pi())
    
    print()
    print()
    print("P5.(a): The following is the output of guess_number():")
    print(check_digit(447))
    print(check_digit(28282))
    print(check_digit(6003))
    
    print()
    print()
    print("P5.(b): The following is the output of find_odd_digit_numbers(a, b)")
    find_odd_digit_numbers(12, 48304)

