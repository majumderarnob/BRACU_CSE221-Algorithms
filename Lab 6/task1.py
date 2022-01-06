finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 6\\input1.txt", "r")
foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 6\\output1.txt", "w")
inp = finput.readlines()

zones = int(inp[0])
match = inp[1].strip("\n")
my_list = len(match)
predict = inp[2].strip("\n")
my_list2 = len(predict)
my_dict = {"Y": "Yasnaya", "P": "Pochinki", "S": "School", "R": "Rozhok",
           "F": "Farm", "M": "Mylta", "H": "Shelter", "I": "Prison"}


def LCS(match, predict):
    lst = [[None] * (my_list2+1) for i in range(my_list + 1)]
    sequence = []
    for i in range(my_list+1):
        for j in range(my_list2 + 1):
            if(i == 0 or j == 0):
                lst[i][j] = 0
            elif(predict[i - 1] == match[j - 1]):
                lst[i][j] = lst[i - 1][j - 1] + 1
            else:
                lst[i][j] = max(lst[i - 1][j], lst[i][j - 1])
    X = my_list
    Y = my_list2
    while(X and Y > 0):
        if(lst[X][Y] != max(lst[X - 1][Y], lst[X][Y - 1])):
            sequence.append(predict[Y-1])
            X -= 1
            Y -= 1
        else:
            if(lst[X][Y] == lst[X][Y - 1]):
                Y -= 1
            else:
                X -= 1
    return sequence, lst


sequence, lst = LCS(match, predict)
for i in range(len(sequence) - 1, -1, -1):
    print(my_dict[sequence[i]], end=" ", file=foutput)
    correct = (lst[my_list][my_list2] * 100) // zones
print(file=foutput)
print("Correctness of predict: " + str(correct)+'%', file=foutput)
