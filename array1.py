# 1. len() - Get the length of an array
arr = [1, 2, 3, 4, 5]
print(len(arr))  

# 2. append(x) - Add an element to the end
arr.append(6)
print(arr)  

# 3. insert(pos, x) - Insert an element at a specific position
arr.insert(2, 10)
print(arr)  

# 4. remove(x) - Remove the first occurrence of a value
arr.remove(10)
print(arr)  

# 5. pop() - Remove and return the last element
last = arr.pop()
print(last)  
print(arr)  

# 6. index(x) - Get the index of the first occurrence of a value
idx = arr.index(3)
print(idx)  

# 7. count(x) - Count occurrences of a value
arr.append(3)
count = arr.count(3)
print(count)  

# 8. reverse() - Reverse the array in place
arr.reverse()
print(arr)