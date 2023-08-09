# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KHarms,8.6.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {priority: newPriority, task: newTask}
lstTable = []  # A list that acts as a 'table' of dictionary rows
strExit = ""   # A menu of user options
strChoice = "" # A variable to capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:  # use try/except so initially empty file does not produce error
    strData = open(objFile, 'r')
    print('Your saved tasks: ')
    for row in strData:  # step through each line in file to get data
        lstRow = row.split(',')
        print(lstRow[0] + ',' + lstRow[1])
        dicRow={'priority':lstRow[1].strip(), 'task':lstRow[0]}  # use list index to put values in correct key pair
        lstTable += [dicRow]  # add to table
    strData.close()
except:  # message to user that list is empty
    print('Congratulations, your To Do list is empty. Would you like to add a new task? ')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Your To Do list contains:')
        for row in lstTable:
            print(row['task'] + ': ' + row['priority'] + ' priority')
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = input('Enter a task: ')
        newPriority = input(f'Enter the priority for {newTask}: ')
        dicRow = {'priority': newPriority, 'task':newTask}
        lstTable += [dicRow]
        print(f'You entered {newTask}, with {newPriority} priority\n')
        # print(lstTable)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        count = 0  # set up counter so can have user indicate index of item to be deleted
        for row in lstTable:
            strCount = str(count)
            print(strCount + ': ' + row['task'] + ', ' + row['priority'] + ' priority')
            count += 1
        itemRemove = input('Which task would you like to delete? Enter item number: ')
        intRemove = int(itemRemove)
        # print(lstTable[intRemove])
        del lstTable[intRemove]
        print('Your remaining To Do items are: ')  # tell user which tasks remain
        for row in lstTable:
            print(row['task'] + ': ' + row['priority'] + ' priority')
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        strData = open(objFile, 'w')
        print('Your tasks saved to file: ')  # tell user what saved to file
        for row in lstTable:
            print(row['task'] + ',' + row['priority'])
            strData.write(row['task'] + ',' + row['priority'] + '\n')
        strData.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):  # give user chance to return to program to save or alter
        strExit = str(input('Did you save all your changes? If you are ready to exit, enter y. If you want to continue, enter n: '))
        if strExit.lower() == 'y':
            break  # and Exit the program
        elif strExit.lower() == 'n':
            continue

    else:
        # any other input redirect to Menu
        print('Please choose 1 to 5 - ')
        continue

