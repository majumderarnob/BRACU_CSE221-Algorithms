finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 5\\task1_input.txt", "r")
foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 5\\task1_output.txt", "w")
inp = finput.read().split()
n = 2
x = [inp[i:i+n] for i in range(1, len(inp) - 1, n)]


def assignment_selection(arr, n):
    selected = []
    assignment.sort(key=lambda x: x[1])
    i = 0
    selected.append(arr[i])
    c = 1
    for j in range(1, n):
        if(arr[j][0] >= arr[i][1]):
            selected.append(arr[j])
            i = j
            c += 1
    print(c, file=foutput)
    return selected


assignment = x
n = len(assignment)
selected = assignment_selection(assignment, n)
for el in selected:
    print(el, file=foutput)
