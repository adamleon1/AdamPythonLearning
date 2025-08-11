board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
p=1
name= "adam"
while True:
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])
    index = int(input(f'{name} Turn: '))
    if p ==1 and board[index]==" ":
        board[index] = 'X'
        name = 'umair'
        p = 2
    elif p==2 and board[index]==" ":
        board[index] = 'O'
        name='adam'
        p=1
    if board[0] == board[1] == board[2] and board[0]!=" ": break
    if board[3] == board[4] == board[5] and board[3]!=" ": break
    if board[6] == board[7] == board[8] and board[6]!=" ": break
    if board[0] == board[3] == board[6] and board[0]!=" ": break
    if board[1] == board[4] == board[7] and board[1]!=" ": break
    if board[2] == board[5] == board[8] and board[2]!=" ": break
    if board[0] == board[4] == board[8] and board[0]!=" ": break
    if board[2] == board[4] == board[6] and board[2]!=" ": break
    
print('final output')

print(board[0:3])
print(board[3:6])
print(board[6:9])
print(f'{name} won')