def selectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]

arr = []

n = int(input("Enter size of the array: "))
for i in range(n):
    ele = int(input(f'Enter array values: '))
    arr.append(ele)

print("\nUnsorted array: ")
for num in arr:
    print(num, end=" ")

selectionSort(arr)

print("\nSorted array: ")
for num in arr:
    print(num, end=" ")