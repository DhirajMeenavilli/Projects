def isValidSudoku(self, board: [[str]]) -> bool: #So far can do columns and rows but boxes are a bit more weird. Boxes stayed weird, but beats 90% of people in memory (2/10 MB, but 10 ms slower eh)

    box_col_fix = 0
    box_row_fix = 0
    print(board[2][1])
    for k in range(3):
        for i in range(len(board)):
            
            column = {}
            row = {}
            box = {}

            box_row = box_row_fix
            box_col = box_col_fix


            for j in range(len(board[i])):
                
                if k == 0:

                    if board[i][j] != ".":
                        if board[i][j] in column:
                            return False

                        else:
                            column[board[i][j]] = 1
                    
                    if board[j][i] != ".":
                        if board[j][i] in row:
                            return False 
                        
                        else:
                            row[board[j][i]] = 1
                
                if board[box_row][box_col] != ".":

                    if board[box_row][box_col] in box:
                        return False
                    
                    else:
                        box[board[box_row][box_col]] = 1

                if (j+1) % 3 != 0:
                    box_col += 1

                else:
                    box_row += 1
                    box_col = box_col_fix

            if (i+1) % 3 == 0:
                box_col_fix += 3

        box_row_fix += 3
        box_col_fix = 0

    return True