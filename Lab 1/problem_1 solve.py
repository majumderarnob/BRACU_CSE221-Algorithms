foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 1\\prob_1_output.txt", "w")
frec = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 1\\Record.txt", "w")
finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 1\\prob_1_input.txt", "r")

lines = finput.read().split("\n")
total = (len(lines) - 1)
odd = 0
even = 0
noPar = 0
pal = 0
notpal = 0


def isPalindrome(word):
    l = 0
    r = len(word)-1
    if(len(word) == 0):
        return 0
    while(l <= r):
        if(word[l] != word[r]):
            return 0
        l += 1
        r -= 1
    return 1


for i in range(total):
    a, b = lines[i].split()
    s = ""
    if('.' in a):
        s += a+" has no parity and "
        noPar += 1
    elif(int(a) % 2):
        s += a+" has odd parity and "
        odd += 1
    else:
        s += a+" has even parity and "
        even += 1
    if(isPalindrome(b)):
        s += b+" is a palindrome"
        pal += 1
    else:
        s += b+" is a not palindrome"
        notpal += 1
    foutput.write(s+'\n')

odd = odd*100/total
even = even*100/total
noPar = noPar*100/total
pal = pal*100/total
notpal = notpal*100/total

frec.write(f"Percentage of odd parity: {odd}%\n")
frec.write(f"Percentage of even parity: {even}%\n")
frec.write(f"Percentage of no parity: {noPar}%\n")
frec.write(f"Percentage of palindrome: {pal}%\n")
frec.write(f"Percentage of non-palindrome: {notpal}%\n")
