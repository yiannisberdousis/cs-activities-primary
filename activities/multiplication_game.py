import random

print("Παιχνίδι Προπαίδειας!")
for i in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = int(input(f"{a} x {b} = "))
    if answer == a*b:
        print("Σωστά!")
    else:
        print(f"Λάθος! Η σωστή απάντηση είναι {a*b}")
