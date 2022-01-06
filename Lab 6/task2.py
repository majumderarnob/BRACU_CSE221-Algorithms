finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 6\\input2.txt", "r")
foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 6\\output2.txt", "w")

inp1 = finput.readline()
inp2 = finput.readline()
inp3 = finput.readline()


def LCS(X, Y, Z):
    m = len(X) - 1
    n = len(Y) - 1
    o = len(Z) - 1
    my_list = [[[None] * (o + 1) for i in range(n + 1)] for y in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            for k in range(o + 1):
                if(i == 0 or j == 0 or k == 0):
                    my_list[i][j][k] = 0
                elif(X[i - 1] == Y[j - 1] == Z[k - 1]):
                    my_list[i][j][k] = (my_list[i - 1][j - 1][k - 1] + 1)
                else:
                    my_list[i][j][k] = max(
                        my_list[i-1][j][k], my_list[i][j - 1][k], my_list[i][j][k - 1])
    return my_list[m][n][o]


length = LCS(inp1, inp2, inp3)
print(length, file=foutput)
