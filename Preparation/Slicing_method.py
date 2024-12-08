

my_list = [64, 34, 25, 12, 22,12, 11, 90]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


bubble_sort(my_list)
print("Without inbuield Sorted list is:", my_list)


my_list.sort()
print("Using inbuield function(srot())",my_list)

print(sorted(my_list))




