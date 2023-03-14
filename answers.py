
#Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below #

def hello_name(username):
 print ("Hello, " + username.title() + "!" )
hello_username="Hello, Elliot!"
hello_name('Elliot')

def get_user(username):
 print("Hello, " + username.title() +"!")

 get_user("Elliot")

 def hello_name(user_name):
  """a function to print hello_USERNAME"""
  print("hello, " + user_name.title()+"!")


# Question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing #

def first_odds():
 number = 1
 while number < 101 :
  if number %2 == 1 :
   print(number)
   number += 1

   def odd_number():
    num = list(range(1, 101))
    for no in num:
     if no % 2 != 0:
      print(no)

    odd_number()

print("Odd numbers 1-100:")
for x in range(1, 100+1):
 if x % 2 == 1:
  print(x)

  def first_odds():
   for num in range (1, 101, 2):
     print(num)


#Question 3 #Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.#

def max_num_in_list(a_list):
    maximum = max(a_list)
    #this function would still work without the variable declaration#
    print("The maximum number in a_list is ", maximum)

    
my_list = [1, 3, 53, 6, 7, 4, 24]
max_num_in_list(my_list)

def max_num_in_list(a_list):
 a_list.sort()
 return a_list[-1]


#Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).#
def is_leap_year(year):
    """Returns True if the given year is a leap year, False otherwise."""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.#
      
        def are_consecutive_numbers(lst):
    #Returns True if all numbers in the list are consecutive, False otherwise.#
          n = len(lst)
    if n <= 1:
        return True
    diff = lst[1] - lst[0]
    for i in range(1, n):
        if lst[i] - lst[i-1] != diff:
            return False
    return True

