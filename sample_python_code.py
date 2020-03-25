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
