# used when making the final graph
import matplotlib.pyplot as plt

# variable that records the equation that the user has put
userfunction = input("Please enter function y', which will be evaluated = ")

# initial x value in differential equation terms
q0 = float(input("Please enter the initial quantity produced (in units): "))

# initial y value in differential equation terms
c0 = float(input("Please enter the initial cost of production (in dollars): "))

# value up to which euler's method runs
maxq = float(input("Please enter the quantity up to which estimation is required (in units): "))

# stepsize to evaluate function at different values
stepsize = float(input("Please enter the step size (in units): "))


# evaluate user's function using the eval function and return it to the function euler
def f(x, y):
    return eval(userfunction)


# collect the different values of quantity and cost and return it as an array
def euler(q0, c0, stepsize, maxq):
    q = q0
    c = c0
    xnums = [q0]
    ynums = [c0]

    while q < maxq:
        c = c + stepsize * f(q, c)
        ynums.append(c)
        q = q + stepsize
        xnums.append(q)
    return xnums, ynums


# receive the arrays formed in the function euler
(graphvaluesX, graphvaluesY) = euler(q0, c0, stepsize, maxq)


# give user the choice to view all of the output from the euler method
# or just view the final value. If user enters anything different,
# prompt the user again until they type 1 or 2 in the console
def choice():
    print("")
    choiceforsteps = input("Would you like to see all steps (1) or only the approximate solution (2)? ")
    if choiceforsteps == '1':
        print("")
        print("Quantity Cost")
        for row in zip(graphvaluesX, graphvaluesY):
            print(round(row[0], 2), "   ", round(row[1], 2))
        print("")
        print("Therefore, total cost of production at " + str(graphvaluesX[len(graphvaluesX) - 1]) + " units is " + str(
            round(graphvaluesY[len(graphvaluesY) - 1], 2)) + " dollars.")
    elif choiceforsteps == '2':
        print("Therefore, total cost of production at " + str(graphvaluesX[len(graphvaluesX) - 1]) + " units is " + str(
            round(graphvaluesY[len(graphvaluesY) - 1]), 2) + " dollars.")
    else:
        print("User input not understood. Redirecting to previous question.")
        choice()


# run method choice
choice()

# give the user the choice to view the graph made from the euler method,
# or leave the program without viewing the graph. Is user input does not
# meet the prompt standard, user will be prompted again until they enter
# 1 or 2 in the console.
def anotherchoice():
    print("")
    plottask = input("Would you like to see a plot of the data? Yes (1); Exit with (2): ")
    if plottask == '1':
        plt.plot(graphvaluesX, graphvaluesY, color="green", linestyle='dashed', linewidth=3, marker='o',
                 markerfacecolor='blue',
                 markersize=12)
        plt.ylim(0, graphvaluesY[len(graphvaluesY) - 1] + 100)
        plt.xlim(0, graphvaluesX[len(graphvaluesX) - 1] + 50)
        plt.xlabel('Quantity Produced')
        plt.ylabel('Cost of Production')
        plt.title("Cost of Production estimated by Euler's method")
        plt.show()
    elif plottask == '2':
        print("Goodbye!")
        pass
    else:
        print("User input not understood. Redirecting to previous question.")
        anotherchoice()


# run method anotherchoice
anotherchoice()
