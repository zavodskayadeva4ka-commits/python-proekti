import random
choices = ["камень", "ножницы", "бумага"]
player_score = 0
computer_score = 0

computer_choice = random.choice(choices)
player_choice = input("Твой ход (камень / ножницы / бумага): ").lower().strip()

print(f"Ты: {player_choice} | Компьютер: {computer_choice}")

if player_choice == computer_choice:
    print("Ничья!")
elif (
    (player_choice == "камень" and computer_choice == "ножницы") or
    (player_choice == "ножницы" and computer_choice == "бумага") or
    (player_choice == "бумага" and computer_choice == "камень")
):
    print("Ты победил!")
    player_score += 1
else:
    print("Компьютер победил((")
    computer_score += 1
player_score = 0
computer_score = 0

if player_choice == computer_choice:
    print(f"Ничья! Оба выбрали {player_choice}.")
elif (player_choice == "камень" and computer_choice == "ножницы") or \
     (player_choice == "ножницы" and computer_choice == "бумага") or \
     (player_choice == "бумага" and computer_choice == "камень"):
    print(f"Ты победил! {player_choice} бьёт {computer_choice}.")
    player_score += 1
else:
    print(f"Компьютер победил! {computer_choice} бьёт {player_choice}.")
    computer_score += 1

print(f"Счёт — ты: {player_score}, компьютер: {computer_score}")