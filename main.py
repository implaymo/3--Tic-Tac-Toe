board = ["_|_|_"]

loop_counter = 1

while loop_counter < 3:
    loop_counter += 1
    print(*board)
    if loop_counter == 3:
        print(" | | ")
