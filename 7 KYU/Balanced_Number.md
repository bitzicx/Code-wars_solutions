# Description:
 [Link to original Kata](https://www.codewars.com/kata/5a4e3782880385ba68000018/python)<br/>
A balanced number is a number where the sum of digits to the left of the middle digit(s) and the sum of digits to the right of the middle digit(s) are equal.
If the number has an odd number of digits, then there is only one middle digit. (For example, 92645 has one middle digit, 6.) Otherwise, there are two middle digits. (For example, the middle digits of 1301 are 3 and 0.)

The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5.
<br/>The task<br/>
Given a number, find if it is balanced, and return the string "Balanced" or "Not Balanced" accordingly. The passed number will always be positive.<br />
Examples<br/>
7 ==> return "Balanced"<br/>
Explanation:<br/>
middle digit(s): 7 
sum of all digits to the left of the middle digit(s) -> 0<br/>
sum of all digits to the right of the middle digit(s) -> 0<br/>
0 and 0 are equal, so it's balanced.<br/>
295591 ==> return "Not Balanced"<br/>
Explanation:<br/>
middle digit(s): 55<br/>
sum of all digits to the left of the middle digit(s) -> 11<br/>
sum of all digits to the right of the middle digit(s) -> 10<br/>
11 and 10 are not equal, so it's not balanced.<br/>

### Solution 1 using Python
The Solution is pretty simple and straight forward<br/>
```
def balanced_num(number):      
    str_number = str(number)     #converting number to string
    length = len(str_number)     #getting the length of string
    half = length // 2
    
    if length % 2:  # Odd length
        left_side = str_number[:half]
        right_side = str_number[half + 1:]
    else:  # Even length
        left_side = str_number[:half - 1]
        right_side = str_number[half + 1:]

    left_sum = sum(int(x) for x in left_side)      #summing left side using list comprehension
    right_sum = sum(int(x) for x in right_side)      #summing right side using list comprehension

    return 'Balanced' if left_sum == right_sum else "Not Balanced"