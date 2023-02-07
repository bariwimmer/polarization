from py_pol.jones_vector import Jones_vector, create_Jones_vectors
from py_pol.jones_matrix import Jones_matrix, create_Jones_matrices
from py_pol.stokes import Stokes, create_Stokes, degrees
from py_pol.utils import degrees
import numpy as np

# ask user to choose an initial axis of polarization
# sequential choices
# does user want to add another element?
# start again

##TEST AREA
user_input = [[]]
temp_list = []
elements =[]

# Jones Vector Definitions
x = Jones_vector('Horizontal')
x.from_matrix(np.array([[1], [0]]))
y = Jones_vector('Vertical')
y.from_matrix(np.array(np.array([[0], [1]])))
d = Jones_vector('Diagonal')
d.from_matrix(np.array(np.array([[1 / np.sqrt(2)], [1 / np.sqrt(2)]])))
a = Jones_vector('Anti-diagonal')
a.from_matrix(np.array(np.array([[1 / np.sqrt(2)], [-1 / np.sqrt(2)]])))
l = Jones_vector('Left-hand circular')
l.from_matrix(np.array(np.array([[1 / np.sqrt(2)], [0 + 1j / np.sqrt(2)]])))
r = Jones_vector('Right-hand circular')
r.from_matrix(np.array(np.array([[1 / np.sqrt(2)], [0 - 1j / np.sqrt(2)]])))

# Polarizer Definitions
xPol = Jones_matrix("Horizontal Polarizer")
xPol.from_matrix(np.array([[1, 0], [0, 0]]))
yPol = Jones_matrix("Vertical Polarizer")
yPol.from_matrix(np.array([[0, 0], [0, 1]]))
dPol = Jones_matrix("Diagonal Polarizer")
dPol.from_matrix(np.array([[0.5, 0.5], [0.5, 0.5]]))
aPol = Jones_matrix("Anti-diagonal Polarizer")
aPol.from_matrix(np.array([[0.5, -0.5], [-0.5, 0.5]]))
rPol = Jones_matrix("Right-circular Polarizer")
rPol.from_matrix(np.array([[1 / np.sqrt(2), 0 + 1j / np.sqrt(2)], [0 - 1j / np.sqrt(2), 1 / np.sqrt(2)]]))
lPol = Jones_matrix("Left-circular Polarizer")
lPol.from_matrix(np.array([[1 / np.sqrt(2), 0 - 1j / np.sqrt(2)], [0 + 1j / np.sqrt(2), 1 / np.sqrt(2)]]))
#
#
# user_input = [[]]
# temp_list = []


def vector(a):
    print(a)
    while a != 'x' or a != 'y' or a != 'd' or a != 'a' or a != 'lc' or a != 'rc':
        vectorChoice = Jones_vector('Initial')
        print('in vector function')
        if a == 'x':
            print('line 51')
            vectorChoice = x #why did I make this line different than all of the rest?
            print(vectorChoice)
            return vectorChoice
        elif a == 'y':
            vectorChoice = y
            return vectorChoice
        elif a == 'd':
            vectorChoice = d
            return vectorChoice
        elif a == 'ad':
            vectorChoice = a
            return vectorChoice
        elif a == 'lc':
            vectorChoice = l
            return vectorChoice
        elif a == 'rc':
            vectorChoice = r
            return vectorChoice
        quit()

def VecChoice():
    print('Choose an initial axis of polarization by entering an abbreviation.')
    print(
        ' \n x: horizontal \n y: vertical \n d: diagonal \n a: anti-diagonal \n l: left-hand circular \n r: right-hand circular')
    a = input()
    if a == 'x' or a == 'y' or a == 'd' or a == 'a' or a == 'l' or a == 'r':
        # b = vector(a)
        user_input[0].append(a)
    else:
        print('Your input was invalid. Try again.')
        return 0
    print(user_input[0])

def ElementChoice(num):
    x = 'y'
    while (x == 'y'):
        print('Enter p to choose polarizer or w to choose wave plate:')
        choice = input()
        if choice == 'p':
            temp_list.append(choice)
            polarizer()
        elif choice == 'w':
            temp_list.append(choice)
            wavePlate()
        else:
            print('Your input was invalid. Try again.')
            return 0
        print(temp_list)
        print(user_input)
        user_input.insert(num, temp_list.copy())
        print(user_input)
        print("Do you want to add another element? \n")
        print("y: yes \n n:no")
        x = input()
        if x == 'y':
            print("Your current list is: \n", user_input)
            print("Enter the number of the element before the position of the element you want to add:")
            num = int(input())
            #num = num + 1
        temp_list.clear()

def ElementChange(num):
    x = 'y'
    while (x == 'y'):
        print('Enter p to choose polarizer or w to choose wave plate:')
        choice = input()
        if choice == 'p':
            temp_list.append(choice)
            polarizer()
        elif choice == 'w':
            temp_list.append(choice)
            wavePlate()
        else:
            print('Your input was invalid. Try again.')
            return 0
        user_input.pop(num)
        user_input.insert(num, temp_list.copy())
        print("Do you want to add another element? \n")
        print("y: yes \n n:no")
        x = input()
        if x == 'y':
            print("Your current list is: \n", user_input)
            print("Enter the number of the element before the position of the element you want to add:")
            num = int(input())
        temp_list.clear()

