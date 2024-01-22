#Exercise 9: Check Palindrome Number
#Write a program to check if the given number is a palindrome number.
#A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

def palindrome(number):
    original_number = number
     

    first_digit = (number % 10) * (10000)
    second_digit = (number % 100) // 10 * 1000
    third_digit = (number % 1000) // 100 * 100
    fourth_digit = (number % 10000) // 1000 * 10
    fifth_digit = (number % 100000) // 10000
    new_number = first_digit+second_digit+third_digit+fourth_digit+fifth_digit  


    if original_number == new_number:
        print("the number", original_number, "is a palindrome")
    else:
        print("the number", original_number, "is not a palindrome")

palindrome(12345)
palindrome(12321)