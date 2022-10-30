print("\n***Welcome to Prime and Non-Prime Lists***\n")
#Ask the user to enter any number of integers (a comma-separated list of whole numbers).
#Save the numbers provided into a List (hint: use the string split() method for this part).
List = [int(num) for num in input("Enter any number of integers\n").split(',')]
Prime_List = [] #create a list to store prime numbers
Non_Prime_List = [] #create a list to store non-prime numbers

#For each of the numbers from the list determine if it is prime or non-prime, and place it either
#into an 'prime numbers' list or non-prime numbers list (hint: use a loop for this part)
for number in List: #Iterate over the list
    count = 0 #declare a variable to count 
    for j in range(1,number):  #Iterate from 1 to given number
        if number%j ==0: #If number is divisible by other than 1 and itself
            count +=1  #increase the count by 1
    
    if count == 1:  #if count is 1, means there is no divisible
        Prime_List.append(number) #add that number to Prime_List
    else: #if count is not 1, means there is  divisible
        Non_Prime_List.append(number)  #add that number to Non_Prime_List
               

print("\nThe prime numbers are:")
print(*Prime_List, sep = ", ") #print the Prime_List numbers by comma-separated
print("\n\n") #for space
print("The non-prime numbers are:")
print(*Non_Prime_List, sep = ", ")