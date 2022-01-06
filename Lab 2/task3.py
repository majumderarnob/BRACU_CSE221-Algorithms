foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\output3.txt", "w")
finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\input3.txt", "r")
arr = finput.read().split()

n = int(arr[0])
A = []
for i in range(1, n+1):
    A.append(arr[i])

B = []
for i in range(n+1, len(arr)):
    B.append(arr[i])

for i in range(1, len(B)):
    temp1 = B[i]
    temp2 = A[i]
    j = i - 1
    while j >= 0 and B[j] < temp1:
        A[j + 1] = A[j]
        B[j + 1] = B[j]
        j -= 1
    B[j + 1] = temp1
    A[j + 1] = temp2

for i in range(len(A)):
    foutput.write(str(A[i]))
    foutput.write(' ')
