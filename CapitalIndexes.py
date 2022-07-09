def capitalindexes(string):
    brstr = list(string)
    iterator = 0
    strarr = []
    indexes = []
    for i in brstr:
        strarr.append(i)

    while(iterator < len(strarr)):
        if(strarr[iterator].isupper()):
            indexes.append(iterator)
        iterator += 1

    print("Capital indexes at: ", indexes)

capitalindexes("StRiNg")