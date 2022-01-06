foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\output2.txt", "w")
finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\input2.txt", "r")
arr = finput.read().split()

N = int(arr[0])
M = []
for i in range(2, len(arr)):
    M.append(int(arr[i]))

for i in range(len(M)):
    min_elem = i
    for j in range(i+1, len(M)):
        if M[min_elem] > M[j]:
            min_elem = j
    M[i], M[min_elem] = M[min_elem], M[i]

for i in range(0, int(arr[1])):
    foutput.write(str(M[i]))
    foutput.write(' ')
