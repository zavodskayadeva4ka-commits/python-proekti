import random
secret_number = random.randint(1, 100)
print("Я загадал число от 1 до 100. А ну попробуй угадай!")
guess = int(input("Твой вариант: "))
attempts = 1

while guess != secret_number:
    if guess < secret_number:
        print("Больше!")
    else:
        print("Меньше!")
    guess = int(input("Твой вариант: "))
    attempts += 1

print(f"Угадал! Это число {secret_number}. Попыток: {attempts}")
