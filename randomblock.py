import random
i = 0
while i < 15:
    block = random.choice(["Tuff", "Andersite", "Granite", "deepslate"])
    num1 = random.randint(0,9)

    print(num1, block)
    i += 1







#partially initialized module 'random' has no attribute 'randrange' (most likely due to a circular import),
    #file name was random.py which was breaking the function, renamed to randomblock.py
