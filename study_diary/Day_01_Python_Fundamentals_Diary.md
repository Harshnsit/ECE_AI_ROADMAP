# AI/ML Roadmap - Daily Study Diary

## Day 1 - Python Fundamentals
**Date:** 13 September 2026  
**Stage:** Stage 1 - Python Programming from Absolute Zero  
**Session status:** Completed for today  
**Current position:** Control flow / loops completed; next major topic is functions.

## Learning objectives completed
- Understand what a program is and what Python source code represents.
- Understand basic Python syntax and how `python hello.py` executes a file.
- Use `print()` to display values.
- Understand strings, integers, floating-point numbers, and Boolean values.
- Understand variables, assignment, reassignment, and expressions.
- Use arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`.
- Use `input()` and convert user input with `int()`, `float()`, and `str()`.
- Distinguish `SyntaxError`, `TypeError`, and `ValueError` at a basic level.
- Use comparison operators and Boolean logic: `and`, `or`, `not`.
- Build decisions with `if`, `elif`, `else`, including nested conditions.
- Build repetition with `while` and `for` loops.
- Use lists, list indexes, `range()`, `break`, and `continue`.
- Apply control flow to small analog/engineering examples.

## Core concepts learned

### 1. Program, Python, source code, syntax
A program is a set of instructions for a computer. Python is a high-level programming language. A `.py` file contains Python source code. Syntax is the set of rules that determine how Python code must be written.

Running:

```powershell
python hello.py
```

means the Python interpreter is asked to execute the source code in `hello.py`.

### 2. `print()` and strings
`print()` is a built-in Python function used to display a value.

```python
print("Hello")
```

`"Hello"` is a string. Quotation marks tell Python to treat the contents as text.

### 3. Numeric data types
- `int` - integer / whole number, e.g. `15`
- `float` - floating-point number, e.g. `15.5`
- `str` - string / text, e.g. `"15"`
- `bool` - Boolean value, `True` or `False`

Important distinction:

```python
15     # int
"15"   # str
15.0   # float
```

### 4. Variables and assignment
A variable is a name associated with a value. The `=` symbol is the assignment operator.

```python
voltage = 12
resistance = 1000
current = voltage / resistance
```

A useful mental model:

```text
voltage -> 12
resistance -> 1000
current -> 0.012
```

`=` is not mathematical equality. It performs an assignment.

### 5. Reassignment
A variable can be assigned a new value.

```python
voltage = 12
voltage = 24
```

After the second line, `voltage` refers to `24`.

Important: changing another variable does not automatically recalculate a previous result.

```python
resistance = 1000
current = 12 / resistance
resistance = 2000
print(current)   # still 0.012
```

Python evaluated `12 / resistance` when `current` was assigned.

### 6. Expressions
An expression is a piece of Python code that can be evaluated to produce a value.

Examples:

```python
5 + 3
12 / resistance
voltage * current
```

In:

```python
power = voltage * current
```

`voltage * current` is the expression; the result is assigned to `power`.

## Arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | addition | `5 + 3` | `8` |
| `-` | subtraction | `5 - 3` | `2` |
| `*` | multiplication | `5 * 3` | `15` |
| `/` | true division | `5 / 2` | `2.5` |
| `//` | floor division | `17 // 5` | `3` |
| `%` | remainder / modulo | `17 % 5` | `2` |

Engineering examples used:

```python
current = voltage / resistance
power = voltage * current
```

## Input and type conversion
`input()` returns user input as a string.

```python
voltage = input("Enter the voltage value: ")
```

If the user types `24`, the initial value is conceptually:

```text
"24"
```

Type conversion can change the type:

```python
voltage = int(voltage)
voltage = float(voltage)
text_value = str(number)
```

Useful conversions:

```text
"25"   -> int("25")   -> 25
"25"   -> float("25") -> 25.0
25     -> str(25)      -> "25"
```

Important failure learned:

```python
int("25.7")
```

produces `ValueError` because the string does not represent a whole integer in a form accepted by `int()`.

## Error vocabulary learned

- **SyntaxError** - Python cannot understand the code's structure/syntax.
- **TypeError** - the operation is not valid for the involved types.
- **ValueError** - the type is generally acceptable, but the particular value is not accepted for that operation.

Example:

```python
voltage = "15"
current = voltage / 3000
```

The syntax is valid, but dividing a string by an integer causes a `TypeError`.

## Comparison operators

| Operator | Meaning |
|---|---|
| `>` | greater than |
| `<` | less than |
| `>=` | greater than or equal to |
| `<=` | less than or equal to |
| `==` | equal to |
| `!=` | not equal to |

Important distinction:

```python
voltage = 12   # assignment
voltage == 12  # comparison
```

## Boolean logic

Boolean values are `True` and `False`.

| Operator | Meaning |
|---|---|
| `and` | both conditions must be true |
| `or` | at least one condition must be true |
| `not` | reverses True/False |

