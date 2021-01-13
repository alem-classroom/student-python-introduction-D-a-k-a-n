def insert_squares(arr, num):
    i = 1
    while i <= num:
        arr.append(i**2)
        i += 1

    return arr

arrey = insert_squares([1,2,3], 5)
print(arrey)
