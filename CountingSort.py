#Internet source / insperation: https://www.programiz.com/dsa/counting-sort

#To sort a[left...right] into ascending order:
#1. If left < right:
#1.1. Partition a[left...right] such that
#a[left...p–1] are all less than or equal to a[p], and
#a[p+1...right] are all greater than or equal to a[p].
#1.2. Sort a[left...p–1] into ascending order.
#1.3. Sort a[p+1...right] into ascending order.
#2. Terminate.

# Test Vars: a = [4,3,4,5,2,3,4,6,8,9,10]  # O(1)

# Test Vars: 
# Test Vars:a = ["fox", "cow", "pig", "cat", "rat", "lion", "tiger", "goat", "dog"]  # O(1)
a = [23, 56, 7, 44, 768, 90, 107, 22, 45, 66, 99, 1, 12, 50, 87, 43, 19, 32, 88, 5]  # O(1)

arr = a  # O(1)

#Counting Sort
def CountingSort(Data):

    UnsortedArray = Data  # O(1)
    FinalArray = [0] * len(UnsortedArray)  # Initialize FinalArray with zeros # O(n)
    NumberOfComparisons = 0 # O(1)

    # Find the maximum and minimum elements in the array
    max_element = max(UnsortedArray)  # O(n)
    min_element = min(UnsortedArray)  # O(n)

    # Adjust the range to include negative numbers
    range_of_numbers = max_element - min_element + 1  # O(1)

    # Initialize count array with zeros
    count = [0] * range_of_numbers  # O(n)

    # Count occurrences of each element
    for num in UnsortedArray:  # O(n)
        count[num - min_element] += 1  # O(1)

    # Update count array to contain actual positions of elements
    for i in range(1, len(count)):  # O(n)
        count[i] += count[i - 1]  # O(1)

    # Place elements in the sorted array
    for num in reversed(UnsortedArray):  # O(n)
        FinalArray[count[num - min_element] - 1] = num  # O(1)
        count[num - min_element] -= 1  # O(1)
        NumberOfComparisons += 1 # O(1)

    return FinalArray, NumberOfComparisons

print(CountingSort(arr))  # O(n*log(n))