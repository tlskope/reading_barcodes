#%%

import cv2
from pyzbar.pyzbar import decode
import csv

list = []
img = cv2.imread('test_barcode_3.png')
for code in decode(img):
    print(code.type)
    print(code.data)
    print(code.data.decode('utf-8'))
    list.append(code.data.decode('utf-8'))

print(list)
fields = []
with open('list_of_barcodes.csv','w') as f:
    write = csv.writer(f)
    write.writerows([list])


