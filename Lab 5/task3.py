finput = open(
    "D:\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 5\\task3_input.txt", "r")
foutput = open(
    "D:\\\Documents\\Arnob\\BRACU\\CSE221- Algorithm\\Sec01_20301089_Arnob_Lab 5\\task3_output.txt", "w")

inp = finput.readlines()
x = int(inp[0].strip('\n'))
hours = [int(i) for i in inp[1].strip("\n").split(" ")]
hours.sort()
act = inp[2]
seq = ""
task = []
jack_hour = 0
jill_hour = 0
i = 0
for c in act:
    if(c == "J"):
        task.append(hours[i])
        jack_hour += hours[i]
        seq += str(hours[i])
        i += 1
    elif(c == "j"):
        highest = task.pop()
        seq += str(highest)
        jill_hour += highest

print(seq, file=foutput)
print("Jack will work for", str(jack_hour), "hours", file=foutput)
print("Jill will work for", str(jill_hour), "hours", file=foutput)
