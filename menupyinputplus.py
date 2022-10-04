from secrets import choice
from urllib import response
import pyinputplus as pi

choice = ['burger','sandwich','pasta']

response = pi.inputMenu(choice,prompt='make your choice:\n',numbered=True)
if response == 'burger':
    print("jaggi")