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


allowed_string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', ' ']

def reformatPhoneNumber(number):

    #if len(number) in range(7,13)
    ph_number = []
    for i in number:
        if not i in allowed_string:
            raise Exception("Phone Number contains unwanted charactors!")
        else:
            if not i in [' ', '-']:
                ph_number.append(i)

    if len(number) in range(7,13):
        return ''.join(ph_number)
    else:
        raise Exception("Invalid Phone Number!")
if __name__ == '__main__':
    x = reformatPhoneNumber('012-345 69')
    #x = reformatPhoneNumber('012345')
    #x = reformatPhoneNumber('-012345 678')
    #x = reformatPhoneNumber('-012345 6781234567')
    #x = reformatPhoneNumber('01203- 34566')
    #x = reformatPhoneNumber('123456678875432')
    #x = reformatPhoneNumber('1234x567')
    print x