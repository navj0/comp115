"""
Lab 6 - Strings and Tuples 
(100 marks in total, including 5 exercises - each 20 marks)

Author: Navjot kaur
Due Date: This Friday (Mar. 1) 11am.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
"""
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

    """

def reverse_str(s):
    reverse=""
    for i in range(len(s)-1,-1,-1):
        reverse+=s[i]
    return reverse


assert reverse_str("abc")=="cba"
assert reverse_str("class")=="ssalc"
assert reverse_str("programm")=="mmargorp"
assert reverse_str("question")=="noitseuq"
assert reverse_str("coding115")=="511gnidoc"



"""
Exercise 2 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
   count=0
   for i in s:
       if i in "AEIOUaeiou":
           count+=1
   return count
        

assert count_vowels("hello")==2
assert count_vowels("operation")==5
assert count_vowels("opera")==3
assert count_vowels ("rhythm")==0
assert count_vowels("editing")==3


"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: We have implemented a function removing duplicates for a list in week 6. Similar.
"""
def remove_duplicates(s):
    """
    This function removes the same characters in the string .

    Example: 
    >>> remove_duplicates("paroot")
    parot

    Parameters:
    - (s): The string that has duplicates and needed to be removed.

    Returns:
    - (duplicate ): The duplicates are reomved from the string s . 


    """

    duplicate=""
    for i in s:
        if i not in duplicate  :
            duplicate+=i
            
    return duplicate


assert remove_duplicates("moon")=="mon"
assert remove_duplicates("zoo")=="zo"
assert remove_duplicates("language")=="langue"
assert remove_duplicates("programming")=="progamin"
assert remove_duplicates("hollow")=="holw"


"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
    This find_index function returns the index value of the string.

    Example:
    >>> find_index("snow","o")==2

    Paramters:
    - (s,t)   : The string value that index needs to be find out .

    Returns:
    - (string) : The string value tell us the index of the character or value.

    """
    for i in range(len(s)):
        if s [i:i+len(t)]==t:
            return i
    return -1

assert find_index ("kite","t")==2
assert find_index ("polygon","g")==4
assert find_index("terminal","n")==5
assert find_index("numbers","b")==3
assert find_index ("cat","e")==-1



"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    This function returns the completion day 

    Example :
    >>> project_completion_day ("Tuesday",4)
    Saturday

    Parameters:
    - (day, days_to_completion): The string that completion day needs to be find out . 

    Returns:
    - (string) : The string returns the estimated completion day. 
    """
    dayz=days_week.index(day)
    completion_day= (dayz + days_to_completion) % 7 
    if completion_day == 0:
        completion_day ==7
    return days_week[completion_day]

assert project_completion_day("Wednesday",6)=="Tuesday"
assert project_completion_day("Tuesday",4)=="Saturday"
assert project_completion_day("Wednesday",10)=="Saturday"
assert project_completion_day("Thursday",1)=="Friday"
assert project_completion_day("Sunday",4)=="Thursday"



"""
Congratulations on finishing your lab6. Hope you feel more confident on function implementation.

Now you just need to upload it to your GitHub repository. That's all.
"""