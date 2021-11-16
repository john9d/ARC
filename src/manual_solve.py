#!/usr/bin/python

import os, sys
import json
import numpy as np
import re

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
def solve_3bdb4ada(x):
    for i in x:

        #if i != 0:
            #item = i[1]

            index = [j for j, y in enumerate(i) if y != 0]
            print(index)

            #for a in index:
             #   i[a] = value

    return x

def solve_3bdb4ada(x):
    a = 0
    for j, y in enumerate(x):
        for i in y:
            if i != 0:
                print(i)

            #for a in index:
             #   i[a] = value

    return x
'''
def solve_0d3d703e(x):
    #for i in x:
    x = np.where(x == 1, 5/4, x)

    x = np.where(x == 2, 6/4, x)

    x = np.where(x == 3, 4/4, x)
    x = np.where(x == 4, 3/4, x)
    x = np.where(x == 6, 2/4, x)
    x = np.where(x == 8, 9/4, x)


    x = np.where(x == 5, 1/4, x)
    x = np.where(x == 9, 8/4, x)

    x = x*4
    x - x.astype(int)



    '''
    a = 0
    x = x.flatten
    print(x)
    for i in x:

        if i[a] == 2:
            i[a] = 6
        elif i[a] == 3:
            i[a] = 4
        elif i[a] == 8:
            i[a] = 9
        a +=1
'''

    return x






#def solve_08ed6ac7(x):
 #   H, W = x.shape
  #  y = x.copy()
    #gray, blue, red, green, yellow = color2num["gray"], color2num["blue"], color2num["red"], color2num["green"], color2num[
    #    "yellow"]
   # colors = [1, 2, 3, 4]
    #colors_idx = 0
    #for yy in range(H):
     #   for xx in range(W):
      #      if y[yy, xx] == 5:
       #         for y_ in range(yy, H):
        #            y[y_, xx] = colors[colors_idx]
         #           #print(y)
          #      colors_idx += 1
    #return x


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

