#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sat
#
# Created:     13/01/2015
# Copyright:   (c) Sat 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def generatePassword(size = 0, char = None):
    if size != 0 and char != None:
        passwd = []
        for i in range(size):
            passwd.append(random.choice(char))
        return ''.join(passwd)
    else:
        raise Exception('Invalid Input!')

if __name__ == '__main__':
    x = generatePassword(7'abczxc012394')
    print x