numbers=[2,3,5,6,7,43,54,789,2]
print("Original list:", numbers)
print(numbers.pop(3))
numbers.insert(3,99)
print(numbers)
print(numbers.index(7))
print(2 in numbers) 
print(numbers.count(2))
numbers.reverse()
print(numbers)
numbers.append(121212)
numbers.sort()
print(numbers)
#wrong code to remove duplicates
# i=0
# while i<=len(numbers):
#     if numbers.index(i)==numbers.index(i+1):
#         llist=numbers.pop(i)
#         print(llist)
#     else:
#         print('no dupes')
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)

