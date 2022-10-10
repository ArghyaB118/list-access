import math

x = [x for x in range(1,38)]
double_box = sum(x) / 37
print(double_box)

ml_box = 0
for i in x:
    if i <= 3:
        cr = i
    elif i > 3 and i <= 15:
        cr = (2 / 37) + (6 / 37) + ((i - 1 + 1) * i / 37) + ((1 - (i + 1) / 37) * i)
    elif i > 15:
        cr = (2 / 37) + (6 / 37) + (20 / 37) + ((i - 1 + 1) * i / 37) + ((1 - (i + 2) / 37) * i)
    print(cr)
    ml_box = ml_box + cr / 37
print(ml_box)