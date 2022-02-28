def conversion_8bit(pix):
    temp = []
    for i in range(128):
        for j in range(128):

            while (len(str((pix[i][j]))) != 8):
                pix[i][j] = "0" + str(pix[i][j])
            temp += pix[i][j]
    return temp



