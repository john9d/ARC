#!/usr/bin/python

import os, sys
import json
import numpy as np
import re
import math


### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.

def solve_22eb0ac0(x):
    '''
    ########################### SOLUTION No.1 ###############################
    #Using the ARC testing interface Task 22eb0ac0 shows a 10x10 array where there
    #are a number of colours vertically aligned and opposing each other on the
    #left and right side of the array. The task solutions show an array where the
    #a row in the array is filled in wth a colour that had a match of colour on the
    #left and right hand side. Any colours that do not match, will leave the row
    #black in between.

    #To solve this task we will need iterate through the array to adn create an if
    #statement to see if the start of the row and the end of the row match. If this
    #is true, we will enumerate the row, identify and replace all of the colours in
    #between with the match left and right colour.
    '''
    # Initiate loop through the array
    for i in x:

        # We will now check for the matching numbers
        if i[0] == i[-1]:

            # We will need to store the number so we can replace the non-matching ones
            value = i[0]

            # We will store the non-matching number
            item = i[1]

            # Enumerate through the row and create an index of the non-matching values
            index = [j for j, y in enumerate(i) if y==item]

            # We will now loop through the index list so we can replace this values
            for a in index:

                # This will now replace the non-matching values
                i[a] = value

    return x

def solve_0d3d703e(x):
    '''
    ########################### SOLUTION No.2 ###############################
    #Using the ARC testing interface Task 0d3d703e shows a 3x3 array of 3 colours,
    #all vertically aligned. Each colour is converted in the solution i.e. green to
    #yellow, blue to grey, etc. and the conversion is mirrored i.e. yellow to green,
    #grey to blue, etc. The test task has an array of light blue, blue and green all
    #of which need to be converted to wine, grey and yellow respectively.

    #To solve this task we will need to convert each colour (number), however there
    #are overlaps in colours. If we attempt to simply convert each number to its
    #solved state, the number will be reconverted back i.e. when updating 1 to 5, next
    #in the array we are required to update 5 to 1. This will return the old number.
    #To avoid this, we are going to divide by an irrational number (pi in this case)
    #so we can avoid double conversion. Post this, we will multiple the array by pi and
    #perform floor division to remove a chance of a floating point error.
    '''

    # We are going search the array and covert 1 to 5 and divide by pi
    x = np.where(x == 1, 5/math.pi, x)

    # We are going search the array and covert 2 to 6 and divide by pi
    x = np.where(x == 2, 6/math.pi, x)

    # We are going search the array and covert 3 to 4 and divide by pi
    x = np.where(x == 3, 4/math.pi, x)

    # We are going search the array and covert 4 to 3 and divide by pi
    x = np.where(x == 4, 3/math.pi, x)

    # We are going search the array and covert 6 to 2 and divide by pi
    x = np.where(x == 6, 2/math.pi, x)

    # We are going search the array and covert 8 to 9 and divide by pi
    x = np.where(x == 8, 9/math.pi, x)

    # We are going search the array and covert 5 to 1 and divide by pi
    x = np.where(x == 5, 1/math.pi, x)

    # We are going search the array and covert 9 to 8 and divide by pi
    x = np.where(x == 9, 8/math.pi, x)

    # We are going now multiply the array by pi and perform a floor division
    # This will return remove the floating point error
    x = (x*math.pi)//1

    return x

def solve_ce4f8723(x):
    '''
    ########################### SOLUTION No.3 ###############################
    #Using the ARC testing interface Task ce4f8723 shows a 9x4 array. Where there
    #are two 4x4 arrays with coloured and black squares, separated by a 1x4 array
    #to divide the two 4x4 arrays. The results of each task demonstrate that when
    #overlay the two 4x4 arrays, the resulting array shows only black squares in
    #the resulting 4x4 array where both have them. Colouring all of the other squares
    #in a different colour (green!)

    #To solve this task we will need to identify the shape of the array, and then we will
    #flatten the array to (1, N), where N is the total number of items in the array. As
    #we need to combine the two 4x4 coloured arrays we will then split the (1,N) array
    #into two, removing the dividing array. We shall then add the two arrays together and
    #then enumerate it to find where there are black colours (0). We then replace the
    #black (non-zero) with the green and reshape to the correct format for the output.
    '''


    # First we need to define the shape of the array being assessed using .shape
    h, w = x.shape

    # Then we need to flatten nDimension out the array to a (1, N) array
    y = x.ravel()

    # We need to split out the top array of colours from 0 to the width times the width
    # index in the flatten array. This will future proof should we any other NxN array
    y1 = y[0:(w*w)]

    # We will split out the bottom array of colours, removing the 1x4 array by starting
    # the index at width times the width plus the width
    y2 = y[(w*w+w):]

    # Add the two arrays together so we can identify the black (zeros)
    y_total = (y1+y2)

    # Set the value for the green output colour
    value = 3

    # Enumerate through the list to identify the zeros in the combined arrays
    index = [j for j, a in enumerate(y_total) if a != 0]

    # We now need to iterate through the list of non-zeros
    for b in index:

        # Replacing the values with the green (3)
        y_total[b] = value

    # Now we will reshape the (1, N) array back to the correct shape
    x = y_total.reshape(w, -w)

    return x

