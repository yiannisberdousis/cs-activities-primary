import random

number = random.randint(1, 10)
print("Μάντεψε τον αριθμό (1-10)")

guess = 0
while guess != number:
    guess = int(input("Δώσε αριθμό: "))
    if guess < number:
        print("Πιο πάνω!")
    elif guess > number:
        print("Πιο κάτω!")
print("Μπράβο! Βρήκες τον αριθμό.")
