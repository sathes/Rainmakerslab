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
3.
Question: 
Write a function declared as def SplitEmailAddress(address), whose argument will contain string data consisting of a valid e-mail address. This function will take the email address as the argument and return a dictionary with two keys: user for the username part and domain for the domain part of the address. For example, after calling:
dict = SplitEmailAddress('myuser_1@mailserver.example.com') 
dict['user'] should contain the string myuser_1, and  dict['domain'] should contain the string mailserver.example.com

"""

def splitEmailAddress(address):
	if type(address) == str and address.find('@') != -1:
	    username, domain = address.split('@')
	    return dict([('user',username),('domain',domain)])
	else:
		raise Exception(" Invalid input!")

if __name__ == '__main__':
    dict = splitEmailAddress('myuser_1@mailserver.example.com')
    print dict['user']
    print dict['domain']