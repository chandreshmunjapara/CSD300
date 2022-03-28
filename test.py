def zero():
    mse = 0
    val = 0
    l = 0
    x_offset = 0
    y_offset = 0
    prev = 0
    total = 256 * 256
    while total != 0:
        val = 2 * int((secret[l])) + int((secret[l + 1]))
        # prev = host[x_offset][y_offset]
        # host[x_offset][y_offset] = host[x_offset][y_offset] - (host[x_offset][y_offset] % 4) + int(val)
        # mse += ((prev - host[x_offset][y_offset]) ** 2)
        y_offset += 1
        if y_offset == 256:
            x_offset -= 1
            if x_offset == -1 and y_offset == 256:
                x_offset = 255
            y_offset = 0
        l += 2
        total -= 1
    return host, mse

# zer()

a = [0, 1, 0]
def getValue(arr) :
    res = int("".join(str(x) for x in arr), 2)
    print((res))
    return res

getValue(a)