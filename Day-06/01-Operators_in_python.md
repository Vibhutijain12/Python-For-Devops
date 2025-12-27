## Arithmetic Operations in Python

#### Introduction
Arithmetic operators in Python allow you to perform basic mathematical calculations on numeric values. These operators include addition, subtraction, multiplication, division, and more.

#### List of Arithmetic Operators
**Addition (+)**: Adds two numbers.

**Subtraction (-)**: Subtracts the right operand from the left operand.

**Multiplication (*)**: Multiplies two numbers.

**Division (/)**: Divides the left operand by the right operand (results in a floating-point number).

**Floor Division (//)**: Divides the left operand by the right operand and rounds down to the nearest whole number.

**Modulus (%)**: Returns the remainder of the division of the left operand by the right operand.
Exponentiation ():** Raises the left operand to the power of the right operand.

Examples: 
```python
# Addition
a = 5
b = 3
result = a + b
print(result)  # Output: 8
```

```python
# Subtraction
x = 10
y = 7
result = x - y
print(result)  # Output: 3
```

## Assignment Operations in Python

#### Introduction
Assignment operators in Python are used to assign values to variables. They include the basic assignment operator (=) and various compound assignment operators that perform an operation on the variable while assigning a value.

#### List of Assignment Operators

* Basic Assignment (=): Assigns a value to a variable.

* Addition Assignment (+=): Adds the right operand to the left operand and assigns the result to the left operand.

* Subtraction Assignment (-=): Subtracts the right operand from the left operand and assigns the result to the left operand.

* Multiplication Assignment (*=): Multiplies the left operand by the right operand and assigns the result to the left operand.

* Division Assignment (/=): Divides the left operand by the right operand and assigns the result to the left operand.

* Floor Division Assignment (//=): Performs floor division on the left operand and assigns the result to the left operand.

* Modulus Assignment (%=): Calculates the modulus of the left operand and assigns the result to the left operand.

* Exponentiation Assignment (=):** Raises the left operand to the power of the right operand and assigns the result to the left operand.

Examples:

```python 
# Basic Assignment
x = 5
# Addition Assignment
y = 10
y += 3  # Equivalent to y = y + 3
```

## Identity Operations in Python

#### Introduction

Identity operators in Python are used to compare the memory locations of two objects to determine if they are the same object or not. The two identity operators are "is" and "is not."

#### List of Identity Operators

**is**: Returns True if both operands refer to the same object.

**is not**: Returns True if both operands refer to different objects.

Examples:

#### is Operator
```python
x = [1, 2, 3]
y = x  # y now refers to the same object as x
result = x is y
# result will be True
```

#### is not Operator
```python
a = "hello"
b = "world"
result = a is not b
# result will be True
```

## Logical Operations in Python

#### Introduction

Logical operators in Python are used to manipulate and combine Boolean values. These operators allow you to perform logical operations such as AND, OR, and NOT.

#### List of Logical Operators

**AND (and)**: Returns True if both operands are True.

**OR (or)**: Returns True if at least one of the operands is True.

**NOT (not)**: Returns the opposite Boolean value of the operand.

Examples: 

#### AND Operator
```python
x = True
y = False
result = x and y
# result will be False
```

#### OR Operator
```python
a = True
b = False
result = a or b
# result will be True
```
