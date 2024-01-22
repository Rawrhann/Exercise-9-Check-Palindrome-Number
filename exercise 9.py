#Exercise 9: Check Palindrome Number
#Write a program to check if the given number is a palindrome number.
#A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

def palindrome(number):
    original_number = number
     
    new_number = 0
    while number > 0:
        reminder = number % 10
        new_number = (new_number * 10) + reminder
        number = number // 10

    if original_number == new_number:
        print("the number", original_number, "is a palindrome")
    else:
        print("the number", original_number, "is not a palindrome")

palindrome(12345)
palindrome(1234321)