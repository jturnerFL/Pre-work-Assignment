# Question 1

import numbers


def hello_name(user_name):
    print("hello_USERNAME!")

hello_name("USERNAME!")

# Question 2

def first_odds():
    negative_numbers = list(range(1,100,2))
    print(negative_numbers)

first_odds()

# Question 3

def max_num_in_list(a_list):
    max = 0
    for item in a_list:
        if item > max:
            max = item
    return max

list = [1,2,3,4,5,6,7,8,9,10]

maxlist = max(list)
print (maxlist)

# Question 4

def is_leap_year(a_year):
  if a_year %4 == 0:
    if a_year%100 == 0 and a_year%400 == 0:
        return True
    elif a_year%100 == 0:
        return False
    else:
        return True

  return False
     
print(is_leap_year(1500))

# Question 5

def is_consecutive(a_list):
# Returns True if all numbers in list can be ordered consecutively, and false otherwise
    if len(set(a_list)) == len(a_list) and max(a_list) - min(a_list) == len(a_list) - 1:
        return True
    else: 
        return False

# Driver Code
a_list = int(input("Enter numbers to be checked"))
if (is_consecutive(a_list)):
    print("True")
else:
    print("False")