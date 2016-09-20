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

"""
2.
Question: 
You are given an array in Python, which contains positive integers and/or recursively nested arrays of positive integers. It may, for example, be initialized as:
arr = [[141,151,161],2,3,[101,202,[303,404]]]
Write a function def MaxArray(arr) which returns the maximum value contained in arr or some array nested within arr. In the example, the returned value should be 404. 

"""

def maxArray(l=None):
    if not l or l == None:
        raise Exception("Invalid entry of array!")
    else:
        lis = nested_list_to_list(l)
        return max(lis)

def nested_list_to_list(l=None):
    result = []
    if l != None:
        for elem in l:
            if type(elem) == list:
            	if len(elem) >= 2:
    	            for e in nested_list_to_list(elem):
    	                result.append(e)
    	        else:
    	        	result.append(elem[0])
            else:
                result.append(elem)
    return result

if __name__ == '__main__':
    x=maxArray([[141,151,161],2,3,[101,202,[303,404]]])
    #x=maxArray([141,151,161,2,3,101,202,303,40])
    print x