Example:

```python
voltage <= 20 and voltage >= 10
```

This is true only when both comparisons are true.

## Decision making: `if`, `elif`, `else`

Basic pattern:

```python
if condition:
    # execute if condition is True
elif another_condition:
    # execute if the elif condition is True
else:
    # execute when the previous conditions are False
```

Indentation is part of Python syntax and identifies the code belonging to the block.

Engineering example completed:

```python
voltage = float(input("Enter the voltage value: "))
max_voltage = 20

if voltage > max_voltage:
    print("Voltage too high")
else:
    print("Voltage is within safe limit")
```

Three-way classification was also built with `elif`.

## Nested decisions
A decision can contain another decision:

```python
if voltage <= 20:
    if current <= 3:
        print("Safe")
```

This means the second condition is checked only if the first condition passes.

## `while` loops
A `while` loop repeats while its condition is true.

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

Key loop components:
1. starting value
2. condition
3. update

The update is important because it prevents an unintended infinite loop.

## `for` loops
A `for` loop iterates through items in a collection.

```python
voltages = [10, 12, 14, 16, 18]

for voltage in voltages:
    print(voltage)
```

The loop variable (`voltage`) receives each list value one at a time.

## Lists and indexing
A list stores multiple values:

```python
voltages = [8, 12, 17, 23, 19]
```

Indexes start at 0:

```text
index:  0   1   2   3   4
value:  8  12  17  23  19
```

So:

```python
voltages[3]
```

returns `23`.

`voltages[5]` would cause an `IndexError` because index 5 does not exist.

## `range()`
`range()` generates a sequence of numbers.

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```text
range(5)        -> 0, 1, 2, 3, 4
range(2, 5)     -> 2, 3, 4
range(0, 11, 2) -> 0, 2, 4, 6, 8, 10
```

The `stop` value is excluded.

## `break` and `continue`

`break` stops the loop entirely.

```python
for current in currents:
    if current > 3:
        print("FAULT")
        break
```

`continue` skips the rest of the current iteration and moves to the next item.

```python
for current in currents:
    if current > 3:
        continue
    print(current)
```

## Engineering mini-projects built today

### 1. Ohm's-law calculator
User enters voltage and resistance; program calculates current.

### 2. Power calculator
Program calculates `power = voltage * current` and compares it with a reference power.

### 3. Voltage safety checker
Program classifies voltage as high, low, or normal.

### 4. Device operating-condition checker
Program checks voltage/current limits with Boolean logic.

### 5. Measurement scanner
A list of voltage/current measurements is scanned with `for`, conditions, and `break`.

## Common mistakes made today - and the lesson

1. **Confusing `cd` and `mkdir`**  
   `cd` changes directory; `mkdir` creates a directory.

2. **Confusing `TypeError` with `SyntaxError`**  
   Invalid operation for the types can still be syntactically valid code.

3. **Assuming `current` automatically changes when `resistance` changes**  
   Python does not create a live mathematical dependency when an assignment is executed.

4. **Forgetting that `input()` returns a string**  
   Convert it before numeric calculations.

5. **Missing the post-loop variable value**  
   The last value printed can differ from the final variable value after the update.

6. **Introducing `//` before learning it**  
   This was corrected by explicitly teaching floor division before testing it.

7. **Using the wrong test data in the current-monitor challenge**  
   The logic was correct, but the list accidentally contained voltage data. This reinforced that correct logic + wrong input is still a program bug.

## Mastery status

### Passed today
- Variables and assignment
- Numeric and string types
- Type conversion
- Expressions and arithmetic
- Input handling
- Comparison operators
- Boolean logic
- `if / elif / else`
- Nested decisions
- `while` loops
- `for` loops
- Lists and indexing
- `range()`
- `break` and `continue`
- Basic engineering control-flow programs

### Next major topic
**Functions**

## Homework - Engineering Current Monitor
Use this data:

```python
currents = [0.4, 0.9, 1.8, 2.5, 3.2, 0.7, 4.1]
```

Rules:
- `current < 1` -> `LOW`
- `1 <= current <= 3` -> `NORMAL`
- `3 < current < 4` -> `HIGH`
- `current >= 4` -> `FAULT` and stop immediately

Requirements:
- Use a `for` loop.
- Use conditional statements.
- Do not copy a complete solution from AI.
- Put the finished solution in the repository before moving on.

## Tomorrow's protocol
1. Start with a short recall test on today's material.
2. Review homework.
3. Only advance after the recall/mastery gate is passed.
4. Begin functions at a faster pace, while still explaining every code element.

## Resume From Here
**Stage 1 - Python Fundamentals**  
**Completed:** variables, types, operators, input, Boolean logic, decisions, loops  
**Pending:** homework review + functions  
**GitHub project:** `ECE_AI_ROADMAP`  
**Next lesson:** Functions from first principles
