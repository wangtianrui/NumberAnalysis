def split_into_2(array):
    length = len(array)
    result = []
    flag = False
    if length % 2 != 0:
        last_array = [array.pop()]
        flag = True
    i = 0
    while i < length - 1:
        if array[i] < array[i + 1]:
            result.append([array[i], array[i + 1]])
        else:
            result.append([array[i + 1], array[i]])
        i += 2
    if flag:
        result.append(last_array)
    return result


def merge_sort(array1, array2):
    index1, index2 = 0, 0
    result_array = []
    length1, length2 = len(array1), len(array2)

    while index1 + index2 <= length1 + length2 - 1:
        # num1, num2 = array1[index1], array2[index2]
        if index1 == length1 and index2 < length2:
            result_array.append(array2[index2])
            index2 += 1
        elif index2 == length2 and index1 < length1:
            result_array.append(array1[index1])
            index1 += 1
        else:
            # print(index1, index2)
            if array1[index1] < array2[index2]:
                result_array.append(array1[index1])
                index1 += 1
            else:
                result_array.append(array2[index2])
                index2 += 1
    return result_array


def sort(array):
    split_array = split_into_2(array)
    print(split_array)
    while len(split_array) > 1:
        temp_array = []
        for i in range(0, len(split_array) - 1, 2):
            temp_array.append(merge_sort(split_array[i], split_array[i + 1]))
        if len(split_array) % 2 != 0:
            temp_array.append(split_array[-1])
        split_array = temp_array
        print(split_array)


if __name__ == "__main__":
    array = [1, 5, 21, 2, 3, 6, 17, 4, 9, 542, 123, 6]
    sort(array)
