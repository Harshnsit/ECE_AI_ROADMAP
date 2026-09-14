# Day 2 Study Diary - Python Functions, Lists, Comprehensions & Dictionaries

## Date
2026-09-14

## Recall Gate
Day 1 recall: 6/6 correct. Day 1 Engineering Current Monitor homework: completed correctly.

## Topics Actually Learned
- Function definition and function calls
- Parameters vs arguments
- `return` vs `print`
- Local scope
- Default parameters
- Positional vs keyword arguments
- Multiple return values / tuple unpacking
- Boolean-returning functions
- Passing lists into functions
- `len()` and `range(len(...))`
- Indexing and in-place list modification
- Mutable vs immutable objects
- Creating new lists while preserving raw data
- List comprehensions and conditional filtering
- Dictionaries, key-value pairs, nested dictionaries, `.items()`
- Combining functions + dictionaries + measurements for device validation

## Actual Code and Results

### Interactive resistance calculator
```python
def calculate_resistance(voltage, current):
    return voltage / current

voltage_input = float(input("Please enter your measured voltage: "))
current_input = float(input("Please enter your measured current: "))
calculated_res = calculate_resistance(voltage_input, current_input)
print(calculated_res)
```
Tests: 12/2 -> 6.0, 24/3 -> 8.0, 5/0.5 -> 10.0.
Feedback: strong independent extension; later add division-by-zero handling.

### Current classifier
```python
def classify_current(current):
    if current < 1:
        return "LOW"
    elif 1 <= current <= 3:
        return "NORMAL"
    elif 3 < current < 4:
        return "HIGH"
    else:
        return "FAULT"

current_data = [0.5, 2.0, 3.5, 4.2]
for current in current_data:
    print(classify_current(current))
```
Output: LOW, NORMAL, HIGH, FAULT.

### Measurement analysis
```python
def analyze_measurement(voltage, current):
    power = voltage * current
    resistance = voltage / current
    return power, resistance

power, resistance = analyze_measurement(12, 2)
print(power)
print(resistance)
```
Output: 24 and 6.0.

### Max-voltage function
Initial attempt reset the tracking variable inside the loop. Corrected by moving initialization outside:
```python
def find_max_voltage(voltages):
    present_int = voltages[0]
    for voltage in voltages:
        if voltage > present_int:
            present_int = voltage
    return present_int

voltages = [12, 18, 15, 21, 17]
print(find_max_voltage(voltages))
```
Correct output: 21.
Feedback: use a clearer name such as `max_voltage`.

### In-place voltage adjustment
```python
def voltage_add(voltages):
    for i in range(len(voltages)):
        voltages[i] = voltages[i] + 2

voltages = [10, 12, 14, 16]
voltage_add(voltages)
print(voltages)
```
Output: [12, 14, 16, 18].

### Gain processing
```python
def apply_gain(measurements, gain):
    for i in range(len(measurements)):
        measurements[i] = measurements[i] * gain

measurements = [1.0, 2.0, 3.0, 4.0]
gain = 2.5
apply_gain(measurements, gain)
print(measurements)
```
Output: [2.5, 5.0, 7.5, 10.0].

### New processed list
The learner independently used list comprehension:
```python
def apply_offset(measurements, offset):
    processed = [measurement + offset for measurement in measurements]
    return processed

measurements = [10.0, 12.5, 15.0, 17.5]
offset = 0.5
processed_measurements = apply_offset(measurements, offset)
print(measurements)
print(processed_measurements)
```
Output: raw list unchanged; processed list [10.5, 13.0, 15.5, 18.0].
Feedback: good instinct to preserve raw measurements.

### Conditional list comprehension
```python
def current_3(currents):
    processed = [current for current in currents if current <= 3]
    return processed

currents = [0.5, 1.2, 2.5, 3.1, 4.0]
processed = current_3(currents)
print(currents)
print(processed)
```
Output: original list unchanged; processed [0.5, 1.2, 2.5].
Feedback: code works; function name could be more descriptive.

### Device data
```python
device = {
    "part_number": "LMG2107",
    "max_voltage": 100,
    "max_current": 4
}
```

### Nested device data
```python
device = {
    "part_number": "LMG2107",
    "electrical": {
        "max_voltage": 100,
        "max_current": 4
    }
}
```

### Dictionary iteration
```python
specs = {
    "max_voltage": 100,
    "max_current": 4,
    "max_temperature": 150
}

for name, value in specs.items():
    print(name, value)
```

### Final device checker
```python
def check_device(device, measurements):
    if device["max_voltage"] > measurements["voltage"]:
        print("VOLTAGE_OK")
    elif device["max_voltage"] < measurements["voltage"]:
        print("VOLTAGE FAULT")
    if device["max_current"] > measurements["current"]:
        print("CURRENT_OK")
    else:
        print("CURRENT FAULT")

device = {
    "part_number": "LMG2107",
    "max_voltage": 100,
    "max_current": 4
}

measurements = {
    "voltage": 85,
    "current": 3.2
}

check_device(device, measurements)
```
Output: VOLTAGE_OK, CURRENT_OK.
Feedback: tested case works. Boundary case at exactly 100 V needs fixing later.

## Key Conceptual Learnings
- Functions separate reusable logic from the code that calls them.
- `return` is for producing a result for the caller; `print` is for display.
- Lists are mutable; integers and strings are immutable.
- A state variable used to track a maximum must be initialized before the loop.
- List comprehensions build new lists compactly and can include conditions.
- Dictionaries are natural structures for device specifications and later JSON/LLM data.
- Nested dictionaries organize related specification groups.

## Current Weaknesses
- Edge-case validation (equality limits; division by zero).
- Scope/mutability should be reinforced.
- Naming clarity should improve.

## GitHub
Keep:
- `Daily_Code_Book/Day_2_functions.py`
- `study_diary/Day_02_Python_Functions_Diary.md`
- `study_diary/Day_02_Python_Functions_and_Data_Revision_Book.pdf`
- updated `progress.md`

## Resume From Here
Next session starts with a Day 2 recall test, then robust error/input handling and further Python software-engineering foundations.