def solve_e26a3af2(x):
    '''
    ########################### SOLUTION No.4 ###############################
    #Using the ARC testing interface Task e26a3af2 shows a varying NxM arrays.
    #Where some of the arrays N = M. In each of the tasks, there is either a
    #vertical or horizontal lines of varying width containing primarily 3 or 4
    #colours (numbers), with a random placement of any colour throughout. Each
    #task solution clears out the random colours and leaves a neat 3 or 4 colour
    #lines. The test grid is 5 colours in a horizontal arrangement.

    #To solve the task we will enumerate the array and identify the mode colour
    #in each row of the array, inorder to create a new NxM array in clean of any
    #random colours. This will work with the horizontally aligned colours easily,
    #however we will need to transpose the array for the vertically aligned colours.
    #An if statement that will assess if the mode is greater than 1/2 of the array
    #width (as all arrays have 3 or more colours) will be able to ensure the mode
    #and array will be correctly reformed.
    '''


    # We need to create an empty list for mode colour in each row
    mode = []

    # We need to create an empty list for maximum number of colours in each row
    # This will allow us to verify if we need to transpose the array
    total = []

    # Gather the height and width of the array so we can create the new array correctly
    h, w = x.shape

    # We will enumerate x to identify the the mode colour in each row
    for i, j in enumerate(x):

        # Create a list of each value and count of each to identify the mode
        vals, counts = np.unique(x[i], return_counts=True)

        # Capture the value tha made the colour the mode
        total = max(counts)

        # Create an location index for the value which is the mode
        index = np.argmax(counts)

        # Store the mode in the row
        c = vals[index]

        # Append the mode to the global list
        mode = np.append(mode, [c], axis=0)

    # We will now transpose the array and complete the same tasks as above
    # We need to create an empty list for mode colour in each row
    x_T = x.T

    # We need to create an empty list for maximum number of colours in each row
    # This will allow us to verify if we need to transpose the array
    mode_T = []

    # Gather the height and width of the array so we can create the new array correctly
    h_T, w_T = x_T.shape

    # We will enumerate x to identify the the mode colour in each row
    for i_T, j_T in enumerate(x_T):

        # Create a list of each value and count of each to identify the mode
        vals_T, counts_T = np.unique(x_T[i_T], return_counts=True)

        # Create an location index for the value which is the mode
        index_T = np.argmax(counts_T)

        # Store the mode in the row
        c_T = vals_T[index_T]

        # Append the mode to the global list
        mode_T = np.append(mode_T, [c_T], axis=0)

    # Create an if statement to verify if we are working with a vertical task
    if total < w/2:
        ##The mode is less than half the count so we will use the transposed array##
        # Create an empty numpy array
        f_T = np.array([])

        # Iterate through the global mode list created
        for i in mode_T:
            # Append each mode value as a new row and multiply it by the width of
            # of the original transposed array
            f_T = np.append(f_T, [i] * w_T, axis=0)

        # Reshape the new array to the original transposed array
        r = f_T.reshape(h_T, w_T)

        # Transpose the new array back to its original shape
        x = r.T

    # Else we are now working with a horizontal type task
    else:
        ##The mode is more than half the count so we will use the normal array##
        # Create an empty numpy array
        f = np.array([])

        # Iterate through the global mode list created
        for i in mode:

            # Append each mode value as a new row and multiply it by the width of
            # of the original array
            f = np.append(f, [i] * w, axis=0)

        # Reshape the new array to the original array
        x = f.reshape(h, w)

    return x

