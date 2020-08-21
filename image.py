import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('2020-08-21-153016.jpg').convert("L")
arr = np.array(img)

print(arr)



shape = arr.shape
print(shape)
numSeries = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}

flat_arr = arr.ravel()
print(flat_arr)
totalLen = len(flat_arr)
for num in  flat_arr:
    firstDigit = str(int(num))[:1]
    if(firstDigit != '0'):
        numSeries[firstDigit] += 1 

x_list, y_list = [], []
for key, num in numSeries.items():
    x_list.append(key)
    y_list.append(num)
print(x_list)
print(y_list)

plt.plot(x_list, y_list)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Benfords graph!')
plt.savefig('ex2.png')
plt.show()
