currents = [0.4, 0.9, 1.8, 2.5, 3.2, 0.7, 4.1]
for current in currents:
    if current < 1:
        print("low")
    elif 1 <= current <= 3:
        print("normal")
    elif 3 < current < 4:
        print("high")
    else:
        print("fault")
        break