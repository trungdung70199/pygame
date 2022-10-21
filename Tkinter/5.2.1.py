list = [70, 15, 66, 21, 19, 97, 33, 44, 30, 2]

for j in range(len(list) - 1):
    if list[j] > list[j+1]:
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp
    print(list)
    