def UserChoice():
    VecChoice()
    x = 'y'
    while (x == 'y'):
        print('Enter p to choose polarizer or w to choose wave plate:')
        choice = input()
        if choice == 'p':
            temp_list.append(choice)
            polarizer()
        elif choice == 'w':
            temp_list.append(choice)
            wavePlate()
        else:
            print('Your input was invalid. Try again.')
            return 0
        print(temp_list)
        print(user_input)
        user_input.append(temp_list.copy())
        print(user_input)
        print("Do you want to add another element? \n")
        print("y: yes \n n:no")
        x = input()
        temp_list.clear()
    return parseInput()

def Edit():
    print("Do you want to edit the initial light? y/n")
    light = input()
    if light == 'y':
        print('Choose a new initial axis of polarization by entering an abbreviation.')
        print(' \n x: horizontal \n y: vertical \n d: diagonal \n a: anti-diagonal \n l: left-hand circular \n r: right-hand circular')
        a = input()
        if a == 'x' or a == 'y' or a == 'd' or a == 'a' or a == 'l' or a == 'r':
            user_input[0] = a
        else:
            print('Your input was invalid. Try again.')
            return 0

    #make this a loop so they can change multiple if they wish
    print("Do you want to edit an optical element? y/n")
    op = input()
    if op == 'y':
        print("Choices: \n r: remove element \n a: add element \n c: change existing element")
        choice = input()
        if choice == 'r':
            print(user_input)
            print("Enter the number of the element you wish to remove:")
            num = int(input())
            user_input.pop(num)
            print("The new list after removing the element is:")
            print(user_input)
        elif choice == 'a':
            print("Your current list is: \n", user_input)
            print("Enter the number of the element before the position of the element you want to add:")
            num = int(input())
            ElementChoice(num) #adds one or more elements to correct position in list
        elif choice == 'c':
            print("Your current list is: \n", user_input)
            print("Enter the number of the element you want to edit:")
            num = int(input())
            num = num - 1
            ElementChange(num)
            #change element

        #after all changes are made call parseInput with new list (maybe call in menu function, don't know yet which is better)


def polarizer():
    print('Choose an orientation for the polarizer.')
    print(' \n x: linear polarizer with horizontal axis \n y: linear polarizer with vertical axis \n d: diagonal \n a: anti-diagonal \n o: other/arbitrary')
    choice = input()
    if choice == 'x' or choice == 'y' or choice == 'd' or choice == 'a' or choice == 'o':
        temp_list.append(choice)
        if choice == 'o':
            print('Enter the angle:')
            angle = float(input())
            temp_list.append(angle)
        # else:
        #     temp_list.append(choice)
    else:
        print('Your input was invalid. Try again.')
        quit()


def wavePlate():
    print('Choose a phase retardance:')
    print(' \n q: quarter-wave plate \n h: half-wave plate \n a: arbitrary angle')
    retardance = input()
    if retardance == 'q' or retardance == 'h' or retardance == 'a':
        temp_list.append(retardance)
    else:
        print('Your input was invalid. Try again')
        quit()
    print('Enter the angle of the axis of transmission from the horizontal:')
    print(" x: horizontal \n y: vertical \n d: diagonal \n a: anti-diagonal  \n o: other/arbitrary")
    choice = input()
    if choice == 'x':
        angle = 0
    elif choice == 'y':
        angle = 90
    elif choice == 'd':
        angle = 45
    elif choice == 'a':
        angle = -45
    elif choice == 'o':
        print("Please enter the angle: \n")
        angle = float(input())
    temp_list.append(angle)


def parseInput():
    jones = vector(user_input[0][0])
    elements.append(jones)
    size = len(user_input)
    index = size -1
    for index in range(1, size):
        type = user_input[index][0] ##polarizer or wave plate
        if type == 'p':
            choice = user_input[index][1]
            print('line 157')
            if choice == 'x':
                elements.append(xPol)
            elif choice == 'y':
                elements.append(yPol)
            elif choice == 'd':
                elements.append(dPol)
            elif choice == 'a':
                elements.append(aPol)
            elif choice == 'o':
                angle = user_input[index][2][2] * (np.pi / 180)
                m = arbitraryPolarizer(angle)
                elements.append(m)
        elif type == 'w':
            angle = int(user_input[index][2]) * (np.pi / 180)
            retardance = user_input[index][1]
            if retardance == 'q':
                retardance = np.pi / 2  ##converts to radians
                m = arbitraryWavePlate(angle, retardance)
                elements.append(m)
            elif retardance == 'h':
                retardance = np.pi  ##converts to radians
                m = arbitraryWavePlate(angle, retardance)
                elements.append(m)
            elif retardance == 'a':
                m = arbitraryWavePlate(angle, retardance)
                elements.append(m)

    return calculateNew()


