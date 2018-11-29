def bisearch(array, star, end, target):
    index_mid = (int)((star + end) / 2)
    print(array[star:end])
    if array[index_mid] < target:
        bisearch(array, index_mid, end, target)

    elif array[index_mid] > target:
        bisearch(array, star, index_mid, target)
    else:
        print(target, "的位置是", index_mid)


if __name__ == "__main__":
    # print("hello")
    array = [1, 4, 6, 2, 0, 23, 543, 12, 9, 21, 11, 28]
    target = 11
    array = sorted(array)
    bisearch(array, 0, len(array) - 1, target)

