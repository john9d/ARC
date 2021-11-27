#!/usr/bin/python

import os, sys
import json
import numpy as np
import re
import math
from scipy import stats

### YOUR CODE HERE: write at least three functions which solve
### specific tasks by transforming the input x and returning the
### result. Name them according to the task ID as in the three
### examples below. Delete the three examples. The tasks you choose
### must be in the data/training directory, not data/evaluation.


'''
###this one works!!!

def solve_22eb0ac0(x):
    for i in x:

        if i[0] == i[-1]:
            value = i[0]
            item = i[1]
            
            index = [j for j, y in enumerate(i) if y==item]
            #print(index)

            for a in index:
                i[a] = value

    return x

'''

'''
###this one works!!!
def solve_0d3d703e(x):
    
    x = np.where(x == 1, 5/math.pi, x)

    x = np.where(x == 2, 6/math.pi, x)

    x = np.where(x == 3, 4/math.pi, x)
    x = np.where(x == 4, 3/math.pi, x)
    x = np.where(x == 6, 2/math.pi, x)
    x = np.where(x == 8, 9/math.pi, x)


    x = np.where(x == 5, 1/math.pi, x)
    x = np.where(x == 9, 8/math.pi, x)

    x = (x*math.pi)//1



    return x

'''

def solve_ce4f8723(x):
    '''
    ########################### SOLUTION No.3 ###############################
    Using the ARC testing interface Task ce4f8723 shows a 9x4 array. Where there
    are two 4x4 arrays with coloured and black squares, separated by a 1x4 array
    to divide the two 4x4 arrays.

    The results of each problem demonstrate that when overlay the two 4x4 arrays,
    the resulting array shows only black squares in the resulting 4x4 array where
    both have them. Colouring all of the other squares in a different colour (green!)
    '''


    # First we need to define the shape of the array being assessed using .shape
    h, w = x.shape

    # Then we need to flatten nDimension out the array to a 1D array
    y = x.ravel()

    # As the problem shows
    y1 = y[0:(w*w)]
    y2 = y[(w*w+w):]
    y_total = (y1+y2)

    value = 3

    index = [j for j, a in enumerate(y_total) if a != 0]

    for b in index:
        y_total[b] = value
    x = y_total.reshape(w, -w)

    return x


def solve_e26a3af2(x):
    '''
    ########################### SOLUTION No.4 ###############################
    Using the ARC testing interface Task e26a3af2 shows a varying NxM arrays.
    Where some of the arrays N = M. In each of the tasks, there is either a
    vertical or horizontal lines of varying width containing primarily 3 or 4
    colours (numbers), with a random placement of any colour throughout. Each
    task solution clears out the random colours and leaves a neat 3 or 4 colour
    lines. The test grid is 5 colours in a horizontal arrangement.

    To solve the task we will enumerate the array and identify the mode colour
    in each row of the array, inorder to create a new NxM array in clean of any
    random colours. This will work with the horizontally aligned colours easily,
    however we will need to transpose the array for the vertically aligned colours.
    An if statement that will assess if the mode is greater than 1/2 of the array
    width (as all arrays have 3 or more colours) will be able to ensure the mode
    and array will be correctly reformed.

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
        '''The mode is less than half the count so we will use the transposed array'''
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
        '''The mode is more than half the count so we will use the normal array'''
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

