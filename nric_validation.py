# Filename: nric_validation.py
# Name: Ng Cheryl
# Created: 20130408
# Updated: 20130408
# Description: program to validate user-input NRIC

import re

# define functions to validate alphabets of NRIC
def check_alphabet(nric):
    '''function to determine check alphabet of valid NRIC'''
    weights = [2, 7, 6, 5, 4, 3, 2]
    sum_products = 0
    check_map = {21:'K', 20:'L', 19:'M', 18:'N', 17:'P', 16:'Q', 15:'R', 14:'T', 13:'U',
                12:'W', 11:'X', 10:'A', 9:'B', 8:'C', 7:'D', 6:'E', 5:'F', 4:'G', 3:'H', 2:'I',
                1:'Z', 0:'J', -1:'H', -2:'I', -3:'Z', -4:'J'}
    for i in range(1,8):
        sum_products = sum_products + (int(nric[i]) * weights[i-1])
    remainder = sum_products % 11
    if nric[0] == "t" or nric[0] == "T":
        remainder = remainder - 4
    elif nric[0] == "f" or nric[0] == "F":
        remainder = remainder + 11
    elif nric[0] == "g" or nric[0] == "G":
        remainder = remainder + 7
    if check_map[remainder] == nric[8]:
        return True
    else:
        return False


valid_nric = False
while not valid_nric:
    # get nric from user
    nric = input("Please enter your NRIC: ")

    # set pattern
    pattern = re.compile("^[sStTgGfF][0-9]{7}[a-zA-Z]$")
    
    if pattern.match(nric):
        if not 1 < int(nric[1]) < 6:
            print (check_alphabet(nric))
        else:
            print(False)
        valid_nric = True
    else:
        print("Please check input. Make sure the format is <1 letter><7 digits><1 letter>\n")
        

