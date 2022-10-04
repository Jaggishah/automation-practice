from logging import exception
from urllib import response
import pyinputplus as pii

def addnum(number):
    numberslist = list(number)

    for  i,digit in enumerate(numberslist):
        numberslist[i] = int(digit)

        if sum(numberslist) != 10:
            raise exception('number is must be 10,not')
        return int(number)


response = pii.inputCustom(addnum)





