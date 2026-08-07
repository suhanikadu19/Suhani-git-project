# README

## Program Title

**Python Program to Check Whether a Given Number is an Armstrong Number**

## Objective

To write a Python program that checks whether a given number is an Armstrong number.

## Description

An **Armstrong number** is a number that is equal to the sum of its own digits, where each digit is raised to the power of the total number of digits.

For example:

* **153** = (1^3 + 5^3 + 3^3 = 153)
* **370** = (3^3 + 7^3 + 0^3 = 370)

The program:

1. Accepts an integer from the user.
2. Counts the number of digits in the number.
3. Extracts each digit using the modulo (`%`) operator.
4. Raises each digit to the power of the total number of digits and adds the result.
5. Compares the calculated sum with the original number.
6. Displays whether the number is an Armstrong number or not.

## Algorithm

1. Start.
2. Read the input number.
3. Store the original number in a temporary variable.
4. Count the total number of digits.
5. Initialize the sum to 0.
6. Extract each digit using `% 10`.
7. Add the digit raised to the power of the total number of digits to the sum.
8. Remove the last digit using integer division (`// 10`).
9. Repeat until all digits are processed.
10. Compare the calculated sum with the original number.
11. Print the result.
12. Stop.

## Input

An integer entered by the user.

## Output

Displays whether the entered number is an Armstrong number or not.

## Example

**Input:**

```
153
```

**Output:**

```
153 is an Armstrong number
```
