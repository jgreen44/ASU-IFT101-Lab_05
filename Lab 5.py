#   Filename:           Lab 5
#   Created by:         jasongreen
#   Date:               Monday, February 04, 2019
#   Time of Creation:   11:33
#   ---

# 4. A shop is having a five-day sale. Each day, starting on Monday,
# the price will drop by 10% of the previous day’s price. For example,
# if the original price of a product is $20, then the sale price on
# Monday would be $18 (that’s 10% less than the original price),
# and on Tuesday it would be $16.2 (that’s 10% less than Monday’s
# price), and so on. Develop a solution that will calculate the price
# of an item for each of the five days, given the original price.
# Test the solution for an item costing $10.

product = 10
product_reduction = 0


for i in range(0, 7):
    product_reduction = product * 0.1
    update_prod_price = product - product_reduction
    product = update_prod_price
    if i == 0:
        print("On Monday, the price is ${:.2f}".format(update_prod_price))
    if i == 1:
        print("On Tuesday, the price is ${:.2f}".format(update_prod_price))
    if i == 2:
        print("On Wednesday, the price is ${:.2f}".format(update_prod_price))
    if i == 3:
        print("On Thursday, the price is ${:.2f}".format(update_prod_price))
    if i == 4:
        print("On Friday, the price is ${:.2f}".format(update_prod_price))
    if i == 5:
        print("On Saturday, the price is ${:.2f}".format(update_prod_price))
    if i == 6:
        print("On Sunday, the price is ${:.2f}".format(update_prod_price))

# 5. Develop a solution to flip a coin a given amount of times,
# and then print the number of heads and the number of tails.
# The equation to toss the coin is:
# Coin = Integer(Random * 2) + 1
# This is called a simulation question where you use a math
# function to represent mathematically what you might observe
# physically, by actually flipping a coin.


import random

record_flips = []
number_of_flips = int(input("How many times do you want to flip a coin? "))

for i in range(number_of_flips):
    flip = random.randint(0, 1)
    if flip == 0:
        record_flips.append("heads")
    else:
        record_flips.append("tails")
print("You flipped " + str(record_flips.count("heads")) +
      " heads and " + str(record_flips.count("tails")) + " tails!")


# Write a Python function to print the multiplication table (from 1 to 10)
# of a number. Your function takes a number as an input, and it prints its
# multiplication table.

def multiplication(number):
    for i in range(1, 11):
        new_number = number * i
        print("{} times {} is {}".format(number, i, new_number))


number = int(input("Choose a number to be multiplied sequentially up to 10: "))
multiplication(number)


# Write a Python program that prints the multiplication
# table (form 1 to 10) for all the numbers between 1 and
# 20. You can use the function that you wrote in P3 above.

for i in range(1, 21):
    for j in range(1, 11):
        print("{} times {} is {}".format(i, j, i*j))


for i in range(4,11):
        print("{} times {} is {}".format(1, i, i))




# Write a Python program that, given an array of integers,
# it counts and prints the number of 1's in the array.


first_array = [9, 1, 1, 3, 1]
x = 0

for i in first_array:
    if i == 1:
        x += 1
if x > 1:
    print("There are {} ones in your array!".format(x))
else:
    print("There is only 1 one found in your array!")
