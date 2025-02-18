def printTable():

    colwidths = [0] * len(tableData)

    for i in range(len(tableData)):
        for item in tableData[i]:
            if len(item) > colwidths[i]:
                colwidths[i] = len(item)

    for row in range(len(tableData[0])):
        for col in range(len(tableData)):
            print(tableData[col][row].rjust(colwidths[col]), end=' ')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable()
