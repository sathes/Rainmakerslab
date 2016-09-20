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


def getUniqueOnes(a=None):
	if a != None:
		return ','.join(map(str,sorted(list(set(a)))))
	else:
		raise Exception('Invalid input!')

if __name__ == '__main__':
	arr = [34,54,67,68,141,151,161,141,54,151,54]
	x = getUniqueOnes(arr)
	print x