#! /usr/local/bin/python3
# Takes a matrix of strings, prints them in tabular form


def print_table(matrix):
    # find maximum length for each column
    max_lengths = []
    for i in range(len(matrix)):
        max_length = 0
        for j in range(len(matrix[0])):
            max_length = max(max_length, len(matrix[i][j]))
        max_lengths.append(max_length)

    for i in range(len(matrix[0])):
        row = ''
        for j in range(len(matrix)):
            row += matrix[j][i].rjust(max_lengths[j])
            row += ' '
        print(row)


table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
