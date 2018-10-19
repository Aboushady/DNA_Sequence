import numpy as np
import matplotlib.pyplot as plt

str_2   = 'asdsdfDFDFcvfFGDFG'
str_1 = 'ASdSDfDFDFcvffgDfG'

match = True
for i in range(len(str_2)):
    if str_2[i].lower() != str_1[i].lower():
        match = False

print('Two strings were match ? ' + str(match) + '\n')
print('This is the first string ' + str_2 + '\n')
print('This is the second string :' + str_1 + '\n')
