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
'''
def solve_ce4f8723(x):
    '''
    #Using the ARC testing interface Task ce4f8723 shows a 9x4 array.
    #Where there are two 4x4 arrays with coloured and black squares,
    #separated by a 1x4 array to divide the two 4x4 arrays.

    #The results of each problem demonstrate that when overlay the two
    #4x4 arrays, the resulting array shows only black squares in the
    #resulting 4x4 array where both have them. Colouring all of the other
    #squares in a different colour (green!)

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
'''
def solve_6cf79266(x):
    def get_closed_area(arr):
        # depth first search
        H, W = arr.shape
        Dy = [0, -3, 0, 3]
        Dx = [3, 0, -3, 0]
        arr_padded = np.pad(arr, ((3, 3), (3, 3)), "constant", constant_values=0)
        searched = np.zeros(arr_padded.shape, dtype=bool)
        searched[0, 0] = True
        q = [(0, 0)]
        while q:
            y, x = q.pop()
            for dy, dx in zip(Dy, Dx):
                y_, x_ = y + dy, x + dx
                if not 0 <= y_ < H + 2 or not 0 <= x_ < W + 2:
                    continue
                if not searched[y_][x_] and arr_padded[y_][x_] == 0:
                    q.append((y_, x_))
                    searched[y_, x_] = True
        res = searched[3:-3, 3:-3]
        res |= arr == 0
        return ~res

    #x = x.copy()
    x[get_closed_area(x)] = 5
    return x
'''

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

