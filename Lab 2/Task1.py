foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\output1.txt", "w")
finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 2\\input1.txt", "r")
arr = finput.read().split()


def bubbleSort(arr):
    n = int(arr[0])
    for i in range(n):
        swapp = False
        for j in range(1, n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = (arr[j + 1], arr[j])
                swapp = True
        if(swapp == False):
            break


#######################
bubbleSort(arr)
for i in range(1, len(arr)):
    foutput.write(str(arr[i]))
    foutput.write(' ')

# here in this scenerio,  if the given array will already being sorted then it will be the best case scenerio. We don't have to sort the array again in that case. That's why, the time complexity for the best case scenerio is big Theta(n)
