def get_spiral_parsing(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    curr_row = 0
    curr_col = 0
    result = ""

    while curr_row < rows and curr_col < columns:
        # print the row ->
        for i in range(curr_col, columns):
            result += matrix[curr_row][i]
        curr_row += 1

        # print the last remaining column on the right
        for i in range(curr_row, rows):
            result += matrix[i][columns - 1]
        columns -= 1

        # print the last remaining row from below <-
        if curr_row < rows:
            for i in range(columns - 1, curr_col - 1, -1):
                result += matrix[rows - 1][i]
            rows -= 1

        # print the first column from the left
        if curr_col < columns:
            for i in range(rows - 1, curr_row - 1, -1):
                result += matrix[i][curr_col]
            curr_col += 1

    return result


input_matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

print(get_spiral_parsing(input_matrix))
