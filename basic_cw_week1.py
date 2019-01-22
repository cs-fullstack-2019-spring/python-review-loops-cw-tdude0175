# Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
#
# Hint: Use 'continue' statement.
#
# Expected Output : 0 1 2 4 5

def main():
    # problem1()
    # problem2()
    # problem3()
    bonus()

# you can also use a while loop
#  if number == 3 or number == 6
# if we had switch cases we could use a switch case inside the loop and have the input be [number]

def problem1():
    for number in range(6):
        if (number%3 == 0):
            continue
        else:
            print(number)

# Write a Python program to count the number of even and odd numbers from a series of numbers.
#
# Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# Expected Output :
#
# Number of even numbers : 5
# Number of odd numbers : 4

# don't need to define more then one condition for it to log into one
# if a number is not even it's odd
# could you use a while loop?

def problem2():
    evenNum = 0
    oddNum = 0

    ending = int(input("gimme a number to end on"))

    for number in range(1,ending+1):
        if (number%2 == 0):
            evenNum +=1
        else:
            oddNum +=1

    print("number of even numbers: " + str(evenNum))
    print("number of odd numbers: " + str(oddNum))


# Write a Python program that accepts a sequence of lines
# (blank line to terminate) as input and prints the lines as output after User enters a blank line to end
#
# Do not use an array to hold the lines of text
#
# Hints: You can use "\n" if you want to add a line break between sentences

# don't need to print it every time
#  without adding it to an array how would you return all sentences
#

def problem3():
    userInput = input("")
    while(True):

        newInput = input("")

        if (newInput== ""):
            print("")
            break
        else:
            userInput += ("\n" + newInput)
    print(userInput)


# Write a Python program to construct the following pattern, using a nested for loop.
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# build a loop
# using a loop inside to go backwards
#  doing it without a loop
#  need to define the end of the line and when you hit the end start subtracting
# growing without loops

def bonus():
    z = 0
    for y in range(0,10):

        if y > 5:
            z+=2
            print("*"*(y-z))

            # for x in range(4,0,-1):
            #     print("*"*x)
        else:
            print("*"*y)







if __name__ == '__main__':
    main()