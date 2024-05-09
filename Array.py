from array import *
arr = array('i', [1, 2, 3, 4, 5])
print(arr)

arr1 =array('d',[1.4,2.4, 3.5, 4.6, 5.0])
print(arr1)


#add a element to last element
arr.append(12)
print(arr)

#add a element to any where
arr.insert(0, 122)
print(arr)

#add many element to array

arr.extend([1,2,3,4,5])
print(arr)

#Traversal Operations
for i in arr:
    print(i)
    
#Access array elements
print(arr[2])

#Delete array elements
arr.remove(arr[0])
print(arr)

#Delete last element of the array
arr.pop()
print(arr)
    
    
