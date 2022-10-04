from urllib import response
import pyinputplus as pii
# import time
print("you have two number:10 and second numbeer is 15/npleae enter the exact wht we /ngot after multiplication")

response = pii.inputInt('enter the result:',allowRegexes=['^%s$'%(10*15)],blockRegexes=['.*','incorrect'],limit=3)
# time.sleep(2)
print(response)

