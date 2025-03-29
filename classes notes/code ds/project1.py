board = [["","",""],["","",""],["","",""]]
player = "X"
status = False
count = 0




for i in range(100):
    print(f"{player}, This is your chance. ")
    row = int(input("Enter the row index i.e 0,1,2 : "))
    col = int(input("Enter the Column index i.e 0,1,2 : "))
   
    if board[row][col] == "":
        board[row][col] = player
        count +=1
    else:
        print("Ops, this cell is not empty")
        continue

    for i in range(3):
        # print('-'*6)
        # print("|".join(board[i]))
        print(board[i])
    

    # Condition for winning

    # Row 
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            print(f" {player}, you won the game ")
            status = True
            break
        elif board[i][0] == board[i][1] == board[i][2] == player:
            print(f" {player}, you won the game ")
            status = True
            break
        elif board[0][0]==board[1][1] == board[2][2] == player or board[0][2]==board[1][1]==board[2][0] == player:
            print(f" {player}, you won the game ")
            status = True
            break
    
    if status:
        break
    elif count == 9:
        print("Game is Over, no one wins")
        break


    if player == "X":
        player = "0"
    else:
        player = "X"
else:
    print("Game is Over")   
    