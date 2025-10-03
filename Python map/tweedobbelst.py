import random

# dobbelstl = random.randint(1,6)
# doubbelst2 = random.randint(1,6)
# worp = dobbelstl + doubbelst2
# print(worp)

#worp = random.randint(2,12)

# doubbelst1 = random.randint()
# doubbelst2 = random.randint()
# worp = doubbelst1 + doubbelst2


teller = 0
worp = 0
while(worp != 7):
    doubbelst1 = random.randint(1,6)
    doubbelst2 = random.randint(1,6)
    word = doubbelst1 + doubbelst2
    teller += 1
print(str(worp) + "poging" + str(teller))


