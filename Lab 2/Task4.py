foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\output4.txt", "w")
finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\input4.txt", "r")
ro = finput.read().split()

N = ro[0]
arr = []
for i in range(1, len(ro)):
    arr.append(int(ro[i]))


def merge(l, r):
    A = []
    i = 0
    j = 0
    while (i < len(l) and j < len(r)):
        if (l[i] < r[j]):
            A.append(l[i])
            i += 1
        else:
            A.append(r[j])
            j += 1
    A += l[i::]
    A += r[j::]
    return A


def mergeSort(p):
    if(len(p) <= 1):
        return p
    m = int(len(p) / 2)
    l = mergeSort(p[:m])
    r = mergeSort(p[m:])
    return merge(l, r)


sorted_N = mergeSort(arr)
for i in range(len(sorted_N)):
    foutput.write(str(sorted_N[i]))
    foutput.write(' ')
