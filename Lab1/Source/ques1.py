def subset(arr, n):
    _list = []

    for i in range(2 ** n):
        subset = ""
        # consider each element in the set
        for j in range(n):
            if (i & (1 << j)) != 0:
                subset += str(arr[j]) + "|"
        # if subset is encountered for the first time
        if subset not in _list and len(subset) > 0:
            _list.append(subset)
            # consider every subset
    for subset in _list:
        # split the subset and print its elements
        arr = subset.split('|')
        for string in arr:
            print(string, end=" ")
        print()

if __name__ == '__main__':
    arr = [1, 2, 2]
    n = len(arr)
    subset(arr, n)
