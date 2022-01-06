out = open("D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 1\\output4.txt", "w")
inp = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 1\\input4.txt", "r")
lines = inp.readlines()
n = int(lines[0])

a = [[0]*n for i in range(n)]
b = [[0]*n for i in range(n)]
c = [[0]*n for i in range(n)]

for i in range(1, n+1):
    a[i - 1] = list(map(int, lines[i].split()))
for i in range(n + 2, n + 2 + n):
    b[i - n - 2] = list(map(int, lines[i].split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]

for i in range(n):
    s = ""
    for j in range(n):
        s += str(c[i][j])+" "
    s += "\n"
    out.write(s)
