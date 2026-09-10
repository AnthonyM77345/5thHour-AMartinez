#Name:Anthony Martinez
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
list1 = [1,2,3,4,5,6,7,8,9,]
#2. Sort the list from highest to lowest.
list1.sort(reverse=True)
print(list1)
 #3. Create an empty list.
list2= []
#4. Remove the median number from the first list and add it to the second list.
list1.pop (4)
list2.insert(0,5)
#5. Remove the first number from the first list and add it to the second list.
list1.pop(0)
list2.insert(0,9)
#6. Print both lists.
print(list1)
print(list2)
#7. Add the two numbers in the second list together and print the result.
list3=list2[0]+list2[1]
print(list3)