def solve_9ecd008a(x):
    '''
    ########################### SOLUTION No.5 ###############################
    Using the ARC testing interface Task 9ecd008 shows a large 20x20 array.
    All with a pattern of different colours. Each task has a small 3x3 array with
    colour missing, the solution for each task is to create a 3x3 of the missing
    colours in the correct pattern. As each pattern is mirrored on x and y axes where
    10x20 = 10x20 and 20x10 = 20x10, the missing pattern is its mirror on the y axis
    in each task.

    To solve the task we will enumerate the array and identify which rows contain
    a black (zero) square by calculating the length of the row with no black. If
    the row has black square, we will pass this into another loop to enumerate for
    the index of the black square in the row. In turn getting the absolute difference
    between the index and the length of the row so we capture the index of the mirror
    colours. We will then append the correct colour into a new list and finally
    reshape it to the 3x3 array.
    '''
    # 1st we will create an empty list to append the correct pattern into
    answer = []

    # We will now get the shape of the array to determine the length of each row
    h, w = x.shape

    # We will now start the loop through the array
    for i in x:

        # We will set the value for the black square
        black = 0

        # We will enumerate to identify the length of each row that has a black square
        non_count = [j for j, y in enumerate(i) if y != black]

        # Now create an if statement to pass the row into the next loop if contains a
        # black square
        if len(non_count) != w:

            # We will now enumerate to identify the count of the black squares
            zero_index = [j for j, y in enumerate(i) if y == black]

            # Create a (1,3) array of the maximum index number so we can calculate
            # the mirror location of the black square
            mirror_index = [w - 1] * max(zero_index)

            # Create an empty list of the mirrored index number
            index = []

            # Create a loop to get the location of the black square and the mirror
            # location by getting the absolute difference between the indexes
            for q, p in zip(mirror_index, zero_index):
                index.append(abs(q - p))

            # Finally we will append the colour of the mirrored index in the row
            for c in index:

                # Append the colour to the def global answer
                answer = np.append(answer, [i[c]], axis=0)

    # We will now reshape the list to the correct array size
    x = answer.reshape(3, -3)

    return x

def main():
    # Find all the functions defined in this file whose names are
    # like solve_abcd1234(), and run them.

    # regex to match solve_* functions and extract task IDs
    p = r"solve_([a-f0-9]{8})" 
    tasks_solvers = []
    # globals() gives a dict containing all global names (variables
    # and functions), as name: value pairs.
    for name in globals(): 
        m = re.match(p, name)
        if m:
            # if the name fits the pattern eg solve_abcd1234
            ID = m.group(1) # just the task ID
            solve_fn = globals()[name] # the fn itself
            tasks_solvers.append((ID, solve_fn))

    for ID, solve_fn in tasks_solvers:
        # for each task, read the data and call test()
        directory = os.path.join("..", "data", "training")
        json_filename = os.path.join(directory, ID + ".json")
        data = read_ARC_JSON(json_filename)
        test(ID, solve_fn, data)
    
def read_ARC_JSON(filepath):
    """Given a filepath, read in the ARC task data which is in JSON
    format. Extract the train/test input/output pairs of
    grids. Convert each grid to np.array and return train_input,
    train_output, test_input, test_output."""
    
    # Open the JSON file and load it 
    data = json.load(open(filepath))

    # Extract the train/test input/output grids. Each grid will be a
    # list of lists of ints. We convert to Numpy.
    train_input = [np.array(data['train'][i]['input']) for i in range(len(data['train']))]
    train_output = [np.array(data['train'][i]['output']) for i in range(len(data['train']))]
    test_input = [np.array(data['test'][i]['input']) for i in range(len(data['test']))]
    test_output = [np.array(data['test'][i]['output']) for i in range(len(data['test']))]

    return (train_input, train_output, test_input, test_output)


def test(taskID, solve, data):
    """Given a task ID, call the given solve() function on every
    example in the task data."""
    print(taskID)
    train_input, train_output, test_input, test_output = data
    print("Training grids")
    for x, y in zip(train_input, train_output):
        yhat = solve(x)
        show_result(x, y, yhat)
    print("Test grids")
    for x, y in zip(test_input, test_output):
        yhat = solve(x)
        show_result(x, y, yhat)

        
def show_result(x, y, yhat):
    print("Input")
    print(x)
    print("Correct output")
    print(y)
    print("Our output")
    print(yhat)
    print("Correct?")
    if y.shape != yhat.shape:
        print(f"False. Incorrect shape: {y.shape} v {yhat.shape}")
    else:
        print(np.all(y == yhat))


if __name__ == "__main__": main()

