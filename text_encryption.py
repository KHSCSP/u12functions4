import math
from PIL import Image 
import numpy as np


def create_mat(mess):
    '''
    receives text string
    returns np array of black & white 'encyption'
    '''
    # convert to list of ascii
    # ex: [72, 101, 108, 108, 111, 32, 119]
    asclist = []
    # print("list of ascii values:", asclist)


    # convert to list of binary, removing '0b' prefix
    # ex: ['1001000', '1100101', '1101100', '1101100', '1101111', '100000', '1110111', '1101111']
    binlist = []
    # print("list of binary nums:", binlist)



    # convert to long string
    # ex: 0100100001100101011011000110110001101111001000000111011101
    s = ''

    # print("long string:", s)


    # convert to list of b&w colors
    # 1 becomes (255,255,255), zero becomes (0,0,0)
    # ex: [(0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
    col_list = []

    # print("black & white color list:", col_list)


    # convert to square 2d list
    # length of list, square root, round up
    size = 0
    mat = []
    # print("zeros 2d list:", mat)
    count = 0

    # print("2d list:", mat)


# save to image
def save(mat, filename):
    '''
    receives np array
    saves as image file
    '''
    result = Image.fromarray(np.uint8(mat))
    result.save(filename)




# call your functions
mess = "PLTW AP Computer Science Principles"
