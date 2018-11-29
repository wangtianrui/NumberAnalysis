def quick_sort(array, star, end):
    if star < end:
        i, j = star, end
        base = array[i]
        while i < j:
            while i < j and array[j] >= base:
                j -= 1
            array[i] = array[j]
            while i < j and array[i] <= base:
                i += 1
            array[j] = array[i]
        array[i] = base
        quick_sort(array, star, i - 1)
        quick_sort(array, j + 1, end)
    print(array)



if __name__ == "__main__":
    array = [1, 6, 8, 3, 5, 0, 32, 12, 31, 2, 14]
    quick_sort(array, 0, len(array) - 1)