def calculateNew():
    #print("inside calculateNew function")
    #print(elements)
    i = len(elements)-1
    m1 = elements[i]
    while i>0:
        print("m1 is ", m1)
        m2= elements[i-1]
        print("m2 is ", m2)
        solution = m1 * m2
        m1 = solution
        i= i - 1
    return solution
    #print(solution)
    #Graph(solution)

# def Graph(sol):
#     S= create_Stokes("Solution Stokes")
#     S.from_Jones(sol)
#     print("The Stokes vector is: ", S)
#     S.draw_poincare()
#     #angles = np.linspace(0, 180 * degrees, 5)
#     #S.linear_light(amplitude=1, azimuth=angles)
#     sol.draw_ellipse(draw_arrow=True, figsize=(9,5))

def Graph(sol, choice):
    S = create_Stokes("Solution Stokes")
    S.from_Jones(sol)
    if choice=='d':
        print("Would you like to save the images? y/n")
        save = input()
        print(S)
        if save == 'y':
            print("What would you like to name the file for the Poincare sphere?")
            sname = input()
            sfname = sname + '.jpg'
            S.draw_poincare(filename=sfname)
            print("What would you like to name the file for the ellipse?")
            name = input()
            fname = name + '.jpg'
            sol.draw_ellipse(filename=fname, draw_arrow=True, figsize=(9, 5))
        elif save == 'n':
            fig = sol.draw_ellipse()
            # fig.show()
            fig2= S.draw_poincare()
            fig2.show()
    elif choice=='a':
        print(S)
    elif choice == 'b':
        print("Would you like to save the image? y/n")
        save = input()
        if save == 'y':
            print("What would you like to name the file for the ellipse?")
            name = input()
            fname = name + '.jpg'
            sol.draw_ellipse(filename = fname, draw_arrow=True, figsize=(9, 5))
        elif save == 'n':
            fig=sol.draw_ellipse(draw_arrow=True, figsize=(9, 5))
            fig.show()
    elif choice == 'c':
        print("Would you like to save the image? y/n")
        save = input()
        if save == 'y':
            print("What would you like to name the file for the Poincare sphere?")
            sname = input()
            sfname = sname + '.jpg'
            fig =S.draw_poincare(filename=sfname)
            fig.show()
        elif save == 'n':
            fig= S.draw_poincare()
            fig.show()

def GraphRotate(sol):
    S = create_Stokes("Solution Stokes")
    S.from_Jones(sol)
    fig=S.draw_poincare()
    fig.show()

def arbitraryPolarizer(angle):
    angle = float(angle)
    zero = np.cos(angle) * np.cos(angle)
    one = np.cos(angle) * np.sin(angle)
    two = one
    three = np.sin(angle) * np.sin(angle)
    matrixPol = np.array([[zero, one], [two, three]])
    polChoice = Jones_vector('Arbitrary')
    polChoice.from_matrix(matrixPol)
    return polChoice


def arbitraryWavePlate(angle, retardance):
    zero = np.cos(angle) * np.cos(angle) + np.exp(1j * retardance) * np.sin(angle) * np.sin(angle)
    one = (1 - np.exp(1j * retardance)) * np.cos(angle) * np.sin(angle)
    two = (1 - np.exp(1j * retardance)) * np.cos(angle) * np.sin(angle)
    three = np.sin(angle) * np.sin(angle) + np.exp(1j * retardance) * np.cos(angle) * np.cos(angle)
    matrix = np.array([[zero, one], [two, three]])
    J = Jones_matrix().from_matrix(matrix)
    return J

def newCalc():
    s = UserChoice()
    print("How would you like to view the solution: \n a) Stokes \n b) Polarization Ellipse \n c) Poincare Sphere \n d) All")
    view = input()
    Graph(s, view)

def Menu():
    run = 1
    newCalc()
    while run != 0:
        print("What would you like to do now?")
        print(" n: start new calculation")
        print(" e: edit previous calculation")
        print(" r: show the effects of rotating an element")
        print(" x: exit program")
        new = input()
        if new == 'x':
            run = 0
        elif new == 'n':
            newCalc()
        elif new == 'e':
            Edit()
            parseInput()
        elif new == 'r':
            print("Sorry, this option is not currently supported.")
            #print("Your current list is: \n", user_input)
            #print("Enter the number of the element you want to rotate:")
            #ask user for range to be rotated through
            #GraphRotate()

Menu()


# S = Stokes('Linear light')
# S.linear_light(azimuth=0, degree_pol=0.5)
# fig = S.draw_poincare(depol=True) #error says depol is unexpected
# fig.show()

# S = Stokes('Linear light')
# S.linear_light(azimuth=0)
# print(S)
# S.draw_poincare()

# S = Stokes('Linear light')
# S.linear_light(azimuth=90*degrees)
# fig = S.draw_poincare(figsize=(4,4), draw_axes=False, draw_guides=False, show_fig=True)
#
# S = Stokes('Linear light')
# S.general_azimuth_ellipticity(azimuth=np.linspace(0,179*degrees,13), ellipticity=np.linspace(0,45*degrees,13))
# fig = S.draw_poincare(kind="scatterline")
# fig.show()