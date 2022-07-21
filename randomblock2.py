import random
i = 0
while i < 30:
    block = random.randint(1,5)

    if block == 1:
        print(block, "Diorite")
    elif block == 2:
        print(block, "Granite")
    elif block == 3:
        print(block, "Andersite")
    elif block == 4:
        print(block, "Deepslate")
    elif block == 5:
        print(block, "Tuff")

    i += 1







#partially initialized module 'random' has no attribute 'randrange' (most likely due to a circular import),
    #file name was random.py which was breaking the function, renamed to randomblock.py
