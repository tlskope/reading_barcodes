#%%

import cv2
from pyzbar.pyzbar import decode 

img = cv2.imread('test_barcode.png')

print(img)

print (len(decode(img)))

for code in decode(img):
    print(code.type)
    print(code.data)

# %%
