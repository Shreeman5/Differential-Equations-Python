HOW TO OPEN THE FILE:

Firstly, python has to be installed in the computer. Assuming that the host computer has python installed, right click on the "project2.py" file and click on "Open with...".
The user will be prompted to select an app to open the file and assuming that the user has python, the user will choose the python icon. A terminal for python opens and this
is where the code will come into play.

HOW TO USE THE CODE:

The first thing the user will see is a prompt to enter a function. A topic which will be expanded more on BUGS & IMPROVEMENTS, the equations that the code can take are only
algebraic functions. Here's how to enter algebraic functions, consisting of only x and y variables since the code only reads x and y functions:
Let's assume the user is entering x^0.5(x power 0.5). In compliance with python, the user has to enter "x**.5" to get x^0.5.  
Let's assume the user is entering x^0.8 * y^3(x power 0.8 times y power 3). In compliance with python, the user has to enter "x**.8 * y**3" to get x^0.8 * y^3.
Let's assume the user is entering (x^2 * y^2) - (x^1.5 * y^2)(x square times y square minus x power 1.5 times y square). In compliance with python, the user has to enter 
"x**2 * y**2 - x**1.5 * y**2" to get (x^2 * y^2) - (x^1.5 * y^2).
Let's assume the user is entering (x^0.7/y^2) - (x^0.5/y^3) (x power 0.7 divided by y square minus x power 0.5 divided by y cube). In compliance with python, the user has 
to enter "x**.7/y**2 - x**.5/y**3" to get (x^0.7/y^2) - (x^0.5/y^3).
These are just a few examples. The user can enter the most extreme x and y algebraic function and the code will read it and evaluate it.
The next 4 questions that the terminal will ask to the user, in differential equation terminology, is x0(initial value of x), y0(initial value of y), h(step size) and xmax(max
value of x). If the user enters anything other than a number, which in most cases is a string, the program will terminate, and the user will need to start again. 
Now, assuming that the user has entered an algebraic functions and 4 numbers, the program will give the user the option to view all of the steps(1) or just the y value at the
final x value(2). If user enters anything else other than a "1" or "2", the code will not understand the command and ask the user the same question until the user enters a
"1" or a "2". Assuming that the user has entered a "1" or "2", the program prompts the user to enter "1" to see a plot of the graph(y-values against x-values). If the user 
enters "2", the program is entered and if the user input is anything other than "1" or "2", the code will not understand the command and asks the user the same question until
the user enters a "1" or "2". After the user views the graph and closes the graph window, the program exits anyway. That is all for the code.

POSITIVES OF THE CODE:

Every algebraic function is handled.
Any number(barring complex numbers) can be entered into the 4 prompts and the code will handle it.
Steps, if the user wants to see it, of the euler method are shown.
A graph of y-values against x-values is shown.


BUGS & IMPROVEMENTS:

There are no bugs in the program because every line of code works like it is supposed to. However, there are many improvements that can be made. The most obvious improvement 
is the code's inability to handle trigonometric, log and exponential functions. Next, the 4 prompts that ask for x0, y0, h and xmax can only accept numbers. If the user enters
a string(some random string like "ads" or "man") in any of those 4 prompts, the program will exit, and the user will have to restart the application again, which is not 
user-friendly. That can be improved as well. In the event that the user enters a string into any of those 4 prompts, the program should be able to ask the user to enter a 
number. Another obvious improvement that a future coder can make on this code is to make the .py file into a mobile app.
