#This project inputs a vector, standard, or factored form of a quadratic function
#from the user and provides the remaining two forms of the function.
#This project will also graph the function
import matplotlib.pyplot as plt
#matplotlib library will be used to plot the function
import numpy as np
#numpy library will be used to set an array for a set of numbers
import math
import cmath
#because quadratic functions can have complex roots, cmath is used for the
#project, but math will also be used for positive roots
#while loop makes the user enter a valid input. If the user enters 'q' or 'quit', the program closes
def Trinomial(valid = True):
    print("Welcome to the Trinomial Triangle, please enter 'factored', 'vector', or 'standard' and enter the "
          "constants for the polynomials. This program will output the other 2 forms of the equation and graph the"
          "function. Type 'q' or 'quit' to quit.")
    # User inputs the type of quadratic function the user wants to morph, valid
    # determines if the entry is valid
    quad_type = input("Which quadratic function type do you want to convert?")
    # initializes variables
    a, b, c = "", "", ""
    r, s = "", ""
    h, k = "", ""
    while (valid == True):
        if quad_type.lower() == "vector":
            a, h, k = float(input("Please enter an 'a' value.")), \
                      float(input("Please enter an 'h' value.")), \
                      float(input("Please enter an 'k' value."))
            valid = False
        elif quad_type.lower() == "standard":
            a, b, c = float(input("Please enter an 'a' value.")), \
                  float(input("Please enter an 'b' value.")), \
                  float(input("Please enter an 'c' value."))
            valid = False
        elif quad_type.lower() == "factored":
            a, r, s = float(input("Please enter an 'a' value.")), \
                  float(input("Please enter an 'r' value.")), \
                  float(input("Please enter an 's' value."))
            valid = False
        elif quad_type.lower() == "q" or quad_type.lower() == "quit":
            return 0
        else:
            quad_type = input("invalid entry")
            # calculate constants for the respective function inputs.
    if quad_type.lower() == "vector":
        b = -2 * a * h
        c = a * h ** 2 + k
        #for simplifying the output, only use cmath if -k / a is negative
        if -k / a >= 0:
            r = h + math.sqrt(-k / a)
            s = h - math.sqrt(-k / a)
        else:
            r = h + cmath.sqrt(-k / a)
            s = h - cmath.sqrt(-k / a)
        print("The function is f(x) = " + str(a) + "x**2 + " + str(b) + "x + " + str(
            c) + " in standard form and f(x) = " + str(a) +
              "(x - " + str(r) + ")(x - " + str(s) + ") in factored form")
    elif quad_type.lower() == "standard":
        if b ** 2 >= 4 * a * c:
            r = -b / (2 * a) + math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
            s = -b / (2 * a) - math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
        else:
            r = -b / (2 * a) + cmath.sqrt(b ** 2 - 4 * a * c) / (2 * a)
            s = -b / (2 * a) - cmath.sqrt(b ** 2 - 4 * a * c) / (2 * a)
        h = -b / (2 * a)
        k = c - b ** 2 / (4 * a)
        print("The function is f(x) = " + str(a) + "(x + " + str(h) + ")^2 + " + str(
            k) + " in vector form and f(x) = " + str(a) +
              "(x - " + str(r) + ")(x - " + str(s) + ") in factored form.")
    elif quad_type.lower() == "factored":
        b = -(a * r + a * s)
        c = a * r * s
        h = (r + s) / 2
        k = -a * ((r - s) / 2) ** 2
        print("The function is f(x) = " + str(a) + "x**2 + " + str(b) + "x + " + str(c) +
              " in standard form and f(x) = " + str(a) + "(x + " + str(h) + ")^2 + " + str(
            k) + " in vector form.")
        # plots the graph using the Numpy library and the standard form of the quadratic

    #x values range from h - 10 to h + 10 with 0.05 increments totaling 400 points
    x = np.arange(h - 10, h + 10, 0.05)
    #uses standard form to plot y values
    y = a * x ** 2 + b * x + c
    plt.plot(x, y)
    plt.title("f(x) = " + str(a) + "x**2 + " + str(b) + "x + " + str(c))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
Trinomial()
