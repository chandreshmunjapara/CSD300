import  math
import numpy as np
from PIL import Image

def return_psnr(pix,secret):
    x_offset = 50
    y_offset = 50
    total = 256 * 256
    j = 0
    i = 0
    k = 0
    l = 0
    val = 0
    prev = 0
    mse = 0


    while (total != 0):
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        prev = pix[x_offset][y_offset]
        # print(type(secret[l]))
        pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
        # print(pix[x_offset][y_offset])
        mse += ((prev - pix[x_offset][y_offset])**2)
        # print(mse)
        j += 1
        if j == 256:
            i += 1
            j = 0
        y_offset += 1
        if y_offset == 256:
            x_offset -= 1
            if x_offset == -1 and y_offset == 256:
                x_offset = 255
            y_offset = 0
        l += 2
        total -= 1

    array = np.array(pix, dtype=np.uint8)
    new_image = Image.fromarray(array)
    new_image.save("new.png")
    mse = mse/(256*256)
    psnr = 10 * math.log10((255*255) / mse)
    print(psnr)

