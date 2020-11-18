from random import randint

list = []
for i in range(7):
    list.append(randint(-256, 256))


def min(list):
    if len(list) == 2:
        return list[0] if list[0] < list[1] else list[1]
    else:
        sub_min = min(list[1:])
        return list[0] if list[0] < sub_min else sub_min

    print(sub_min)

print(min(list))

