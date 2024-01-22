#Exercise 9: Check Palindrome Number
#Write a program to check if the given number is a palindrome number.
#A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers


number = 12321

first_digit = (number % 10) * (10000)
second_digit = (number % 100) // 10 * 1000
third_digit = (number % 1000) // 100 * 100
fourth_digit = (number % 10000) // 1000 * 10
fifth_digit = (number % 100000) // 10000
new_number = first_digit+second_digit+third_digit+fourth_digit+fifth_digit

if number == new_number:
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")