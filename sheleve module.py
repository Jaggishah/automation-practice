import imp


import shelve
# make a file
shefile = shelve.open('mydata')
cats = ['jaggi' , 'shah' , 'panjab']
shefile['cats'] = cats
shefile.close()

# print(list(shefile.keys()))
# pprint.pformat