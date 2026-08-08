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
# README

## Program Title

**Python Program to Find the Sum of the First N Natural Numbers**

## Objective

To write a Python program that calculates the sum of the first **N** natural numbers.

## Description

This program accepts a positive integer **N** from the user and calculates the sum of all natural numbers from **1** to **N** using a `for` loop. The calculated sum is then displayed on the screen.

## Algorithm

1. Start.
2. Read the value of **N** from the user.
3. Initialize `sum` to 0.
4. Use a `for` loop from 1 to **N**.
5. Add each number to `sum`.
6. Display the final sum.
7. Stop.

## Input

An integer **N** entered by the user.

## Output

The sum of the first **N** natural numbers.

## Example

**Input:**

```text
Enter a number: 10
```

**Output:**

```text
Sum of first numbers: 55
```

## Conclusion

The program successfully computes and displays the sum of the first **N** natural numbers using a `for` loop.
# README

## Program Title

**Python Program to Count the Number of Digits in a Given Integer**

## Objective

To write a Python program that counts the number of digits in a given integer.

## Description

This program accepts an integer from the user and counts the total number of digits in it using a `while` loop. In each iteration, the last digit is removed using integer division (`// 10`), and a counter is incremented until the number becomes 0. Finally, the total digit count is displayed.

## Algorithm

1. Start.
2. Read an integer from the user.
3. Initialize `count` to 0.
4. Repeat while the number is greater than 0:

   * Increment `count` by 1.
   * Remove the last digit using `num = num // 10`.
5. Display the value of `count`.
6. Stop.

## Input

An integer entered by the user.

## Output

The total number of digits in the given integer.

## Example

**Input:**

```text
Enter a number: 12345
```

**Output:**

```text
Number of digit count: 5
```

## Conclusion

The program successfully counts and displays the total number of digits in the given integer using a `while` loop.
# Calculate Sum and Average of Numbers

## 📌 Description

This Python program calculates the **total sum** and **average** of a list of numbers.

## 🧮 Input

The program uses the following list:

```python
numbers = [10, 20, 30, 40, 50]
```

## ⚙️ How It Works

1. The `sum()` function calculates the total of all numbers.
2. The `len()` function counts the number of elements.
3. The average is calculated by dividing the total sum by the number of elements.
4. The results are displayed using `print()`.

## 💻 Code

```python
numbers = [10, 20, 30, 40, 50]

total_sum = sum(numbers)
average = total_sum / len(numbers)

print("Total Sum:", total_sum)
print("Average:", average)
```

## 📤 Output

```text
Total Sum: 150
Average: 30.0
```

## 🎯 Concepts Used

* Python Lists
* `sum()` function
* `len()` function
* Arithmetic operations
* `print()` function

## ▶️ How to Run

1. Install Python.
2. Save the code as `main.py`.
3. Open the terminal.
4. Run:

```bash
python main.py
```

