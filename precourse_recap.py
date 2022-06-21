house = "apartment"
car = "4x4"
sallary = 1000
bills = 500
saves = 0

properties = " I have one house" + " and one " + car
print(properties)
saves = sallary - bills
economy = " My savings are " + "£" + str (saves)
print(economy)

house_capitalized = house.capitalize
expression = "This is how you write house in a capitalized way : " 
print (expression)
print (house_capitalized)
print ("Why does not print House?")
bit_count = saves.bit_count
print(bit_count) # It is not going to print what I expect : the number of bits
# So how to print it properly?


