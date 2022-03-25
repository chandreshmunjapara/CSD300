import math
import numpy as np
from PIL import Image

def getValue(arr) :
    res = int("".join(str(x) for x in arr), 2)
    return res

def return_psnr(pix, secret, population):
    x_offset = getValue(population[14:22])
    y_offset = getValue(population[6:14])
    direction = getValue(population[2:6])
    sb_pole = getValue(population[1:2])
    sb_dir = getValue(population[0:1])
    val = 0
    prev = 0
    mse = 0
    l = 0

    if(sb_pole):
        for i in range(len(secret)):
            if secret[i] == '0':
                secret[i] = '1'
            else:
                secret[i] = '0'


    if(sb_dir):
        secret.reverse()

    def zero(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while total != 0:
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            y_offset += 1
            if y_offset == 256:
                x_offset -= 1
                if x_offset == -1 and y_offset == 256:
                    x_offset = 255
                y_offset = 0
            l += 2
            total -= 1
        return pix

    def one(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1 and x_offset == 256:
                    y_offset = 255
                x_offset = 0
            l += 2
            total -= 1
        return pix

    def two(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)

            y_offset -= 1
            if y_offset == -1:
                x_offset +=1
                if x_offset == 256 and y_offset == -1:
                    x_offset = 0
                y_offset = 255
            l += 2
            total -= 1
        return pix

    def three(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            x_offset -= 1
            if x_offset == -1:
                y_offset += 1
                if y_offset == 256 and x_offset == -1:
                    y_offset = 0
                x_offset = 255
            l += 2
            total -= 1
        return pix

    def four(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            y_offset += 1
            if y_offset == 256:
                x_offset += 1
                if y_offset == 256 and x_offset == 256:
                    x_offset = 0
                y_offset = 0
            l += 2
            total -= 1
        return pix
    def five(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            x_offset += 1
            if x_offset == 256:
                y_offset += 1
                if y_offset == 256 and x_offset == 256:
                    y_offset = 0
                x_offset = 0
            l += 2
            total -= 1
        return pix
    def six(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            y_offset -= 1
            if y_offset == -1:
                x_offset -= 1
                if y_offset == -1 and x_offset == -1:
                    x_offset = 255
                y_offset = 255
            l += 2
            total -= 1
        return pix

    def seven(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            x_offset -= 1
            if x_offset == -1:
                y_offset -= 1
                if y_offset == -1 and x_offset == -1:
                    y_offset = 255
                x_offset = 255
            l += 2
            total -= 1
        return pix

    def eight(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            if x_offset%2==0:
                y_offset+= 1
                if y_offset == 256:
                   x_offset += 1
                   y_offset = 255
            else:
                y_offset -= 1
                if y_offset==-1:
                    x_offset+=1
                    if x_offset==256:
                        x_offset=0
                y_offset=0
            l += 2
            total -= 1
        return pix

    def nine(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            if y_offset % 2 == 0:
                x_offset += 1
                if x_offset == 256:
                    y_offset -= 1
                    if y_offset == -1:
                       y_offset = 255
                    x_offset=255
            else:
                x_offset -= 1
                if x_offset == -1:
                    y_offset -= 1
                    x_offset = 0
            l += 2
            total -= 1
        return pix

    def ten(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            # print(mse)
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1 and x_offset == 256:
                    y_offset = 255
                x_offset = 0
            l += 2
            total -= 1
        return pix

    def eleven(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            # print(mse)
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1 and x_offset == 256:
                    y_offset = 255
                x_offset = 0
            l += 2
            total -= 1
        return pix

    def twelve(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            # print(mse)
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1 and x_offset == 256:
                    y_offset = 255
                x_offset = 0
            l += 2
            total -= 1
        return pix

    def thirteen(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            # print(mse)
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1 and x_offset == 256:
                    y_offset = 255
                x_offset = 0
            l += 2
            total -= 1
        return pix

    def fourteen(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            # print(mse)
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1 and x_offset == 256:
                    y_offset = 255
                x_offset = 0
            l += 2
            total -= 1
        return pix

    def fifteen(l, x_offset, y_offset, val, prev):
        nonlocal mse
        total = 256 * 256
        while (total != 0):
            val = 2 * int((secret[l])) + int((secret[l + 1]))
            prev = pix[x_offset][y_offset]
            pix[x_offset][y_offset] = pix[x_offset][y_offset] - (pix[x_offset][y_offset] % 4) + int(val)
            mse += ((prev - pix[x_offset][y_offset]) ** 2)
            # print(mse)
            x_offset += 1
            if x_offset == 256:
                y_offset -= 1
                if y_offset == -1 and x_offset == 256:
                    y_offset = 255
                x_offset = 0
            l += 2
            total -= 1
        return pix

    switcher = {
        0: zero,
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve,
        13: thirteen,
        14: fourteen,
        15: fifteen
    }

    def raster_order(dir_input):
        func = switcher[dir_input](l, x_offset, y_offset, val, prev)
        return func

    # taking the input for direction
    dir_input = direction
    # calculating psnr
    pix = raster_order(dir_input)
    # array = np.array(pix, dtype=np.uint8)
    # new_image = Image.fromarray(array)
    # new_image.save("stego.png")
    # print(mse)
    mse = mse / (256 * 256)
    if(mse):
        # nonlocal psnr
        psnr = 10 * math.log10((255 * 255) / mse)
        return  psnr, pix
    # else:
        # print(dir_input, x_offset, y_offset)

    # print("Psnr of stego:", psnr)
    return  0, pix

