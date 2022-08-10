player1 = input("Введите имя первого игрока:\n")
player2 = input("Введите имя второго игрока:\n" )
sticks = int(input("Введите кол-во палочек:\n"))
move_number = 0
while not sticks == 0:
    move_1_player1 = input(f"{move_number+1} Ход, Кол-во палочек {sticks}\n {player1}:")

    while int(move_1_player1) > 3:
            print("Кол-во палочек за один ход не более 3")
            move_1_player1 = input(f"{move_number + 1} Ход, Кол-во палочек {sticks}\n {player1}:")
    sticks -= int(move_1_player1)

    if sticks <= 1:
        print(f"Победил игрок: {player1}")
        break
        
    move_number += 1
    move_1_player2 = input(f"{move_number+1} Ход, Кол-во палочек {sticks}\n {player2}:")

    while int(move_1_player2) > 3:
        print("Кол-во палочек за один ход не более 3")
        move_1_player2 = input(f"{move_number + 1} Ход, Кол-во палочек {sticks}\n {player2}:")
    sticks -= int(move_1_player2)
    if sticks <= 1:
        print(f"Победил игрок: {player2}")
        break
    move_number += 1

