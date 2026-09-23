
#Name:Anthony Martinez
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("hello people")
#3. Create three different variables that each randomly generate an integer between 1 and 10
tony=random.randint(1,10)
ony=random.randint(1,10)
ny=random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(tony,ony,ny)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
tonyand2 = tony+2
onyminus4 = ony-4
nymultipled=ny * 1.5
#6. Print each result from #5 on the same line.
print(tonyand2,onyminus4,nymultipled)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
pizzabell= [random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)]
#8. Sort the list in #7 and print it.
pizzabell.sort()
print(pizzabell)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(pizzabell[1] + pizzabell[2]+pizzabell[2])
#10. Create a list with 5 names of other students in this class and print the list.
listnames= ["santi","wyatt","oliver","jake","adrian"]
print(listnames)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(listnames)
print(listnames)
#12. Print a random choice from the list of names from #10.
print (random.choice(listnames))