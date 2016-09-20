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


def generateNumbers():
    
    x = [i for i in range(200,601) if i%8 == 0]
    return  ','.join(map(str,sorted(x)))


if __name__ == '__main__':
    x = generateNumbers()
    print x