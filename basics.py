list_of_numbers = []
number = 0

#ask user for input, if input =  -1, stop code
while number != -1:
    number = int(input("Geef een number "))
    list_of_numbers.append(number)

#remove duplicates from list by making dictionary
list_of_numbers = list( dict.fromkeys(list_of_numbers))

#give second highest number
list_of_numbers.sort()
print(list_of_numbers[-2])

#print the list
print(list_of_numbers)