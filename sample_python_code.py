#  Python → Introduction to Python → Introduction to Python 
print("Learn Python to be great!")

# Python → Introduction to Python → Overview of the basic program 
'''
Code Challenge — Write a program

Write a program that prints the string "My name is " followed by your name like in the output example. All words in this string must be separated by a single space.

Output example

My name is John
'''
print("My name is John")


'''

The title of Alice's Adventures in Wonderland is often shortened to Alice in Wonderland.

Now, when we know how to print strings with quotes, we won't shorten it. Please print the full book title.
'''
print("Alice's Adventures in Wonderland ")

'''

Write a program that prints the following line.

2 + 2 = 4
'''
print("2 + 2 = 4")

'''

Write a program that prints out a string We learn Python!

Note that this task is case-sensitive.
'''
print("We learn Python!")

#  Python → Introduction to Python → Multi-line programs 

'''
Write a program that prints the following three text lines in the column.

first
second
third
'''
print("first")
print("second")
print("third")

'''

You need to write a program to display the result grid of a game in Tic-Tac-Toe.

The grid is shown below.

O X X
O X O
X O X

Note: O is not a zero, it is a letter. The letters X and O should be uppercase.
'''
print("O X X")
print("O X O")
print("X O X")

'''

Write a program that prints this square out of * symbols.

* * * *
*     *
*     *
* * * *

Don't forget about whitespaces!
'''
print("* * * *")
print("*     *")
print("*     *")
print("* * * *")

'''

Write a program that prints the following text:

WE NEED
 
TO LEARN PYTHON
 
AS QUICKLY AS POSSIBLE
'''
print("WE NEED")
print("")
print("TO LEARN PYTHON")
print("")
print("AS QUICKLY AS POSSIBLE")

# Python → Code style → PEP 8

# Python → Code style → Comments
'''

There are several comments "hidden" in the code below. Find them and make sure to comment them so that the code runs correctly.
'''
# create a variable x
# with the value 8
x = 8
x = x * x
print(x)  # prints the x squared

'''
Given a line of code and comment, please combine them and write them down as they would look like in a real program. Please make a comment an inline one.

Code: word = word.replace("\u0301", "")

Comment: delete stress symbols from the word
'''
word = word.replace("\u0301", "")  # delete stress symbols from the word


'''

It is sometimes useful to comment out some parts of a program if you don't need them now and want to save them for later. Look at the following code, copy it to the test and decide what line to comment out so that the code will print an integer 7.

print(1 + 2 + 3 + 6)
print(1 + 3 + 3)
print(1 + 2 + 3)
'''
# print(1 + 2 + 3 + 6)
print(1 + 3 + 3)
# print(1 + 2 + 3)

'''

Write the code that corresponds to the comment.
'''
# prints "ok"
print("ok")

#  Python → Data types and operations → Basic data types 

'''

Print an int with a value 10.

Sample Input 1:

Sample Output 1:

10
'''
print(10)

'''

Print the numbers from 1 to 10 in a single line: 1 2 3 4 5 6 7 8 9 10.
'''
print("1 2 3 4 5 6 7 8 9 10")

'''

Write the code that prints the type of 3 objects that are written below (in this exact order).

"int"
394
2.71
'''
print(type("int"))
print(type(394))
print(type(2.71))

'''

Try to print a float number 1.0000000000000001.
'''
print(1.0000000000000001)

'''

Print a string Supercalifragilisticexpialidocious below.
'''
print("Supercalifragilisticexpialidocious")

#  Python → Data types and operations → Variables 

'''

Define a numeric variable with name number and value 10.
'''
number = 10

'''

Create a variable favorite_holiday with a value "Cinnamon Roll Day"
'''
favorite_holiday = "Cinnamon Roll Day"

#  Python → Simple programs → Taking input 

'''

Let's see how it works. Copy the following code and paste it below. Then change one of the lines so that the program would print any data the user inputs without performing any operations on them. 

data = ...
print(data)

Sample Input 1:

10

Sample Output 1:

10
'''
# put your python code here
data = input()
print(data)

'''

Write a program that prints the sum of three integer numbers. Read each number from the user separately.

Sample Input 1:

3
6
8

Sample Output 1:

17
'''
# put your python code here
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 + num2 + num3)

'''

Imagine you are writing a program that will give a prediction for users. And imagine you intend to do so based on a number they enter. Write a program that reads a three-digit number and prints the sum of its digits.

Input: positive integer

Output: positive integer

Sample Input 1:

672

Sample Output 1:

15
'''
# put your code here
number = input()
print(int(number[0]) + int(number[1]) + int(number[2]))

'''

Ask the user about parameters of a rectangular parallelepiped (3 integers representing the length, width and height) and print the sum of edge lengths, its total surface area and volume.

Sum of lengths of all edges:

s=4(a+b+c)s = 4(a + b + c)s=4(a+b+c)

Surface area:

S=2(ab+bc+ac)S = 2(ab + bc + ac)S=2(ab+bc+ac)

Volume:

V=abcV = abcV=abc

Sample Input 1:

5
10
15

Sample Output 1:

120
550
750

'''
# put your python code here
length = int(input())
width = int(input())
height = int(input())

print(4 * (length + width + height))
print(2 * (length * width + width * height + length * height))
print(length * width * height)

'''

Write a program that reads the input from the user and then prints "Hello, " + user input. Don't print any additional messages!

Sample Input 1:

Sauron

Sample Output 1:

Hello, Sauron
'''
name = input()
print("Hello, " + name)

'''

Write a program that reads two integer numbers from user and then prints their difference.

Sample Input 1:

8
11

Sample Output 1:

-3
'''
num1 = int(input())
num2 = int(input())
print(num1 - num2)

'''

Write a program that reads two float numbers from the user (use the float()) and prints their sum.

Sample Input 1:

8.77
11.25

Sample Output 1:

20.02
'''
num1 = float(input())
num2 = float(input())
print(num1 + num2)

'''

Have you ever dreamed of becoming a songwriter? It's time to make a hit. We will leave a verse for later and write the chorus part instead.

All you need to do is to read the input number n and an input word (they are given on separate lines) and to repeat this word exactly n times.

Finally, print your song for us, please!

Sample Input 1:

7
la

Sample Output 1:

lalalalalalala
'''
print(int(input()) * input())

#  Python → Data types and operations → Integer arithmetic

'''

Write a program that calculates a remainder of 10 divided by 3 and prints the result
'''
# put your python code here
print(10 % 3)

'''

Please, print() the result of the following operations: first raise 31 into the power of 331; get the remainder of the result's division by 20.
'''
print((31 ** 331) % 20)

'''

Print the result of execution of the following expression 1234567890 multiplied by 987654321 then add 67890
'''
# put your python code here
print(1234567890 * 987654321 + 67890)

'''

Write a program that prints the product of these three numbers 1 * 2 * 3.
'''
print(1 * 2 * 3)

'''

Write a program that takes two integer numbers a and b and prints their sum.

The variables have already been defined.

Sample Input 1:

8
11

Sample Output 1:

19
'''
a = int(input())
b = int(input())

# calculate the sum below
print(a + b)

'''

Write a program that takes 3 integer numbers a, b and c, subtracts c from a multiplied by b and then prints the result.

There's no need to create the variables, just use them in the code below.

Sample Input 1:

8
11
63

Sample Output 1:

25
'''
# work with these variables
a = int(input())
b = int(input())
c = int(input())

print(a * b - c)

'''

Write a program that takes a single integer number n and then performs the following operations in the following order:

    adds n to itself
    multiplies the result by n
    subtracts n from the result
    exactly divides the result by n (that means, you need to carry out integer division).

Then print the result of the division. The example is given below:

    8 + 8 = 16
    16 * 8 = 128
    128 - 8 = 120
    120 // 8 = 15

The variable n is already defined.

Sample Input 1:

8

Sample Output 1:

15
'''

