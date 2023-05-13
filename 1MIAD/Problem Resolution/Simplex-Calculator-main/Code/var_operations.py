def Round(Table):
    for i in range(0,len(Table)):
        for j in range (0,len(Table[i])):
            Table[i][j] = round(Table[i][j], 2)
    return Table
def ToInt(Table):
    for i in range(0,len(Table)):
       Table[i]=int(Table[i])
    return Table
def ToIntMatrix(Table):
    for i in range(0,len(Table)):
        for j in range (0,len(Table[i])):
            Table[i][j]=int(Table[i][j])
    return Table