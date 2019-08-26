# URL: https://www.geeksforgeeks.org/gold-mine-problem/

def max_gold_in_column(padded_gold_matrix, col_num, row_num = None):
    temp_max_row = 0
    if col_num == 1:
        temp_max_gold = 0
        for i in range(1, m+1):
            if temp_max_gold < padded_gold_matrix[i][1]:
                temp_max_gold = padded_gold_matrix[i][1]
                temp_max_row = i
    else:
        right = padded_gold_matrix[row_num][col_num]
        right_up = padded_gold_matrix[row_num - 1][col_num]
        right_down = padded_gold_matrix[row_num + 1][col_num]
        #print(right_up,right, right_down)

        next_path = max(right, right_down, right_up)
        if next_path == right:
            temp_max_row = row_num
        elif next_path == right_up:
            temp_max_row = row_num - 1
        elif next_path == right_down:
            temp_max_row = row_num + 1
    return temp_max_row

def gold_mine(gold_matrix, m, n):
    gold_collected = 0

    padded_gold_matrix = [[0 for x in range(n + 2)] for x in range(m + 2)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            padded_gold_matrix[i][j] = gold_matrix[i - 1][j - 1]
    
    #print(padded_gold_matrix)
    
    max_row = max_gold_in_column(padded_gold_matrix, 1)
    gold_collected = padded_gold_matrix[max_row][1]
    for i in range(2, n+1):
        #print(gold_collected, max_row)

        max_row = max_gold_in_column(padded_gold_matrix, i, max_row)
        gold_collected += padded_gold_matrix[max_row][i]
        #print(gold_collected, max_row)
        
    return gold_collected
    
gold_mine_table = [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
m = 4
n = 4
print(gold_mine(gold_mine_table, m, n))
