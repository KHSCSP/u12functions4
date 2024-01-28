from PIL import Image 
import numpy as np
import random

def create_mat(size_param):
    '''
    receives size (width & height of square)
    returns np array of random colors
    '''
    # create a 2D list, randomize
    size = size_param
    mat = []
    # print("zeros 2d list:", mat)
    # TODO

    # print("2d list:", mat)

def save(mat, filename):
    '''
    receives np array
    saves as image file
    '''
    result = Image.fromarray(np.uint8(mat))
    result.save(filename)


# call your functions
