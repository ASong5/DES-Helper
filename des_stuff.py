#!/usr/bin/python3

import numpy as np
import pandas as pd


def simplified_initial_permutation(table):
    final_permutation = [None] * 9
    i = 1
    for idx in table:
        final_permutation[idx - 1] = i
        i += 1
    return pd.DataFrame(np.array(final_permutation).reshape(3, 3))

def initial_permutation(bit_string):
    ip_table = [
    58,50,42,34,26,18,10,2,60,52,44,36,28,20,
    12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,
    24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,
    19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,
    23,15,7
    ]

    bit_string = bit_string.replace(" ", "")
    new_string = ""
    for idx in ip_table:
        new_string += bit_string[idx - 1]
    return new_string

def final_permutation(bit_string):
    p_table = [
        16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25
    ]

    bit_string = bit_string.replace(" ", "")
    new_string = ""
    for idx in p_table:
        new_string += bit_string[idx - 1]
    return new_string


def expansion_permutation(bit_string):
    ebit_selection_table = [
        32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15,
        16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28,
        29, 28, 29, 30, 31, 32, 1
    ]

    bit_string = bit_string.replace(" ", "")
    new_string = ""
    for idx in ebit_selection_table:
        new_string += bit_string[idx - 1]

    return new_string


def XOR(key, bit_string):
    bit_string = bit_string.replace(" ", "")
    return int(key, 2) ^ int(bit_string, 2)


def s_box(bit_string):
    S = [
        # S1
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        # S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],

        # S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],

        # S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],

        # S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],

        # S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],

        # S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],

        # S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
    ]
    bit_string = bit_string.replace(" ", "")
    split_bit_string = [
        bit_string[i:i + 6] for i in range(0, len(bit_string), 6)
    ]
    result = ""
    s_box_idx = 0
    
    i = int(split_bit_string[0] + split_bit_string[-1], 2)
    j = int(split_bit_string[1:5], 2)
    result += "{0:04b}".format(S[s_box_idx][i][j])
    s_box_idx += 1


def e_permutation(bit_string):
    e_table = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18,
               31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    
    bit_string = bit_string.replace(" ", "")
    final_permutation = ""
    for idx in e_table:
        final_permutation += bit_string[idx - 1]
    return final_permutation


def main():
    # print("IP:\n" +
    #       simplified_initial_permutation([
    #           3,7,6,5,2,4,9,1,8
    #       ]).to_string(header=False, index=False))  # just prints it in matrix form for readability

    print("IP: " + initial_permutation("01010010 01001001 01000011 01001000 01001101 01001111 01001110 01000100"))
    print("FP: " + final_permutation("1111 1100 0001 1101 0110 0110 1000 1010"))

    e = expansion_permutation("111111100000001111100000011011000000000000000000111101001100101")
    x = XOR("11111111000000011111000000110110 ", "10001100101011101001001011011011")
    s = s_box("111010")
    # ep = e_permutation(s)

    print("Expansion: " + e)

    print("XOR: " + '{0:b}'.format(x))

    print("S-Box: " + " ".join([s[i:i+4] for i in range(0, len(s), 4)]))

    # print("E-Permutation: " + " ".join([ep[i:i+4] for i in range(0, len(ep), 4)]))


main()
