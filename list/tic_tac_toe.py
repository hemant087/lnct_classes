board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
Player = "X"
player_status = False
turns = 9


for i in range(turns):
#taking index
    print(f"{Player} it's your turn:-   ")
    row = int(input("Enter the row (0,1,2): "))
    col = int(input("Enter the column (0,1,2): "))

#checking the shell is empty or not,, if empty assign player
    if board[row][col] == " ":
        board[row][col] = Player
    else:
        turns +=1   #increasing turns, which is get wasted
        print("oops! this cell already exist")
        continue
    for i in range(3):
        print('-'*6)
        print("|".join(board[i]))
# for checking row
    for row in board:
        if row[0] == row[1] ==row[2] == Player:
            print(f"Wow! {Player} you Won ")
            player_status = True
            break
# for checking column    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == Player:
            print(f"Wow! {Player} you Won ")
            player_status = True
            break
# for checking diagonal
    if (board[0][0] == board[1][1] == board[2][2] == Player) or (board[0][2] == board[1][1] == board[2][0] == Player):
        print(f"Wow! {Player} you Won ")
        player_status = True

    if Player == 'X':
        Player = "O"
    else:
        Player ="X"
    
    if player_status:
        break
else:
    print("No one won ,, game draw ")