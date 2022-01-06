finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 3\\input.txt")

given_inp = finput.read().split('\n')
new_dict = {}

for i in range(1, len(given_inp)):
    store = given_inp[i]
    x = store.split()
    y = int(x[0])
    lst = []
    for j in range(1, len(x)):
        lst.append(int(x[j]))
    new_dict[y] = lst

for k in new_dict:
    print(str(k) + "-->" + str(new_dict[k]))
