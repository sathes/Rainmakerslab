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


def getLongestStr(a=None):
	if a != None and hasattr(a, '__iter__') == True and all(isinstance(x,str) for x in a) == True:
		return max(map(len, a))
	else:
		raise Exception('Invalid input!')


if __name__ == '__main__':
    x = getLongestStr(("a", "bcd", "efgh", "ij", ""))
    #x = getLongestStr((1,4,6,7))
    print x