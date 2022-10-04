from urllib import response
import pyinputplus as pi

# response = pi.inputNum('enter only number:')


# print(response)
# print(dir(pi))

# response = pi.inputNum('Enter the Num;',min=4)
# response = pi.inputNum('Enter the Num;',timeout=10,default=789) #also have limit argument and default,BLANK
# print(response)

making = pi.inputStr(allowRegexes=[r'category'],blockRegexes=[r'cat'])
print(making)
