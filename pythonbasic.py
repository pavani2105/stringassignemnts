# Even or Odd Checker  
num = int(input("Enter an integer: "))  
if num % 2 == 0:  
    print("Even")  
else:  
    print("Odd")  

# Find the Largest Number  
a = int(input("Enter the first number: "))  
b = int(input("Enter the second number: "))  
c = int(input("Enter the third number: "))  
if a >= b and a >= c:  
    print(f"The largest number is {a}")  
elif b >= a and b >= c:  
    print(f"The largest number is {b}")  
else:  
    print(f"The largest number is {c}")  

# Number Classification  
num = int(input("Enter a number: "))  
if num > 0:  
    print("Positive")  
elif num < 0:  
    print("Negative")  
else:  
    print("Zero")  

# Sum of Numbers in a Range  
start = int(input("Enter the start number: "))  
end = int(input("Enter the end number: "))  
sum_numbers = 0  
for i in range(start, end + 1):  
    sum_numbers += i  
print(f"The sum of numbers from {start} to {end} is {sum_numbers}")  

# Printing a Multiplication Table  
num = int(input("Enter a number to print its multiplication table: "))  
for i in range(1, 11):  
    print(f"{num} x {i} = {num * i}")  

# Counting Vowels in a String  
string_input = input("Enter a string: ")  
vowel_count = 0  
for char in string_input.lower():  
    if char in 'aeiou':  
        vowel_count += 1  
print(f"The number of vowels in the string is {vowel_count}")  

# Factorial Calculator  
n = int(input("Enter a positive integer: "))  
if n < 0:  
    print("Factorial is not defined for negative numbers.")  
else:  
    factorial = 1  
    for i in range(1, n + 1):  
        factorial *= i  
    print(f"The factorial of {n} is {factorial}")  

# FizzBuzz Game  
for i in range(1, 51):  
    if i % 3 == 0 and i % 5 == 0:  
        print("FizzBuzz")  
    elif i % 3 == 0:  
        print("Fizz")  
    elif i % 5 == 0:  
        print("Buzz")  
    else:  
        print(i)  