n = int(input())
print((((n + n) * n) - n) // n)

'''

It's time for really big numbers! Calculate this 2^{179} and print what you got.
'''
print(2 ** 179)

# 

# =============================================================================
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

# reading a name
name = input()
print('What a great name you have, ' + name + '!')
# =============================================================================

# Python → Code style → Naming variables

'''
Code Challenge — Write a program
Here's a list of variables:

n = 10
model_score = 0.9875
client_name = "Bob"
colorOfTheShirt = "red"
Some of them are named according to naming conventions and best practices, others are not.

Copy only those variables that have good names in your code. You don't need to use the print() function.
'''
# copy the correct variables here
model_score = 0.9875
client_name = "Bob"

'''
Code Challenge — Write a program
The previous developer accidentally overrode the str method and now the code fails.

Please fix the variable by adding "_" to the end of this name as it's said in the code style convention.
Your output should look like Hello10 and you don't need to use print. 
'''
str_ = "Hello"
str_ = str_ + str(10)

'''
Code Challenge — Write a program
Rename the variables into the code below according to the Python code style convention.

httpResponse = 'mocked response'
httpError = 404
'''
http_response = 'mocked response'
http_error = 404

# Python → Simple programs → Program with numbers

'''
Code Challenge — Write a program
Write a program that reads an integer value n from the standard input and prints the result of the expression:

((n + 1) * n + 2) * n + 3
Sample Input 1:

3
Sample Output 1:

45
'''
# put your python code here
n = int(input())
print(((n + 1) * n + 2) * n + 3)


'''
Code Challenge — Write a program
Lucky tickets are a kind of mathematical entertainment. A ticket is considered lucky if the sum of the first 3 digits coincides with the sum of the last 3 digits of the ticket number.
You are supposed to write a program that checks whether the two sums are equal. The code snippet below displays "Lucky" if they do and "Ordinary" otherwise.

However, some parts of the code are missing. Fill in the blanks to make it work!

Input: a string of 6 digits.

Output: either "Lucky" or "Ordinary" (without quotes).

Hint

Sample Input 1:

090234
Sample Output 1:

Lucky
Sample Input 2:

123456
Sample Output 2:

Ordinary
'''
# Save the input in this variable
ticket = int(input())

# Add up the digits for each half
half1 = ticket // 100000 + ticket // 10000 % 10 + ticket // 1000 % 10
half2 = ticket % 1000 // 100 + ticket % 100 // 10 + ticket % 10

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")

'''
Code Challenge — Write a program
Some school have decided to create three new math groups and equip classrooms for them with the new desks. Only two students may sit at any desk. The number of students in each of the three groups is known. Output the smallest amount of desks, which will need to be purchased. Each new group sits in its own classroom.

Input data format

The program receives the input of the three non-negative integers: the number of students in each of the three classes (the numbers do not exceed 1000).

Sample Input 1:

20
21
22
Sample Output 1:

32
Sample Input 2:

16
18
20
Sample Output 2:

27
'''
# put your python code here
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 % 2 + num1 // 2 + num2 % 2 + num2 // 2 + num3 % 2 + num3 // 2)

'''
Code Challenge — Write a program
Given a three-digit integer (i.e. an integer from 100 to 999). Find the sum of its digits.

Sample Input 1:

476
Sample Output 1:

17
'''
# put your python code here
num = int(input())
first_digit = num // 100
second_digit = num // 10 % 10 
third_digit = num % 10
print(first_digit + second_digit + third_digit)

'''
Code Challenge — Write a program
Write a program that reads an integer and outputs its last digit.

Sample Input 1:

425
Sample Output 1:

5
'''
# put your python code here
print(int(input()) % 10)

'''
Code Challenge — Write a program
Given a two-digit number. Output its first digit (i.e. the number of tens).

Sample Input 1:

42
Sample Output 1:

4
'''
# put your python code here
print(int(input()) // 10)

'''
Code Challenge — Write a program
N squirrels found K nuts and decided to divide them equally. Determine how many nuts each squirrel will get.

Input data format

There are two positive numbers N and K, each of them is not greater than 10000.

Sample Input 1:

3
14
Sample Output 1:

4
'''
# put your python code here
n_squirrels = int(input())
k_nuts = int(input())

print(k_nuts // n_squirrels)

'''
Code Challenge — Write a program
N squirrels found K nuts and decided to divide them equally. Find how many nuts will be left after each of the squirrels takes the equal amount of nuts.

Input data format

There are two positive integers N and K, each of them is not greater than 10000.

Sample Input 1:

3
14
Sample Output 1:

2
'''
# put your python code here
n_squirrels = int(input())
k_nuts = int(input())

print(k_nuts % n_squirrels)

'''
Code Challenge — Write a program
Calculate and print the income from a saving account with a 5% interest rate after a year for a given amount.

Sample Input 1:

None
Sample Output 1:

50.0
'''
amount = 1000
interest_rate = 5
years = 1

income = years * interest_rate / 100 * amount

print(income)

'''
Code Challenge — Write a program
You will get the values for two moments in time of the same day: hours, minutes and seconds for each time point. It is known that the first point of time happened earlier than the second one. Find out how many seconds passed between these two time instants.

Input data format

The program gets the input of three integers, hours, minutes, seconds, defining the first moment of time and three integers that define similarly the second moment.

Output data format

Output the number of seconds between these two moments of time.

Sample Input 1:

1
1
1
2
2
2
Sample Output 1:

3661
Sample Input 2:

1
2
30
1
3
20
Sample Output 2:

50
'''
# put your python code here
first_hour = int(input())
first_minute = int(input())
first_second = int(input())
second_hour = int(input())
second_minute = int(input())
second_second = int(input())

first = first_hour * 60 * 60 + first_minute * 60 + first_second
second = second_hour * 60 * 60 + second_minute * 60 + second_second

print(second - first)

'''
Code Challenge — Write a program
Write a program that will help people who are going on vacation. The program should calculate the total required sum (e.g. $) of money to have a good rest for a given duration.

There are four parameters which have to be considered:

duration in days
total food cost per a day
one-way flight cost
cost of one night in a hotel (the number of nights equal duration minus one)
Read values of these parameters from the standard input and then print the result.

Hint

Sample Input 1:

7
30
100
40
Sample Output 1:

650
'''
# put your python code here
duration = int(input())
daily_food_cost = int(input())
one_way_flight = int(input())
daily_hotel_rate = int(input())

print(duration 
        * daily_food_cost + 2 
        * one_way_flight 
        + (duration - 1) 
        * daily_hotel_rate)

# Python → Data types and operations → Membership testing

'''
Code Challenge — Write a program
Fill the value of the substring so that the membership test would result in True regardless of test_string value.

The variable for the test_string has already been defined.

Sample Input 1:

reMEMBER my name
Sample Output 1:

True
'''
test_string = input()
# fill the value of the variable below
substring = ''
print(substring in test_string)

'''
Code Challenge — Write a program
Write a program that takes two strings, checks whether the first string contains the second one and prints the result of the membership test.

The variables for both input strings have already been defined.

Sample Input 1:

Big Brother watches you
Father
Sample Output 1:

False
'''
a = input()
b = input()
print(b in a)

# Python → Data types and operations → Comparisons

'''
Code Challenge — Write a program
Write a program that reads an integer value from the input and checks if it is positive.

Hints:

0 is not a positive number.

A comparison already returns a boolean, so if you need the result of the comparison, you can print it, like this print(5 > 9)  # False

Sample Input 1:

8
Sample Output 1:

True
'''
# don't modify this code
# a stores an input value
a = int(input().strip())

# put your code here
print(a > 0)

'''
Code Challenge — Write a program
The movie theater has N cinema halls that can accommodate K viewers each. Figure out if a movie theater can hold V viewers that plan to visit it on a particular day.

The input format

The first line is N cinema halls, the second line is their capacity (K), and the third line is the planned number of viewers (V).

The output format

True or False.

Sample Input 1:

9
68
589
Sample Output 1:

True
'''
# put your python code here
cinema_halls = int(input())
capacity = int(input())
num_of_viewers = int(input())

print(num_of_viewers <= cinema_halls * capacity )

'''
Code Challenge — Write a program
Find out if the result of dividing A by B is an odd number.

The input format:

The first line is the dividend (A) and the second line is the divider (B). It is guaranteed that the numbers are divided without remainder.

The output format:

True or False

Sample Input 1:

99
3
Sample Output 1:

True
'''
# put your python code here
a = int(input())
b = int(input())

print(a % b == 0)

'''
Code Challenge — Write a program
Write a program that reads an integer value from input and checks if it is less than 10 or greater than 250.

Sample Input 1:

0
Sample Output 1:

True
'''
# don't modify this code
# a stores an input value
a = int(input().strip())

# put your code here
print(a < 10 or a > 250)

'''
Code Challenge — Write a program
You are given 3 large numbers, check that they are given in a strictly ascending order.

The input format:

Three lines with three numbers.

The output format:

True or False

Sample Input 1:

7790765547678990
7790765557679990
7790765557778900
Sample Output 1:

True
'''

a = int(input())
b = int(input())
c = int(input())

print(a < b and b < c and a < c)

'''
Code Challenge — Write a program
You are playing a guessing game with a user. Imagine that you came up with an integer stored in a variable set_number.

Check if set_number is equal to the product of two integers entered by the user.

The input format:

Two lines containing integer numbers.

The output format:

True if the user guessed correctly and False otherwise.

Sample Input 1:

3
11
Sample Output 1:

False
'''
set_number = 6557
a = int(input())
b = int(input())

print(a * b == set_number)

# Python → Control flow statements → If statement

'''
Code Challenge — Write a program
Any recipe starts with a list of ingredients. Below is an abstract of a cookbook with the ingredients for some dishes. Write a program that tells you what recipe you can make based on the ingredient you have.

The input format:

A name of some ingredient.

The output format:

A message that says You can make and then the name of the dish. For example, You can make pasta. If the ingredient is featured in several recipes, write about all of them in the order they're featured in the cook book.

Sample Input 1:

basil
Sample Output 1:

You can make pasta
Sample Input 2:

flour
Sample Output 2:

You can make apple pie
You can make chocolate cake
'''
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

ingredient = input()
if ingredient in pasta:
    print("You can make pasta")
if ingredient in apple_pie:
    print("You can make apple pie")
if ingredient in ratatouille:
    print("You can make ratatouille")
if ingredient in chocolate_cake:
    print("You can make chocolate cake")
if ingredient in omelette:
    print("You can make omelette")

'''
Code Challenge — Write a program
Ferryman Charon carries souls across the river to the world of the dead, but does so only for a fee. It's a business after all.

Check whether the recently deceased has a coin, if any, print Welcome to Charon's boat!

The variable coin stores a Boolean value, so it qualifies as a condition. If coin has False value, alas! There's nothing to be done about it.

The variable coin is already defined. So you DON'T need to read its value from the input.

Lastly, let's warn everyone in the underworld (both those in the boat and those overboard) by printing the message There is no turning back.
'''
# the variable `coin` is already defined
if coin:
    print("Welcome to Charon's boat!")
print("There is no turning back.")

'''
Code Challenge — Write a program
Alex wrote a program that reads a number and a word from the input to create phrases like "3 cats" and "1 dog". Unfortunately, the condition for plural nouns is currently missing. Alex doesn't know how to use if statements, but you do. Help Alex complete this program.

The plural form of a word generally ends with s. All numbers, apart from 1, expect the plural form after them, even zero: "0 birds".

Sample Input 1:

1
engineer
Sample Output 1:

1 engineer
Sample Input 2:

12
student
Sample Output 2:

12 students
'''
number = int(input())
word = input()

# write a condition for plurals
if number != 1:
    word += "s"

print(number, word)

# Python → Control flow statements → While loop

'''
Code Challenge — Write a program
When a bank has financial problems the government can return a client's deposit if it is less than 700,000. The interest rate for a particular deposit is 7,1% a year. The percentages are paid to the same deposit at the end of the year and a new value of the interest is calculated.

Find out how many years it will take for the sum of the deposit to exceed the value protected by the government. 

The input format:

The initial sum of the deposit. It is guaranteed that the value will be between 50,000 and 700,000.

The output format:

The number of years.

Sample Input 1:

650000
Sample Output 1:

2
'''
inital_sum = int(input())
counter = 0

while inital_sum < 700000:
    inital_sum *= 1.071
    counter += 1

print(counter)

'''
Code Challenge — Write a program
In nuclear physics, the half-life is used to describe the rate with which elements undergo radioactive decay. More precisely, it is the time required for an element to reduce in half. 

Let's take an isotope of Radium (Ra) called radium-223. Its half-life is almost 12 days (11.43, to be exact). Write a program that calculates how many full half-life periods (in days) it would take for a certain amount of radium-223 to reduce to a specific value.

The input format:

The first line with the starting amount of atoms N (from 2 to 1,000,000), the second line with the resulting quantity R.

The output format:

The number of full half-life periods (in days) T it would take for radium-223 to reduce from N to R. That is if it would take at least 1 half-life period, write 12 and so on.

Sample Input 1:

4
3
Sample Output 1:

12
'''
n = int(input())
r = int(input())
counter = 0

while r < n:
    n //= 2
    counter += 1

print(counter * 12)

'''
Code Challenge — Write a program
The program below is supposed to print the squares of all numbers from 1 to 20, but there are some mistakes. Find them and fix them.
'''

i = 1
while i <= 20:
    print(i * i)
    i += 1

'''
Code Challenge — Write a program
Carl asks you to count the sum of the first k natural numbers. Read k from the input, then add up numbers from 1 to k and print your answer.

Sample Input 1:

18
Sample Output 1:

171
'''

a = int(input())
counter = 1
total = 0

while counter <= a:
    total += counter
    counter += 1
print(total)

'''
Code Challenge — Write a program
Write a program that prints all even numbers less than the input number using the while loop.

The input format:

The maximum number N that varies from 1 to 200.

The output format:

All even numbers less than N in ascending order. Each number must be on a separate line.

Sample Input 1:

8
Sample Output 1:

2
4
6
'''
a = int(input())
counter = 1

while counter < a:
    if counter % 2 == 0:
        print(counter)
    counter += 1

'''
Code Challenge — Write a program
Write a program that calculates the factorial of the input number using while loop.

The input format:

The number N in range from 1 to 100.

The output format:

The factorial N!. 
'''
a = int(input())
counter = 1
total = 1

while counter <= a:
    total *= counter
    counter += 1
print(total)

# Python → Functions → Invoking a function

'''
Invoking a function → Young and beautiful
Code Challenge — Write a program
Find the youngest person among Jack, Alex, Lana and print this person's age.

Sample Input 1:

23
42
34
Sample Output 1:

23
'''
jack_age = int(input())
alex_age = int(input())
lana_age = int(input())

print(min(jack_age, alex_age, lana_age))

'''
Invoking a function → Hello, world!
Code Challenge — Write a program
The classical introductory exercise, slightly modified. Write a program that takes a string, writes it to the variable name (this part of code is already written for you) and then prints "Hello, world! Hello, name".

The variable name is already defined.

Sample Input 1:

John
Sample Output 1:

Hello, world! Hello, John
'''
name = input()

print("Hello, world! Hello,", name)

'''
Invoking a function → String length
Code Challenge — Write a program
Write a program that takes a string and prints its length.

The variable string is already defined.

Sample Input 1:

foo
Sample Output 1:

3
'''
string = input()
print(len(string))

'''
Invoking a function → Minimal number
Code Challenge — Write a program
Write a program that takes two integer numbers x and y and then prints the minimum of them.

Variables x and y are already defined for you.

Sample Input 1:

8
11
Sample Output 1:

8
Sample Input 2:

935
42
Sample Output 2:

42
'''
x = int(input())
y = int(input())
# the variables `x` and `y` are defined, so just print the minimum
print(min(x, y))

'''
Invoking a function → Longest word
Code Challenge — Write a program
Find the longest word in a pair and print its length.

The variables word1 and word2 are defined for you.

Sample Input 1:

Riddikulus
Alohomora
Sample Output 1:

10
Sample Input 2:

earthquake
Supercalifragilisticexpialidocious
Sample Output 2:

34
'''
word1 = input()
word2 = input()

# How many letters does the longest word contain?
print(max(len(word1), len(word2)))

# Python → Functions → Declaring a function

'''
Declaring a function → Define the function
Code Challenge — Write a program
Define the function f(x) that returns the value of the following function defined on the complete number scale:

f(x)= \begin{cases}   1 - (x + 2)^2,\quad &\text{if } x\le -2\\  -\frac x2 ,\quad &\text{if } -2 \lt x \le 2\\   (x-2)^2 + 1,\quad &\text{if } x \gt 2 \end{cases}
f(x)= 
⎩
⎪
⎪
⎨
⎪
⎪
⎧
​ 
  
 1−(x+2) 
2
 ,
 − 
2
x
​ 
 ,
 (x−2) 
2
 +1,
​ 
  
if x≤−2
if −2<x≤2
if x>2
​ 
 

Just implement the function, handling input/output is NOT required.

Sample Input 1:

4.5
Sample Output 1:

7.25
Sample Input 2:

-4.5
Sample Output 2:

-5.25
Sample Input 3:

1
Sample Output 3:

-0.5
'''
def f(x):
    # put your python code here
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x and x <= 2:
        return -0.5 * x
    else:
       return (x - 2) ** 2 + 1

'''
Declaring a function → Fahrenheit
Code Challenge — Write a program
Convert the temperature from Fahrenheit to Celsius in the function below. You can use this formula:
C∘ =(F∘ −32)× 5/9
  
Round the returned result to 3 decimal places.

You don't have to handle input, just implement the function below.
'''
def fahrenheit_to_celsius(num):
    return round((num - 32) * (5 / 9), 3)

'''
Declaring a function → Make the function work
Code Challenge — Write a program
The function closest_mod_5 takes exactly one integer argument x and returns the smallest integer y such that:

y is greater than or equal to x,
y is divisible by 5.
Copy this code and edit the last line to make the function work:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("
'''
def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return x + (5 - x % 5)

'''
Declaring a function → The Sum of 2
Code Challenge — Write a program
Implement a function get_sum(a, b) that will return the sum of two numbers. 

Don't bother about input/output. You just have to implement the function which will return a value. Please, do not rename the function.

Sample Input 1:

8 11
Sample Output 1:

19
'''
# implement the function below
def get_sum(a, b):
    return a + b

'''
Declaring a function → Captain
Code Challenge — Write a program
Define a function that will add the word "captain" before the name of a person.

The function should be named captain_adder, take one argument name and print the string, i.e. it doesn't have to return anything.

Sample Input:

Jack Sparrow

Sample Output:

captain Jack Sparrow
'''
# declare your function here
def captain_adder(name):
    print("captain", name)

'''
Declaring a function → Miles away
Code Challenge — Write a program
Let's take your skill of converting miles to kilometers to the next level! Define a function that accepts the number of miles and returns this distance in kilometers.

Assume that one mile is approximately equal to 1.609 kilometers.

You don't have to handle input, just implement the function.
'''
def mi_to_km(miles):
    return miles * 1.609

# Python → Control flow statements → Else statement

'''
Else statement → Spellchecker
Code Challenge — Write a program
Write a simple spellchecker that tells you if the word is spelled correctly. Use the dictionary in the code below!

The input format:

A single line with the "word".

The output format:

If the word in spelled correctly write Correct, otherwise, Incorrect. 

Sample Input 1:

aa
Sample Output 1:

Correct
'''
dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()

if word in dictionary:
    print("Correct")
else:
    print("Incorrect")

'''
Else statement → Minimum and maximum
Code Challenge — Write a program
Imagine that your friend asked you to write a program that finds the minimum and the maximum.

Write the code that receives two integers as its input, each number goes on a new line. The output should show:

The biggest number - in the first line
The smallest number - in the second line.
Note that your friend might insert identical numbers! Just output both given numbers in this case.

Sample Input 1:

2
8
Sample Output 1:

8
2
'''
a = int(input())
b = int(input())

max_num = max(a, b)
min_num = min(a, b)

print(max_num)
print(min_num)

'''
Else statement → Leap Year
Code Challenge — Write a program
Write a program that checks if a year is leap.

A year is considered leap if it is divisible by 4 and NOT divisible by 100, or if it is divisible by 400. So, 2000 is leap and 2100 isn't.

The program should work correctly on the numbers 1900≤n≤3000.

Output either "Leap" or "Ordinary" depending on the input.

Sample Input 1:

2100
Sample Output 1:

Ordinary
Sample Input 2:

2000
Sample Output 2:

Leap
'''
# put your python code here
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap")
else:
    print("Ordinary")


#  Python → Data types and operations → Quotes and multi-line strings 

'''
Quotes and multi-line strings → Taking turns

Write a program that will print the following multi-line string:

' '' '''
' '' '''
' '' '''
'''

print("' '' '''")
print("' '' '''")
print("' '' '''")

'''
Quotes and multi-line strings → Poetry 

Write a program that will create and print this string from "How The Grinch Stole Christmas":

Did that stop the old Grinch?
No! The Grinch simply said,
"If I can't find a reindeer,
I'll make one instead!"
'''

print("Did that stop the old Grinch?")
print("No! The Grinch simply said,")
print("\"If I can't find a reindeer,")
print("I'll make one instead!\"")

'''
Quotes and multi-line strings → Possessive case 

Make a phrase with a possessive noun out of two strings and print it, for example, the phrase philosopher's stone given the strings philosopher and stone.
'''

word1 = "King"
word2 = "Cross"
# add the correct string instead of the dots
print(word1 + "\'s " + word2)

'''
Quotes and multi-line strings → Triple-quoted string 

Create a program that will print this multi-line string containing triple double quotes:

"""
THIS IS A STRING
"""
'''

print("\"\"\"")
print("THIS IS A STRING")
print("\"\"\"")

'''
Quotes and multi-line strings → A pyramid! 

Write a program that prints a 4-line string, containing:

    at the first line – one single quote
    at the second line – two single quotes with one double quote inside
    at the third line – five alternating single and double quotes, starting with a single quote
    at the fourth line – seven alternating single and double quotes, starting with a single quote

So, the output should look like this:

'
'"'
'"'"'
'"'"'"'
'''

print("'")
print("'\"'")
print("\'\"\'\"\'")
print("\'\"\'\"\'\"\'")

#  Python → Collections → List 

'''
List → An empty list! 
Write a program that will create and print an empty list.
'''
empty_list = []
print(empty_list)

'''
List → Single-element list 
Helen wants to create a list containing only one element – a string with her name. To do this, she wrote this line of code:

name = list('Helen')

However, when she prints the list, her name appears broken into several one-letter strings:

print(name)
# ['H', 'e', 'l', 'e', 'n']
'''
name = ['Helen']
print(name)

'''
List → Reveal the hidden 
There's a predefined variable hidden that contains a list. Count the number of elements in this list and print it.
'''
# use the variable "hidden", it is already defined
print(len(hidden))

'''
List → List from string 
Write a program that constructs a list from the given string's symbols and then prints it.

The variable string has been defined for you.

Sample Input 1:

python

Sample Output 1:

['p', 'y', 't', 'h', 'o', 'n']

Sample Input 2:

John

Sample Output 2:

['J', 'o', 'h', 'n']
'''
# work with this variable
string = input()
print(list(string))


#  Python → Collections → Indexes 

'''
Indexes → Tail 
Sentences generally end with a certain punctuation mark: a period ., an exclamation point !, or a question mark ?.

Find out which of these symbols marks the end of a string stored in the variable sentence and print it out.

Sample Input 1:

What a lovely day!

Sample Output 1:

!
'''
sentence = input()
# print the last symbol below
print(sentence[len(sentence) - 1])

'''
Indexes → Initials 
Find the initial letter of a person's name and print it out.

Make use of the variable name that stores a string.

Sample Input 1:

Kate

Sample Output 1:

K

Sample Input 2:

Ivor

Sample Output 2:

I
'''
name = input()
# print the initial letter
print(name[0])

'''
Indexes → Find the third number 
The list prices contains several numbers. Print the third number from this list.

You don't have to handle the input.

Sample Input 1:

[5230, 5661, 5081, 9539, 5563]

Sample Output 1:

5081
'''
# work with the list 'prices' here
print(prices[2])

'''
Indexes → Latin alphabet 
We have created a variable for the lowercase English alphabet:

alphabet = 'abcdefghijklmnopqrstuvwxyz'

Your task is to print the 15th letter of this string.
'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# put your python code here
print(alphabet[14])

'''
Indexes → Update a list 
Modify the list numbers so that each number in it coincides with its index (not the negative one).

In the end, print the list.
'''
numbers = [4, 1, 0, 3, 2, 5]
# put your python code here
numbers = [0, 1, 2, 3, 4, 5]
print(numbers)

'''
Indexes → Modifying data 
Lists, unlike strings, are mutable. We can use that to modify their data with indexes.

There is a list planets with the names of the Solar system planets. However, instead of the 5th planet, there's an X. Reassign it to the real name of the 5th planet.

Note that the list planets has already been defined, you just need to change one element.
'''
# change the name of the 5th planet in planets
planets[4] = "Jupiter"

#  Python → Control flow statements → Elif statement 

'''
Elif statement → Menu 
Let's say you were asked to create a program for a restaurant: a visitor enters what kind of food they would like to order and gets back the restaurant's offer.

The restaurant has just opened so its menu contains only a few options:

    pizza: Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy
    salad: Caesar salad, Green salad, Tuna salad, Fruit salad
    soup: Chicken soup, Ramen, Tomato soup, Mushroom cream soup

If the visitors asks for something that is not in the menu, the program should write "Sorry, we don't have it in the menu".

Input: "pizza"
Output: "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy"

Input: "burger"
Output: "Sorry, we don't have it in the menu"

Sample Input 1:

pizza

Sample Output 1:

Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy

'''
food = input()
if food == "pizza":
    print("Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy")
elif food == "salad":
    print("Caesar salad, Green salad, Tuna salad, Fruit salad")
elif food == "soup":
    print("Chicken soup, Ramen, Tomato soup, Mushroom cream soup")
else:
    print("Sorry, we don't have it in the menu")
    
'''
Elif statement → What day is it? 

Today the whole world uses the Coordinated Universal Time (UTC) to distinguish between the time zones. The UTC is considered to be the 0, and the rest of the time zones are expressed using positive or negative offsets from the UTC. For instance, London is in the zone UTC+00:00 (or GMT) and Moscow is in the zone UTC+3:00. 

There are 14 positive offsets (from UTC+1:00 to UTC+14:00) and 12 negative offsets (from UTC-12:00 to UTC-1:00). This also means that at a particular hour, three calendar days are observed on the planet.

Imagine, it is 10:30 on a Tuesday in London (UTC). What day of the week is it in a specific timezone?

The input format:

The value of offset with the sign (e.g. +3 or -9).

The output format:

The day of the week in that timezone. 

Sample Input 1:

0

Sample Output 1:

Tuesday

Sample Input 2:

-11

Sample Output 2:

Monday
'''
offset = input()
if offset == "0":
    print("Tuesday")
elif len(offset) == 2:
    print("Tuesday")
else:
    if offset[0] == "-" and int(str(offset[1]) + str(offset[2])) > 10:
        print("Monday")
    elif offset[0] == "+" and int(str(offset[1]) + str(offset[2])) == 14:
        print("Wednesday")
    else:
        print("Tuesday")

'''
Elif statement → Computer hours 

Write a program that asks a user how long, on average, they spend on a computer per day and:

if it is less than 2 hours says 'That seems reasonable'
else if it is less than 4 hours per day says 'Do you have time for anything else?'
else the programs says 'You need to get outside more!'

Sample Input 1:

6

Sample Output 1:

You need to get outside more!
'''
# Make sure your output matches the assignment *exactly*
computer_hours = int(input())
if computer_hours < 2:
    print("That seems reasonable")
elif computer_hours < 4:
    print("Do you have time for anything else?")
else:
    print("You need to get outside more!")

'''
Elif statement → Calculator 

Let's write a simple calculator!

It will read 3 lines:

    the first number
    the second number
    the arithmetic operation.

Numbers are floats!

The output is the result of the following: first_number operation second_number.

Operations are: +, -, /, *, mod, pow, div.
mod — modulo operation, i.e. the remainder of the division first_numer % second_number,
pow — exponentiation, the first number will be the base and the second — the power: first_number ** second_number,
div — integer division first_number // second_number.

Note that if the second number is 0 and you want to perform any of the operations /, mod, or div, the calculator should say "Division by 0!"

Sample Input 1:

5.0
0.0
mod

Sample Output 1:

Division by 0!

Sample Input 2:

-12.0
-8.0
*

Sample Output 2:

96.0

Sample Input 3:

5.0
10.0
/

Sample Output 3:

0.5
'''
# put your python code here
n1 = float(input())
n2 = float(input())
op = input()
# +, -, /, *, mod, pow, div.
if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "/":
    if int(n2) == 0:
        print("Division by 0!")
    else:
        print(n1 / n2)
elif op == "*":
    print(n1 * n2)
elif op == "mod":
    if int(n2) == 0:
        print("Division by 0!")
    else:
        print(n1 % n2)
elif op == "pow":
    print(n1 ** n2)
else:
    if int(n2) == 0:
        print("Division by 0!")
    else:
        print(n1 // n2)

'''
Elif statement → Particles 
The world of elementary particles is rather complex. There are many different classes and they can interact in a rather interesting way.

Two important characteristics of the elementary particles are the spin and the electric charge. Here are some of the elementary particles:
Particle    Class   Spin    Electric charge
Strange     Quark   1/2     -1/3
Charm   Quark   1/2     2/3
Electron    Lepton  1/2     -1
Muon    Lepton  1/2     0
Photon  Boson   1   0
Higgs boson     Boson   0   0

Write a program that returns the particle and its class based on its spin and electric charge.

The input format:

Two lines: first the spin of the particle, then its charge.

The output format:

The particle and its class separated by a space.

Sample Input 1:

1/2
-1/3

Sample Output 1:

Strange Quark
'''
spin = input()
charge = input()
if spin == "1/2":
    if charge == "-1/3":
        print("Strange Quark")
    elif charge == "2/3":
        print("Charm Quark") 
    elif charge == "-1":
        print("Electron Lepton")
    else:
        print("Muon Lepton")
elif spin == "1":
    print("Photon Boson")
else:
    print("Higgs boson Boson")


'''
Elif statement → Grade 
There is a number of grades you can get in a test: A, B, C, D, F. The percentages are the following:

A: 90-100%

B: 80-90%

C: 70-80%

D: 60-70%

F: <60%

Determine the grade that a student will get based on the student's score and the maximum score.

Note that the upper limit is not included in the range, except for the A grade. For example, a student with 60% will get D, with 70% or 79.9% — C, but the top score 100% is just A.

The input format:

Two lines: the first with a student's score and the second with the maximum.

The output format:

The grade of the student.

Sample Input 1:

75
100

Sample Output 1:

C

Sample Input 2:

100
200

Sample Output 2:

F
'''
student_score = int(input())
max_score = int(input())

if (student_score / max_score) * 100 >= 90:
    print("A")
elif (student_score / max_score) * 100 >= 80 and (student_score / max_score) * 100 < 90:
    print("B")
elif (student_score / max_score) * 100 >= 70 and (student_score / max_score) * 100 < 80:
    print("C")
elif (student_score / max_score) * 100 >= 60 and (student_score / max_score) * 100 < 70:
    print("D")
else:
    print("F")

'''
Elif statement → Index of synthesis 

One way to classify the languages of the world is by looking at their morphological systems. One classification is based on the index of synthesis that reflects an average number of morphemes in a word. The values vary between 1 and 4 and there are 3 types of languages according to that system. Here are they:

Type — Index

Analytic — less than 2

Synthetic — from 2 to 3

Polysynthetic — more than 3

Write a program that given the index of synthesis determines the type of the language.

The input format:

The value of the index of synthesis.

The output format:

The type of language.

Sample Input 1:

2.35

Sample Output 1:

Synthetic

Sample Input 2:

1.68

Sample Output 2:

Analytic
'''
value = float(input())
if value < 2:
    print("Analytic")
elif 2 <= value <= 3:
    print("Synthetic")
else:
    print("Polysynthetic")

'''
Elif statement → The farm 

In a farming game, you can buy certain animals for a specific price. As a player, you want to buy the most useful (i.e. the most expensive) animal. Here are the animals and their prices:

Item: Price

Chicken: 23

Goat: 678

Pig: 1296

Cow: 3848

Sheep: 6769

Write a program that determines what is the most expensive animal that the user can buy with their money and how many of them they can buy.

The input format:

The money that the user has.

The output format:

How many animals the user can afford, for example, 20 chickens or 4 cows. If the user cannot afford any animal, write None. 

Pay attention to the number of nouns. Also, keep in mind that the word "sheep" has the irregular plural form "sheep".

Sample Input 1:

25

Sample Output 1:

1 chicken

Sample Input 2:

8

Sample Output 2:

None

Sample Input 3:

668

Sample Output 3:

29 chickens
'''
money = int(input())
count = 0
if money < 23:
    print("None")
elif 23 <= money < 678:
    count = money // 23
    if count == 1:
        print("1 chicken")
    else:
        print(str(count) + " chickens")
elif 678 <= money < 1296:
    count = money // 678
    if count == 1:
        print("1 goat")
    else:
        print(str(count) + " goats")
elif 1296 <= money < 3848:
    count = money // 1296
    if count == 1:
        print("1 pig")
    else:
        print(str(count) + " pigs")
elif 3848 <= money < 6769:
    count = money // 3848
    if count == 1:
        print("1 cow")
    else:
        print(str(count) + " cows")
else:
    count = money // 6769
    print(str(count) + " sheep")

'''
Elif statement → The army of units
In a computer game, each gamer has an army of units.

Write a program that will classify the army of your enemies corresponding to the following rules:

 

Units:  Category

less than 1: no army

from 1 to 9: few

from 10 to 49: pack

from 50 to 499: horde

from 500 to 999: swarm

1000 and more: legion

 

The program should read the number of units and output the corresponding category.

Sample Input 1:

18

Sample Output 1:

pack

Sample Input 2:

5

Sample Output 2:

few
'''
units = int(input())
if units < 1:
    print("no army")
elif 1 <= units <= 9:
    print("few")
elif 10 <= units <= 49:
    print("pack")
elif 50 <= units <= 499:
    print("horde")
elif 500 <= units <= 999:
    print("swarm")
else:
    print("legion")

'''
Elif statement → Healthy sleep 

Ann watched a TV program about health and learned that it is recommended to sleep at least AA hours per day, but oversleeping is also not healthy and you should not sleep more than BB hours. Now, Ann sleeps HH hours per day.

If Ann's sleep schedule complies with the requirements of that TV program, print "Normal". If Ann sleeps less than AA hours, output "Deficiency", if she sleeps more than BB hours, output "Excess".

The input comprises three strings with variables in the following order: A A A, B B B, H H H.

A A A is always less than or equal to B B B.

Sample Input 1:

6
10
8

Sample Output 1:

Normal

Sample Input 2:

7
9
10

Sample Output 2:

Excess

Sample Input 3:

7
9
2

Sample Output 3:

Deficiency
'''
# put your python code here

input_a = int(input())
input_b = int(input())
input_h = int(input())

if input_h < input_a:
    print("Deficiency")
elif input_h > input_b:
    print("Excess")
else:
    print("Normal")

'''
Elif statement → Positive, Negative or Zero 

Write a program that reads an integer number and prints:

    "negative" if the number is less than 0;
    "positive" if the number is greater than 0;
    "zero" if the number equals 0.

Do not output double quotes.

Sample Input 1:

-5

Sample Output 1:

negative

'''
# put your python code here
num = int(input())
if num < 0:
    print("negative")
elif num > 0:
    print("positive")
else:
    print("zero")

'''
Elif statement → Recommender system 

Write a program that recommends one of the following movies based on the age of a user:

<=16<= 16<=16 "Lion King"

17−2517 - 2517−25 "Trainspotting"

26−4026 - 4026−40 "Matrix"

41−6041 - 6041−60 "Pulp Fiction"

>60> 60>60 "Breakfast at Tiffany's"

The user enters their age and the program outputs one title.

Sample Input 1:

19

Sample Output 1:

Trainspotting

Sample Input 2:

71

Sample Output 2:

Breakfast at Tiffany's
'''
age = int(input())
if age <= 16:
    print("Lion King")
elif 17 <= age <= 25:
    print("Trainspotting")
elif 26 <= age <= 40:
    print("Matrix")
elif 41 <= age <= 60:
    print("Pulp Fiction")
else:
    print("Breakfast at Tiffany's")

'''
Locate a point on the Cartesian coordinate plane: which of four quadrants does a point belong to?

Read two numbers from the input, not necessarily integers, the first number will indicate a position on the X-axis, the second one — on the Y-axis. Let's keep referring to the quadrants by Roman numerals, as shown in the picture.

The points lying on the axes, with either x = 0 or y = 0, and the origin (0, 0) will not appear in the tests.

Sample Input 1:

3.987
-10

Sample Output 1:

IV
'''

x = float(input())
y = float(input())

if x > 0 and y > 0:
    print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
else:
    print("IV")

'''
Elif statement → Long live the king 

Figure out how many moves a chess king can make from a square with given coordinates. The coordinates are numbers between 1 and 8 inclusively. The first number indicates a column, the second one indicates a row.

The king moves one square in any direction (horizontally, vertically, or diagonally). Other rules, as well as special moves, are not taken into account.

Sample Input 1:

3
2

Sample Output 1:

8
'''
column = int(input())
row = int(input())

if column == 1:
    if row in (1, 8):
        print(3)
    else:
        print(5)
elif column == 8:
    if row in (1, 8):
        print(3)
    else:
        print(5)
elif 1 < column < 8:
    if row in (1, 8):
        print(5)
    else:
        print(8)
else:
    print(8)

#  Python → Collections → Tuple 

'''
Tuple → The last number 

Given a tuple consisting of numbers, print its last element.

Sample Input 1:

24 22 42

Sample Output 1:

42
'''
# use this tuple
numbers = tuple(int(n) for n in input().split())
print(numbers[len(numbers) - 1])

'''
Tuple → Oceans 

Turn a list oceans into a tuple to prevent further data change.

You are NOT supposed to create a new variable for the tuple or print anything.
'''



'''
Tuple → Alphabet 

Suppose we have a string with some alphabet and we want to store all the letters from it in a tuple. Read the input string and print this tuple.

Sample Input 1:

abcdefghijklmnopqrstuvwxyz

Sample Output 1:

('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
'''
# work with this string
alphabet = input()
print(tuple(alphabet))

'''
Tuple → A single-element tuple 

Alice tried to define a singleton tuple with the first and only item [0, 1, 1, 2, 3, 5, 8, 13, 21]. Alas, one small detail is missing here. Fix the code Alice wrote.

You are NOT supposed to create a new variable for the tuple or print anything.
'''
# fix the code below
singleton = ([0, 1, 1, 2, 3, 5, 8, 13, 21],)

'''
Tuple → Name 

From the input, you get the first and the last name of a person. Create a tuple with the full name: the first element should be the first name and the second element should be the last name. Save the resulting tuple to the variable full_name. Do NOT print anything!

The variables first_name and last_name have already been read from input.

Example. Suppose, first_name is "John" and last_name is "Doe". The resulting tuple should be ("John", "Doe")
'''
first_name = input()
last_name = input()

# create full_name here
full_name = (first_name, last_name)

#  Python → Functions → Arguments  

'''
Arguments → URL 

Declare a function called create_url(). It should take two arguments host and port and return URL in the format "https://{host}:{port}".

Set default values for both parameters: a string "localhost" and an integer 443 respectively. Called without arguments, the function would return "https://localhost:443".
'''
def create_url(host="localhost", port=443):
    return "https://" + str(host) + ":" + str(port)

'''
Arguments → Favorable default 

Write a short function code that will print out this message:

We code in {language}

Set "Python" as a default value to the language parameter.
'''
def code(language="Python"):
    print("We code in", language)

'''
Arguments → Call me by my name 

There is a function called add_book() that takes a non-empty string containing the title of a book to add it to recommendations. Share your favorite book with us by calling this function. Importantly, specify the keyword argument title in the call. Otherwise, you may get an error.
'''
add_book(title="Stuff")

'''
Arguments → Misfortune 

Robin has declared a function that prints the squares of odd numbers in the specified range. Unfortunately, several function calls gave an unexpected result. The function itself seems to be fine. Help Robin figure out what went wrong in these calls and fix them.

For each case, the required range is written in a comment.
'''
def square_odds(a, b):
    start = a
    if a % 2 == 0:
        start += 1
    end = b + 1
    for odd in range(start, end, 2):
        print(odd ** 2)


# from 22 to 42
square_odds(22, 42)

# from 15 to 31
square_odds(15, 31)

# from 42 to 49
square_odds(42, 49)


'''
Arguments → Warm welcome

Morgan founded a company that sends satellites into the orbit to observe Earth from space. To headhunt the best aerospace engineers, Morgan decided to pay a welcome bonus equal to 35% of the base salary. However, the bonus may be even higher for a particular candidate.

Declare a function get_bonus() below that would calculate this bonus. It should take two arguments, salary and percentage, with a default value 35 for the last one. Return only the integer part of the bonus.
'''
def get_bonus(salary, percentage=35):
    bonus = (salary * percentage) / 100
    return int(bonus)

#  Python → Collections → Operations with list 

'''
Write a program that takes n numbers as input, creates a list from them and then prints it.

The first input line is n – length of the resulting list. It is followed by n lines containing list elements.

Sample Input 1:

5
100
-1
72
0
0

Sample Output 1:

[100, -1, 72, 0, 0]
'''
n = int(input())
input_list = []
for i in range(n):
    input_list.append(int(input()))
print(input_list)

'''
Operations with list → Changed beyond recognition 
Dany created this list:

dragons = ['Rudror', 'Targiss', 'Coporth']

and then played with it for some time. She used some operations on it, so the result looks like this:

['Coporth', -10, 'Rudror', 'Targiss']

Now Dany is confused and wants to understand what she has done exactly. Help her out! Place the operations in the correct order (the order in which they were used, from the first to the last).

Let’s find out what was the last operation Dany did. Sorting can’t be the last operation, since a list containing both numbers and strings can’t be sorted, and inserting -10 to the position 2 can’t be the last operation, because in the resulting list -10 is at the position 1, not the position 2. So, dragons.reverse() was the last operation. From the remaining two, obviously, dragons.sort(reverse=True) was earlier, since you can’t sort a list of strings after inserting an integer number to it. Here are all changes made into a list:

['Rudror', 'Targiss', 'Coporth']
dragons.sort(reverse=True)
['Targiss', 'Rudror', 'Coporth']
dragons.insert(2, -10)
['Targiss', 'Rudror', -10, 'Coporth']
dragons.reverse()
['Coporth', -10, 'Rudror', 'Targiss']
'''

'''
Operations with list → Shopping list 

Ruth goes shopping today, so she is busy making a shopping list.

She wrote down things that she would like to buy at the grocery store: first "milk", then "olive oil" and "bananas". When sneaking a look at the fridge, she noticed that there was some milk left and changed her mind about buying a new one. It got crossed out of the list. And, like a cherry on top, a "brownie" became the last item Ruth had put on the list.

Now you try to replicate these operations on the variable shopping_list.

You are NOT supposed to print the results.
'''
# work with this variable
shopping_list = []

shopping_list.append("milk")
# put the rest of list operations below
shopping_list.append("olive oil")
shopping_list.append("bananas")
shopping_list.remove("milk")
shopping_list.append("brownie")

'''
Operations with list → Sort the numbers 

Below you can see a list of strings called numbers. Sort it in the descending order as strings (alphabetically) and print the resulting list.
'''
numbers = ["77", "145", "987", "2095", "6", "371", "4999", "81"]

# sort numbers
numbers.sort(reverse=True)
print(numbers)

#  Python → Modules and packages → Load module 

'''
Load module → Capitalize all words 

Write a program that takes a string, capitalizes all words in it and then prints the result. Use capwords function from the string module.

The string is already defined.

Sample Input 1:

a aaaa aaaaaaaa

Sample Output 1:

A Aaaa Aaaaaaaa
'''
# place `import` statement at top of the program
import string

# don't modify this code or the variable may not be available
input_string = input()

# use capwords() here
print(string.capwords(input_string))

'''
# Load module → Calculating the factorial 

Import factorial function from math module and print the value of the factorial of x.

Sample Input 1:

5

Sample Output 1:

120
'''
# place `import` statement at top of the program
from math import factorial

# don't modify this code or variable `x` may not be available
x = int(input())

# use factorial() here
print(factorial(x))

'''
Load module → E ** x minus one 

Write a program that takes an integer number x and prints e (a mathematical constant) raised to power x minus one. Use the function expm1 defined in the math module.

The variable x is already defined.

Sample Input 1:

91

Sample Output 1:

3.317400098335743e+39
'''
# place `import` statement at top of the program
from math import expm1

# don't modify this code or variable `x` may not be available
x = int(input())

# use expm1() here
print(expm1(x))

'''
Load module → Working with strings 

Print the values of digits and ascii_lowercase from string module on separate lines.
'''
# put your code here
import string

print(string.digits)
print(string.ascii_lowercase)

'''
Load module → Not exactly random 

Numbers, generated by functions provided in random module, are not exactly random – they use random number generator based on some number (by default, on the current system time). You can also set this number with the seed function – and all numerical sequences generated after that will be the same.

Write a program that takes an integer number n, sets a random number generator to that number and then prints a pseudo-random number from -100 to 100.

Use seed and randint functions. The former takes one argument and the latter takes two numbers that represent the range.

The variable n is already defined.

Sample Input 1:

36

Sample Output 1:

-16
'''
# place `import` statement at top of the program
import random

# don't modify this code or variable `n` may not be available
n = int(input())

# put your code here
random.seed(n)
print(random.randint(-100, 100))

'''
Load module → Copysign function 

Write a program that takes two float numbers, x and y, and prints x with the sign of y. Use copysign function defined in the math module.

Variables x and y are already defined.

Sample Input 1:

-68.83573394536573 -66.80342071491599

Sample Output 1:

-68.83573394536573
'''
# place `import` statement at top of the program
from math import copysign

# don't modify this code or the variables may not be available
x, y = map(float, input().split(' '))

print(copysign(x, y))

#  Python → Math → Random module 

'''
Random module → The dice game 

It's impossible not to know the dice game. Please, write a program that will imitate a roll of one dice with the help of an appropriate random function.

Thus, your task is just to generate one integer and print it.

The module random has been imported for you.
'''
# The `random` module has been imported.
# Use a function from it in the next line
print(random.randint(1, 6))

'''
Random module → From 0 to 1 

The function used to set a starting point of the random search algorithm is called random.seed() and takes a single integer number. Write a program that takes an integer number n, sets a seed to n and then prints a pseudo-random number from 0 to 1.

The variable n is already defined.

Sample Input 1:

-38

Sample Output 1:

0.6394736947203203
'''
import random
# work with this variable
n = int(input())
random.seed(n)
print(random.uniform(0, 1))

'''
Random module → Yoda style 

Everybody wants to speak like master Yoda sometimes. Let's try to implement a program that will help us with it. 

First, we turn the string of words into a list using the string.split() method.

Then use the function random.seed(43) and rearrange the obtained sequence.

To turn the list back into a string, use ' '.join(list). 

Print the message in the end.

Note: you have to use random.seed(43) in this task!

Sample Input 1:

Luke, I'm your father

Sample Output 1:

your father I'm Luke,

Sample Input 2:

I will be back

Sample Output 2:

be back will I
'''
import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
random.seed(43)
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))


'''
Random module → Voldemort 

The function used to set a starting point of the random search algorithm is called random.seed() and takes a single integer number. Write a program that takes a single number n, sets a seed to n and then prints a pseudo-randomly chosen letter from the string "Voldemort".

The variable n is already defined.
'''
import random
# work with this variable
n = int(input())
random.seed(n)
print(random.choice("Voldemort"))

'''
Random module → Beta distribution 

Python is widely used for mathematical purposes. Calculate the beta distribution where alpha=0.9 and beta=0.1.

Print your results.
'''
import random
random.seed(3)
# call the function here
print(random.betavariate(alpha=0.9, beta=0.1))

#  Python → Data types and operations → String formatting 

'''
String formatting → Beautify both output and code 

The output should be user-friendly, but the code part is also important. Well-structured and readable code is very important for being a good programmer. Now it's up to you to decide, which formatting method to choose.

Imagine you need to compose a dynamic URL for every certain user with user-specific details. Suppose, you want to send different URLs for every user, depending on their name and profession. The base would be something like

"http://example.com/*nickname*/desirable/*profession*/profile", where nickname and profession are prompts from a user and are dynamic.

Prompt a user for their nickname and profession and print a user-specific URL. Don't bother about any rules of composing the URLs and just use raw input to accomplish the task.

Sample Input 1:

raybeam
cereal-killer

Sample Output 1:

http://example.com/raybeam/desirable/cereal-killer/profile

Sample Input 2:

AnnMelon
bodybuilder

Sample Output 2:

http://example.com/AnnMelon/desirable/bodybuilder/profile
'''
nickname = input()
profession = input()

print("http://example.com/{0}/desirable/{1}/profile".format(nickname, profession))

'''
String formatting → How long is that word? 

Write a program that calculates the length of the word from the input and prints it out together with the word in the format word has N letters. 

Sample Input 1:

serendipity

Sample Output 1:

serendipity has 11 letters
'''
word = input()
print("{0} has {1} letters".format(word, len(word)))

'''
String formatting → Decimal places 

Round the number from input to the required number of decimals.

The input format:

Two lines: the first with a floating-point number, the second with an integer representing the decimal count.

The output format:

The rounded number.

Do NOT forget to convert the input numbers and to enclose each value in {} in a formatted string.

Sample Input 1:

2.71828
3

Sample Output 1:

2.718
'''
num = float(input())
place = int(input())

print(f'{num:.{place}f}')

'''
String formatting → Round pi 

Write a code that rounds the number pi to 5 decimal places and prints it out.

We've defined the variable pi for you.
'''
pi = 3.141592653589793
print(f'{pi:.5f}')

'''
String formatting → Film 

Write a program that gets information about a movie from the input and presents in the following format:

movie (dir. director) came out in year

The input format:

3 lines: first the title of the movie, then the name of the director and then the year of its release.

Sample Input 1:

Fight Club
David Fincher
1999

Sample Output 1:

Fight Club (dir. David Fincher) came out in 1999
'''
movie = input()
director = input()
year = input()
print(f"{movie} (dir. {director}) came out in {year}".format(movie, director, year))

'''
String formatting → Tax brackets 

n progressive tax systems, tax rates change according to the income. Tax brackets are divisions that regulate those changes. 

Here's an example of tax brackets in a certain tax system:

0 — 15,527: 0% tax

15,528 — 42,707: 15% tax

42,708 — 85,414: 22% tax

85,415 — 132,406: 26% tax

132,407 and more: 28% tax

Suppose we use a simplified version of taxation and apply one tax rate to the entire amount of money.

Write a program that calculates the tax that a person's going to pay based on their income.

The input format:

The value of someone's taxable income (in dollars).

The output format:

The tax for {income} is {percent}%. That is {calculated_tax} dollars!

The calculated_tax should always have 2 decimal places.

Sample Input 1:

14378

Sample Output 1:

The tax for 14378 is 0%. That is 0.00 dollars!

Sample Input 2:

99999

Sample Output 2:

The tax for 99999 is 26%. That is 25999.74 dollars!
'''
income = int(input())
percent = 0
if 0 <= income <= 15527:
    percent = 0
elif 15528 <= income <= 41707:
    percent = 15
elif 42708 <= income <= 85414:
    percent = 22
elif 85415 <= income <= 132406:
    percent = 26
else:
    percent = 28

calculated_tax = income * (percent / 100)
print(f'The tax for {income} is {percent}%. That is {calculated_tax:.2f} dollars!')

#  Python → Data types and operations → Basic string methods 

'''
Basic string methods → Markdown parsing 

Markdown syntax is used to format a text. There are several ways to emphasize it using Markdown:
Typeface    Example
Italic text     *italics*, _same italics_
Bold text   **bold**, __same bold__
Strikethrough text  ~~crossed out~~
Code snippet    `code`

Read an input and parse the text so that it doesn't include special symbols mentioned in the table "*_~`" at its beginning and its end.

Do not forget to print the result.

Sample Input 1:

**Important info**

Sample Output 1:

Important info

Sample Input 2:

~~hidden ~ tilde~~

Sample Output 2:

hidden ~ tilde
'''
markdown = input()
print(markdown.lstrip("*_~`").rstrip("*_~`"))

'''
Basic string methods → Preprocessing 

Preprocess an input text:

    delete punctuation symbols (commas, periods, exclamation and question marks ,.!?),
    convert all symbols to lowercase.

Then print your text.

Punctuation marks appear not only at the end of the input string, so you have to figure out how to get rid of all of them.

Sample Input 1:

Nobody expects the Spanish inquisition!

Sample Output 1:

nobody expects the spanish inquisition
'''
input_text = input()
input_text = input_text.replace(",", "")
input_text = input_text.replace(".", "")
input_text = input_text.replace("!", "")
input_text = input_text.replace("?", "")
input_text = input_text.lower()
print(input_text)

'''
Basic string methods → Poster artist 

Imagine that you design film posters for a living. Write a program that prints each film title in all caps.

Sample Input 1:

the lion king

Sample Output 1:

THE LION KING

Sample Input 2:

MaTRiX

Sample Output 2:

MATRIX
'''
print(input().upper())

#  Python → Collections → Set 

'''
Set → Letters 

Write a program that calculates how many unique letters the input word has. The word is stored in the variable word. Print out the result you'll get.

Sample Input 1:

mississippi

Sample Output 1:

4
'''
word = input()  # the input word
print(len(set(word)))

'''
Set → Mystery set 

There is an unknown set of objects named mystery_set which has been defined beforehand. You don't have access to this set.

Write a program that deletes the input string (stored in the variable string) from the mystery_set. It is NOT guaranteed that the string is an element of the mystery_set to begin with. Don't forget to take that into account!

Don't print anything!
'''
# mystery_set has been defined
string = input()

# delete string from mystery_set
mystery_set.discard(string)

'''
Set → Memory test 

Today you are assisting in a psychological experiment. To test a short-term memory, a researcher gives a set of numbers to each volunteer and asks to repeat all of them in any order. Repeats are allowed in the answer, but not the numbers not mentioned earlier.

The input has been read into two variables for you.

If the volunteer remembers the numbers correctly, print True, otherwise, you should output False.

Sample Input 1:

1 2 3 4 5
5 4 1 2 1 3

Sample Output 1:

True

Sample Input 2:

999 1 1001 15 6 7
1 6 7 1 999

Sample Output 2:

False

Sample Input 3:

3 4 5 7
3 4 5 6 7

Sample Output 3:

False
'''
numbers = input().split()
answers = input().split()

print(set(numbers) == set(answers))

'''
Set → Counting unique 

Imagine you have information about the three students: which subjects they study. It could be in the following format:

Belov = ["Physics", "Math", "Russian"]
Smith = ["Math", "Geometry", "English"]
Sarada = ["Japanese", "Math", "Physics"]

The subjects can be the same or differ. Your task is to find the amount of unique subjects.

 

NB! Don't write the prompting code. In this task you're given the variables to work: Belov, Smith, and Sarada.

Sample Input 1:

{"Belov": ["Physics", "Math", "Russian"], "Smith": ["Math", "Geometry", "English"], "Sarada": ["Japanese", "Math", "Physics"]}

Sample Output 1:

6
'''
# please, work with the variables 'Belov', 'Smith', and 'Sarada'
unique_subjects = set()
for i in range(0, len(Belov)):
    unique_subjects.add(Belov[i])
for i in range(0, len(Smith)):
    unique_subjects.add(Smith[i])
for i in range(0, len(Sarada)):
    unique_subjects.add(Sarada[i])
    
print(len(unique_subjects))

#  Python → Control flow statements → For loop 

'''
For loop → A mean of n 

Write a program that reads an integer number n. This is a number of integer values you will receive on the next n lines. Your program should compute their mean value.

Print the mean as a float number.

Sample Input 1:

8
5
-7
6
2
5
5
-7
-10

Sample Output 1:

-0.125
'''
n = int(input())
total = 0

for i in range(0, n):
    total += int(input())

print(total / n)

'''
For loop → Speech generation 

Here is your chance to write instructions for a text-to-speech system. Let's focus on reading phone numbers aloud. The input phone number will consist solely of digits. Print the name of each digit on a new line for the system to read them one by one.

You can store the digit names in a container, e.g. in a list with the names from 0 to 9 digits = ['zero', 'one', 'two', ..., 'nine'], and refer to each digit by index, digits[2] equals to 'two', etc. Mind the type, an index should be an interger, not a string.

Sample Input 1:

4901825

Sample Output 1:

four
nine
zero
one
eight
two
five
'''
number = input()
digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for char in number:
    print(digits[int(char)])

'''
For loop → Lucky 7 

Find all numbers that can be divided by 7 and print their squares.

The input format:

In the first line, there's an integer number of values n.

Then you'll receive n lines with one number on each.

The output format:

m lines with the squares of all numbers that can be divided by 7.

Sample Input 1:

5
8
11
-49
0
3564 

Sample Output 1:

2401
0
'''
n = int(input())
for _i in range(0, n):
    x = int(input())
    if x % 7 == 0:
        print(x * x)

'''
For loop → Arithmetic mean 

Calculate the arithmetic mean of a list. The arithmetic mean is a sum of all elements divided by their total number.

Elements are given in the list numbers. Find their sum, divide it by the number of elements and then print the result.

Sample Input 1:

10 15 1 6 3

Sample Output 1:

7.0
'''
numbers = [int(x) for x in input().split()]
total = 0
for i in numbers:
    total += i
print(total / len(numbers))

'''
For loop → The average of all numbers 

Write the code that reads 2 numbers from the keyboard, a and b. As an output, it shows the average of all numbers that lie on the interval between a and b, and can be divided by 3. 

What does it mean? In the example, you are to calculate the average of the numbers in the range [−5;12] [-5; 12] [−5;12]

The numbers divided by 3 without the remainder are: −3,0,3,6,9,12 -3, 0, 3, 6, 9, 12 −3,0,3,6,9,12. There are six of them, and the average is 4.5.

The input interval always contains at least one dividend of 3. Remember to include the values of a and b in your calculations.

Sample Input 1:

-5
12

Sample Output 1:

4.5
'''
# put your python code here
a = int(input())
b = int(input())
total = 0
counter = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        total += i
        counter += 1
print(total / counter)

'''
For loop → Vowel count 

Have a look at the program that iterates through string and counts vowels in it. Fill in the blank to make it work.
'''
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0

# fix this for loop
for letter in string:
    if letter in vowels:
        count += 1

'''
For loop → FizzBuzz 

FizzBuzz is a famous code challenge used in interviews to test basic programming skills. It's time to write your own implementation.

Print numbers from 1 to 100 inclusively following these instructions:

    if a number is multiple of 3, print "Fizz" instead of this number
    if a number is multiple of 5, print "Buzz" instead of this number
    for numbers that are multiples of both 3 and 5, print "FizzBuzz"
    print the rest of the numbers unchanged.

Output each value on a separate line.
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Python → Control flow statements → Loop control statements

'''
Loop control statements → Small scale

Read lines with floats from the input until you get a single period . that signals you to stop.

Find the minimum of these numbers and print it out.

Sample Input 1:

11.1
2.05
4.0
.
Sample Output 1:

2.05
'''
num_list = []
user_input = input()
while user_input != ".":
    num_list.append(float(user_input))
    user_input = input()
print(min(num_list))

'''
Loop control statements → Count up the squares

Write a program that reads from the console numbers (one in a line) until their sum is equal to 0. Immediately after that, it should display the sum of the squares of all the entered numbers.

It is guaranteed that at some point the sum of the entered numbers will be equal to 0. After that, reading is not necessary to continue.

In case the first integer equals to 0, also stop reading values from the input. Print out 0 instead of the sum of the squares.

For example, we are reading the numbers 1, -3, 5, -6, -10, 13. At this point, we have noticed that the sum of these numbers is 0 and output the sum of their squares, not paying attention to the fact that there are still unread values.

Sample Input 1:

1
-3
5
-6
-10
13
4
-8
Sample Output 1:

340
'''
# put your python code here
user_input = int(input())
_sum = user_input
squared_sum = user_input * user_input

while _sum != 0:
    user_input = int(input())
    _sum += user_input
    squared_sum += user_input * user_input
print(squared_sum)

'''
Loop control statements → Prime number

Determine whether the input number is a prime number.

The output options:

This number is prime

This number is not prime

Sample Input 1:

6
Sample Output 1:

This number is not prime
'''
user_input = int(input())
is_prime = True

for i in range(2, user_input):
    if user_input % i == 0:
        is_prime = False
        break

if is_prime:
    print("This number is prime")
else:
    print("This number is not prime")

'''
Loop control statements → Process integer input

Write a program that reads integers from the console, one number per line.

For each input number you should check:

if the number is less than 10, then skip this number;
if the number is greater than 100, then stop reading numbers from the console;
in other cases, print this number back to the console on a separate line.
Sample Input 1:

12
4
2
58
112
Sample Output 1:

12
58
Sample Input 2:

101
Sample Output 2:

Sample Input 3:

1
2
102
Sample Output 3:

'''
# put your python code here
user_input = int(input())

while user_input:
    if user_input > 100:
        break
    if user_input >= 10:
        print(user_input)
    user_input = int(input())
'''
Loop control statements → Palindrome

Palindrome is a word or a text that reads the same backward as forward. Create a program that checks if the word is palindrome.

The input format:

Word that needs to be checked. It is guaranteed that the word will be of even length.

The output format:

If the word is palindrome, write Palindrome. Otherwise, write Not palindrome

Sample Input 1:

noon
Sample Output 1:

Palindrome
Sample Input 2:

banana
Sample Output 2:

Not palindrome
'''
# put your python code here
user_input = input()
is_palindrome = True
for i in range(len(user_input) // 2):
    if user_input[i] != user_input[len(user_input) - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not palindrome")

'''
Loop control statements → Vowels and consonants

You'll get a sequence of characters (a word, a sentence or just gibberish). For each character tell if it's a vowel or a consonant. If you hit a non-alphabetic symbol, just stop processing.

The input format:

One line with N characters. Alphabetic symbols will be from English alphabet.

The output format:

Print "vowel" if the character is a vowel, and "consonant" if the character is consonant. Stop printing information at the first non-alphabetic symbol.

Sample Input 1:

somegibberish
Sample Output 1:

consonant
vowel
consonant
vowel
consonant
vowel
consonant
consonant
vowel
consonant
vowel
consonant
consonant
Sample Input 2:

normal phrase
Sample Output 2:

consonant
vowel
consonant
consonant
vowel
consonant
Sample Input 3:

weusedtowritewithnospaces
Sample Output 3:

consonant
vowel
vowel
consonant
vowel
consonant
consonant
vowel
consonant
consonant
vowel
consonant
vowel
consonant
vowel
consonant
consonant
consonant
vowel
consonant
consonant
vowel
consonant
vowel
consonant
'''
user_input = input()
vowel = "aeiou"
consonant = "bcdfghjklmnpqrstvwxyz"

for char in user_input:
    if char in vowel:
        print("vowel")
    elif char in consonant:
        print("consonant")
    else:
        break

'''
Loop control statements → Game over

In online test games, there is usually a limited number of lives: if, for example, you make 3 mistakes, you lose and do not continue with the game. Imagine you are trying to implement that system to an existing online test that doesn't have it yet.

The input format:

A line with N scores of a user in a test game separated by a space: C for the correct answer and I for the incorrect answer. N will be between 15 and 50.

The output format:

If the user loses the game, print "Game over" and their score (how many correct answers they gave). If the user wins, print "You won"  and their score. The message should be printed without quotation marks. The message and the score should be printed on separate lines.

Sample Input 1:

C C C I C C C C I I C C C C C C C C C
Sample Output 1:

Game over
7
Sample Input 2:

C C I I C C C C C C C C C C C
Sample Output 2:

You won
13
'''
scores = input().split()
# put your python code here
correct_score = 0
incorrect_score = 0
for score in scores:
    if incorrect_score == 3:
        break
    if score == "C":
        correct_score += 1
    if score == "I":
        incorrect_score += 1
if incorrect_score == 3:
    print("Game over")
else:
    print("You won")
print(correct_score)

'''
Loop control statements → Party time

James is hosting a party today. He decided to welcome all new guests personally. To remember their names, James kindly asks you to write them in a list. Read the names from the input, each on a new line, and stop at a single period . that denotes the end of the sequence.

Print your list and its length (the number of guests) for James.

Sample Input 1:

Katja
Adam
Eva
Nicholas
.
Sample Output 1:

['Katja', 'Adam', 'Eva', 'Nicholas']
4
'''
user_input = input()
names_list = []
while user_input != ".":
    names_list.append(user_input)
    user_input = input()
print(names_list)
print(len(names_list))

'''
Loop control statements → The mean

Calculate the arithmetic mean of integer numbers. You will receive the integers on separate lines. The numeric sequence ends with a period ., so stop reading the input on it.

There will always be at least one number.
'''
user_input = input()
names_list = []
while user_input != ".":
    names_list.append(int(user_input))
    user_input = input()
print(sum(names_list) / len(names_list))

'''
Loop control statements → Cat cafés

Kitty wants to visit a cat café! Help her find the one with the largest number of cats.

Input format

Each string contains a café's name followed by a space and the number of cats in it, e.g. Paws 11, Kittens 9.

The names would be one-word only. Read input lines until you get a string MEOW (without any number).

Output format

The café with the maximum number of cats.

Hint

Sample Input 1:

Paws 11
Kittens 9
MEOW
Sample Output 1:

Paws
'''
user_input = input()
cafe_list = {}
nums_list = []
cafe = ""
num_of_cats = 0

while user_input != "MEOW":
    cafe = user_input.split()[0]
    num_of_cats = int(user_input.split()[1])
    nums_list.append(num_of_cats)
    cafe_list.update({num_of_cats: cafe})
    user_input = input()

print(cafe_list.get(max(nums_list)))


#  Python → Simple programs → Errors 

'''
Errors → Chaos 

Look at the code below and eliminate the chaos: the first line should print the resulting number of the calculation and the second line should print the word mathematics.
'''
print(45 / 9 + 16 * (5 + 8))
print("mathematics")

'''
Errors → English contractions 

Lucy is drawing a poster with English contractions for her students. We will join her English club and help with learning materials.

Print the following strings with contractions:
I am = I'm
I have = I've
I will = I'll
I had / would = I'd

Each string should be on a new line. This will be easy if you use quotes wisely.
'''
print("I am = I'm")
print("I have = I've")
print("I will = I'll")
print("I had / would = I'd")

'''
Errors → Visual poetry 

Just look at this piece of poetry in the shape of an egg! Try to run this code without errors.

Please do NOT edit the strings within print().
'''
print("      *  *  *     ")
print("    *         *   ")
print("  *    Which   *  ")
print(" *  came first: * ")
print("*  the  chicken  *")
print(" *   or   the   * ")
print(" *   egg?   *")
print("     *  *  *     ")

'''
Errors → Locate a problem 

The code snippet below needs debugging. Examine it and write down the line number on which the compilation of code will stop.

print( "The quick brown fox" )  # 1
print()                         # 2
print'jumps')                   # 3
pint()                          # 4
print( ' over the lazy dog  )   # 5
'''
# Python → Collections → List comprehension

'''
List comprehension → Vowels

Read a string from the input and print a list of vowels that belong to that string.

All vowels are enlisted in a variable of the same name.

Sample Input 1:

invertebrate
Sample Output 1:

['i', 'e', 'e', 'a', 'e']
'''
vowels = 'aeiou'
# create your list here
user_input = input()
print([i for i in user_input if i in vowels])

'''
List comprehension → Even numbers

Write a program that takes a list of numbers, creates another list of even numbers from the first list, and prints it.

E.g. if my_numbers = [1, 2, 3, 4, 5], then your ptogram should return the list [2, 4].

NB: the list with numbers my_numbers is already defined, so you don't have to work with the input.
'''
# work with the variable 'my_numbers'
print([i for i in my_numbers if i % 2 == 0])

'''
List comprehension → A list of words

Write a program that takes a list with words, creates a new list of words that start with the letter "a" in the first list, and prints it.

Some words may begin with the capital A! Leave them in their original form in the resulting list.

E.g. if words = ['apple', 'pear', 'banana', 'Ananas'], then your program should return the list ['apple', 'Ananas'].

The list with words is already defined: you can access it using the variable words.
'''
# work with the preset variable `words`
print([x for x in words if x.startswith('a') or x.startswith('A')])

'''
List comprehension → How many days?

The list seconds is a list of numbers that represent seconds. Convert the number of seconds to full days and print the list that contains these values. The number of full days should be an int value.
'''
seconds = [86400, 3600, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
days = [x // 86400 for x in seconds]
print(days)

'''
List comprehension → Length

Given a list of words in the code below, create a list of lengths of those words and print it.
'''
words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
         "apothecary"]
print([len(w) for w in words])

'''
List comprehension → Plus one

You are given a list of strings containing integer numbers. Print the list of their values increased by 1.

E.g. if list_of_strings = ["36", "45", "99"], your program should print the list [37, 46, 100].

The variable list_of_strings is already defined, you don't need to work with the input.
'''
# please work with the variable 'list_of_strings'
print([int(x) + 1 for x in list_of_strings])

# Python → Collections → Nested lists

'''
Nested lists → Fill the blanks

Below you can see the code that chooses some elements from one list and appends them to another:

for a in x:
    for el in a:
        if el > 0:
            els.append(el)
Fill in the blanks in the code below so that list comprehension produces the same result as the code above.
'''
els = [el for a in x for el in a if el > 0]

'''
Nested lists → A lot of nested lists

How to create a nested list [[1, 2], [1, 2], [1, 2], [1, 2], [1, 2]] in one line?
'''
my_list = [[x for x in range(1, 3)] for y in range(5)]
print(my_list)

'''
Nested lists → Accessing elements of a matrix

Let's say we have a matrix M:

M = [[34, 77, 8,  45], 
     [80, 15, 23, 57], 
     [92, 86, 19, 38]]
How to print the element in the first column and the third row?
'''
# the variable M is already defined
print(M[2][0])

'''
Nested lists → Conditions & nested lists

This is a list of students and their grades for an exam: 

students = [["Will", "B"], ["Kate", "B"], ["Max", "A"], ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]
Select only students with the best grade ("A") and print their names in a list. Do all this in one line.
'''
# the list "students" is already defined
print([s[0] for s in students if s[1] == "A"])

'''
Nested lists → Word list

Create a list of words from the text below that are shorter than or equal to the input value. Print the new list.

Sample Input 1:

1
Sample Output 1:

['a', 'a']
'''
text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
user_input = int(input())
print([w for words in text for w in words if len(w) <= user_input])

'''
Nested lists → A very nested list

Write a program that takes three strings as input and then constructs and prints a nested list from them – with first string as a first element, a list containing only second string as a second element and a list containing another list containing a third string as a third element.

Sample Input 1:

cat
dog
dragon
Sample Output 1:

['cat', ['dog'], [['dragon']]]
'''
str_1 = input()
str_2 = input()
str_3 = input()
nest_nest_list = [str_1, [str_2], [[str_3]]]
print(nest_nest_list)

# Python → Data types and operations → Type casting

'''
Type casting → Exactly 100 times

Jane knows that variable n stores some integer number (for example, 12345) and wants to print it exactly 100 times. Help her and write down a single line of code that will print number n exactly 100 times.
'''
n = 12345
# put your python code here
print(str(n) * 100)

'''
Type casting → Lexical reduplication

The languages of the world are amazing! Programming languages too, but now we will talk about the human ones. In linguistics, repeating a word or part of it is called reduplication. This morphological phenomenon is found in different languages. Think for a second, and you will definitely come up with a couple of examples. Just to name a few: knock-knock, so-so, bye-bye.

We have a full reduplication here since the entire word is repeated. That's the mechanism we want you to implement. Print a word exactly 2 times. The spelling rules vary across the globe, so do not separate the halves (that will be easy!).

Sample Input 1:

maru
Sample Output 1:

marumaru
Sample Input 2:

piga
Sample Output 2:

pigapiga
Sample Input 3:

knock
Sample Output 3:

knockknock
'''
word = input()

# Change the next line
print(word * 2)

# Theory: Escape sequences 

'''
Escape sequences → Find the length 

Write a program that will print the length of the string 'That is \n mine'.
'''
print(len('That is \n mine'))

'''
Escape sequences → Good programmer 

You are really good at what you do (programming), so your colleague has decided to congratulate you on the completed project with a message "You are the best programmer!". But how to do this?

Write the code that prints this message using an escape sequence so that each word of the sentence would be on a new line.

Omit the trailing spaces, we can do without them!
'''
print("You\nare\nthe\nbest\nprogrammer!")

'''
Escape sequences → Print a sign 

Print two backslash characters \\.
'''
# put your python code here
print("\\\\")

#  Python → Functions → Scopes 

''' 
Scopes → Cities 

Imagine you've created a program that plays the cities game with a user. For the game to work, you need to remember the user's city and be able to change it. Below is the code that does that, but there's a mistake in it. Find it and fix it!
'''
user_city = "Istanbul"

def change_city(new_user_city):
    global user_city
    user_city = new_user_city

change_city("Paris")
print(user_city)

# Python → Data types and operations → Split and join

'''
Split and join → Prepositional genitive

Advanced input() handling is used to read input directly into several variables, for example:

x, y = input().split()
Use it to print the next message with the two input values: "{x} of {y}"

Sample Input 1:

state Massachusetts
Sample Output 1:

state of Massachusetts
Sample Input 2:

Queen Scots
Sample Output 2:

Queen of Scots
'''
x, y = input().split()
print(x + str(" of ") + y)

'''
Split and join → Straight A's

Write a program that calculates the proportion of students who received grade A.

A five-point rating system with grades A, B, C, D, F is used.

Input format:
A string with students' marks separated by space. At least one mark will be present.

Output format:
A fractional number with exactly two decimal places.

To format the decimal places use the round(number, places) function.

Hint

Sample Input 1:

F B A A B C A D
Sample Output 1:

0.38
Sample Input 2:

B C B
Sample Output 2:

0.0
Sample Input 3:

A D
Sample Output 3:

0.5
'''
# put your python code here
grades = input().split()
total = 0
a_total = 0
for i in grades:
    if i == "A":
        a_total += 1
    total += 1
print(round(a_total / total, 2))

'''
Split and join → Find positions

Write a program that reads a sequence of numbers from the first line and the number x from the second line. Then it should output all positions of x in the numerical sequence.

The position count starts from 0. In case if x is not in the sequence, print the line "not found" (quotes omitted, lowercased).

Positions should be displayed in one line, in ascending order of the value.

Hint

Sample Input 1:

5 8 2 7 8 8 2 4
8
Sample Output 1:

1 4 5
Sample Input 2:

5 8 2 7 8 8 2 4
10
Sample Output 2:

not found
'''
# put your python code here
seq = input().split()
find = input()
indexes = []
counter = 0
for i in seq:
    if i == find:
        indexes.append(str(counter))
    counter += 1
if len(indexes) == 0:
    print("not found")
else:
    print(" ".join(indexes))

'''
Split and join → Spellchecker

Write a spellchecker that tells you which words in the sentence are spelled incorrectly. Use the dictionary in the code below.

The input format:

A sentence. All words are in the lowercase.

The output format:

All incorrectly spelled words in the order of their appearance in the sentence. If all words are spelled correctly, print OK.

Sample Input 1:

srutinize is to examene closely and minutely
Sample Output 1:

srutinize
examene
Sample Input 2:

all correct
Sample Output 2:

OK
'''

dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
seq = input().split()
incorrect = []
for word in seq:
    if word not in dictionary:
        incorrect.append(word)
if len(incorrect) == 0:
    print("OK")
else:
    for w in incorrect:
        print(w)

'''
Split and join → Find words

Find all words that end in "s" and print them together separated by an underscore. 

Sample Input 1:

First ladies rule the State and state the rule: ladies first
Sample Output 1:

ladies_ladies
'''
seq = input().split()
to_print = []

for word in seq:
    if word.endswith("s"):
        to_print.append(word)

print("_".join(to_print))

'''
Split and join → String tricks

Examine the code and fix the mistakes so that the join() method works.
'''
random_numbers = [1, 22, 333, 4444, 55555]
str_numbers = [str(n) for n in random_numbers]
print("\n".join(str_numbers))

'''
Split and join → Fix the mistakes

The code below is supposed to find all website addresses (https://, http://, www.) in the input text. However, it is not finished and there are several mistakes in the code. Find the mistakes, fix them and return all addresses in the chronological order each on a new line.

Sample Input 1:

WWW.GOOGLE.COM uses 100-percent renewable energy sources and www.ecosia.com plants a tree for every 45 searches!
Sample Output 1:

WWW.GOOGLE.COM
www.ecosia.com
'''
text = input()
words = text.split()
for word in words:
    # finish the code here
    if word.lower().startswith("www.") \
            or word.lower().startswith("https://") \
            or word.lower().startswith("http://"):
        print(word)

# Python → Builtins → Any and all

'''
Any and all → Heads or Tails

We have tossed a coin 6 times and saved the results in a list called heads_or_tails. The values are integers: 1 stands for a head, while 0 denotes a tail.

Add some code to find out whether the list has any heads.
'''
# Fingers crossed
check = any(heads_or_tails)

'''
Any and all → Lottery

Imagine that you have bought a bunch of lottery tickets and wrote down their numbers into the list. Now, it's time to figure out whether you have a winning ticket.

You know that all winning tickets are no less than 44. Fill the empty fields in the code (these ones ...) to check if you have at least one winning ticket.

You DON'T need to print the answer.
'''
# As luck would have it
tickets = [11, 22, 33, 44, 55]
winning_tickets = [i >= 44 for i in tickets]
tickets_bool = any(winning_tickets)

'''
Any and all → Competition

Today you are taking part in the chess competition. The winner of the competition will get the 'winner' status and the largest amount of money if they win all the games. Much is at stake!

The results are stored in a list. Fill the blanks in the code below and figure out how much money you won.

You DON'T need to print the answer.
'''
check = any([True, True, 1, 1, True])

if check:
    status = 'winner'
else:
    status = 'looser'

if status == 'winner':
    winning_sum = 100
else:
    winning_sum = 10

# Python → Object-oriented programming → Class

'''
Class → The Creator

Imagine for a second that you're a God and create a class Human. Humans are a species called "Homo Sapiens" and they (usually) have 2 legs and 2 arms. Create the attributes species, n_legs, and n_arms for your class Human.
'''
# create a Human here
class Human:
    species = "Homo Sapiens"
    n_legs = 2
    n_arms = 2

'''
Class → The housing problem

The code below defines the class House and an object of that class. However, the code is somewhat incorrect. Fix the mistakes.
'''
class House:
    construction = "building"
    elevator = True


h = House()

'''
Class → Who is who

There are two classes: Angel and Demon.

They have certain characteristics that help tell them apart. Both of these classes have 3 common class attributes with different values:

class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"
        
        
class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"
Suppose there is a mysterious object called mystery_entity. Print its attributes to find out whether this entity is an angel or a demon. You should print the attributes in this order: color, feature, home. Each should be on a separate line.
'''
# mystery_entity has already been defined
# print its class attributes
print(mystery_entity.color)
print(mystery_entity.feature)
print(mystery_entity.home)

'''
Class → Let's rock

There are many bands in the world that perform all kinds of music. Let's suppose for a second that you're a fan of rock and want to create a program that deals with rock bands.

For that, you obviously need the class RockBand with such attributes as genre ("rock"), n_members(4, by default) and famous_songs (an empty list as a default value). Create this class and an object of that class: name the variable after any rock band that you like. 

You do NOT need to fill the famous_songs attribute, leave the default value.

Print the attributes of your rock band on separate lines in this order: genre, n_members, famous_songs.
'''
# start a RockBand here
class RockBand:
    genre = "rock"
    n_members = 4
    famous_songs = []

r = RockBand()
print(r.genre)
print(r.n_members)
print(r.famous_songs)


