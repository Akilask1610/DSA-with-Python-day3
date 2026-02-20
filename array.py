# to print largest number in array
arr = [10, 5, 20, 8, 15]

largest = 0

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]
print("largest number is:", largest)


# count even numbers
# return how many even numbers are present in the array
# input:arr = [1,2,3,4,6]
# output:3


arr = [1,2,3,4,6]
count=0
for i in arr:
    if i%2==0:
        count=count+1
print(count)

#Count positive numbers
#Return how many positive numbers (>0) are in the array.
arr = [-2,5,-1,3,0]
output:2
arr = [-2,5,-1,3,0]
count=0
for i in arr:
    if i>0:
        count=count+1
print(count)


#Count negative numbers
#Return how many negative numbers (<0) are in the array.
arr = [-2, 5, -1, 3, 0]
count=0
for i in range(len(arr)):
    if arr[i] < 0:
        count += 1
print("count of negative numbers is:", count)

#Print array in reverse order
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')


# Linear search 
# given an array and a target value, print "Found" if the value exists, otherwise print "Not Found"
# Inputarr = [5,8,3,9]
# target = 3
# output: Found

arr = [5,8,3,9]
target = 3
found = False
for i in arr:
    if i==target:
        found = True
        break 
if found:
    print("found")
else:
    print("not found")

#second largest element in an array
arr = [10, 5, 20, 8, 15]

largest = 0
second_largest = 0
for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
print("second largest number is:", second_largest)



#remove element from the given array
#arr = [1,2,2,3,1,4,3]
#remove 2

arr = [1,2,2,3,1,4,3]
element_to_remove = 2
new_arr = []
for i in range(len(arr)):
    if arr[i] != element_to_remove:
        new_arr.append(arr[i])
print("array after removing element:", new_arr)


#sum of elements at even indexes
arr = [1, 2, 3, 4, 5]
sum_even_index = 0
for i in range(len(arr)):
    if i % 2 == 0:
        sum_even_index += arr[i]
print("sum of elements at even indexes is:", sum_even_index)

#swipe first and last element in an array

arr = [1, 2, 3, 4, 5]
temp = arr[0]
arr[0] = arr[len(arr)-1]
arr[len(arr)-1] = temp
print("array after swapping first and last element:", arr)

# 1. move all zeros to the end (keep order)
# input: [0,1,0,3,12]
# output: [1,3,12,0,0]
# 1.move all zeros to the end
# 2.Keep the order of non-zero numbers
# 3.create a new list

arr=[0, 1, 0, 3, 12]
temp=0
new_arr=[]
for i in arr:
    if i==0:
        temp+=1
    else:
        new_arr.append(i)
for i in range(temp):
    new_arr.append(0)
print(new_arr)


#check if array is sorted
#arr = [1, 2, 3, 4, 5]
#output: False
arr = [1, 2, 3, 5, 4]
is_sorted = True
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break
if is_sorted:
    print("array is sorted")
else:
    print("array is not sorted")