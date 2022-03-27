import cv2
from copy import copy,deepcopy
import helper as h
import diretion_gene as d
import random


# getting host image
img = cv2.imread("hostim.jpg", 0)

# getting secret image
sec_img=cv2.imread("secret2.png",0)
y_=deepcopy(img)
x_=deepcopy(sec_img)

# converting to pixels
host=y_.tolist()
pix_secret=x_.tolist()

# converting decimal to binary
for i in range(len(pix_secret)):
    for j in range(len(pix_secret)):
        pix_secret[i][j]=bin(pix_secret[i][j]).replace("0b", "")

# converting to 8-bit pixels 
secret=[]
secret+=h.conversion_8bit(pix_secret)

# getting the psnr of stego image
# print(d.return_psnr(pix,temp3))

#initialize population
best=-100000
best_stego1 = []
best_stego2 = {}
populations =([[random.randint(0,1) for x in range(22)] for i in range(300)])
# print(type(populations))
parents=[]
new_populations = []
# print(populations)


# fitness score calculation ............
def fitness_score():
    global populations, best, best_stego1, best_stego2
    fit_value = []
    fit_score = []
    all_stego = []
    for i in range(300):
        # chromosome_value = 0
        # for j in range(21, 0, -1):
        #     chromosome_value += populations[i][j]*(2 * (21 - j))
        #         chromosome_value = -1*chromosome_value if populations[i][0]==1 else chromosome_value
        # print(chromosome_value)
        # getGene(populations[i])
        # fit_value.append(d.return_psnr(host,secret, populations[i]))
        f, stego = d.return_psnr(host,secret, populations[i])
        fit_value.append(f)
        all_stego.append(list(stego))
        best_stego2[f] = stego
    # print(fit_value)
    fit_value, populations, all_stego = zip(*sorted(zip(fit_value, populations, all_stego) , reverse = True))
    best= fit_value[0]
    best_stego1 = all_stego[0]


# fitness_score()
# print(len(all_stego), type(best_stego1))


def selectparent():
    global parents
    #global populations , parents

    parents=populations[0:150]
    # print(type(parents))
    # print("Parents ", len(parents))
# selectparent()


def crossover():
    global parents

    cross_point = random.randint(0, 21)
    # print("cross ", cross_point)
    # parents = parents + tuple([(parents[0][0:cross_point + 1] + parents[1][cross_point + 1:22])])
    offsprings = []
    for j in range (75):
        if(j%2 == 0):
            offspring1 = (parents[j][0:cross_point + 1] + parents[j+1][cross_point + 1:22])
            for i in range (6):
                offspring1[i+16] = random.randint(0, 1)
            # print(type(offspring1))
            # parents = parents + tuple([offspring1])

            offspring2 = (parents[j+1][0:cross_point + 1] + parents[j][cross_point + 1:22])
            for i in range(6):
                offspring2[i + 16] = random.randint(0, 1)
        offsprings.append(offspring1)
        offsprings.append(offspring2)


    offsprings=tuple(offsprings)
    # print(len(offsprings),len(parents),len(offspring1))
    parents = parents + offsprings

    # print(len(parents))


# crossover()
#
def mutation() :
    global populations, parents
    mute = random.randint(0,100)
    if mute == 4 :
        x=random.randint(0,299)
        y = random.randint(0,21)
        parents[x][y] = 1-parents[x][y]
    populations = parents
    # print(populations)
# mutation()
#
# # [1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0]
#
for i in range(10) :
    fitness_score()
    selectparent()
    crossover()
    mutation()
print("best score :")
print(best)
print("sequence........")
print(populations[0])
print("stego.........")
# print(best_stego1)
# print(".....................")
# print(best_stego2[best])
# if best_stego2[best] != best_stego1:
#     print(type(best_stego2[best]), type(best_stego1))

# Extraction



