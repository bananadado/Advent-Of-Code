with open("input.txt", "r") as f:
    inp = [line.strip() for line in f.readlines()]

def compare(thing1, thing2): #why did i name them this thing
    if isinstance(thing1, int) and isinstance(thing2, int): #ineteger check
        if thing1 < thing2:
            return -1
        elif thing2 < thing1:
            return 1
        else:
            return 0
    elif isinstance(thing1,list) and isinstance(thing2, list):
        i = 0
        while i < len(thing1) and i < len(thing2):
            comparison = compare(thing1[i], thing2[i])
            if comparison == 1:
                return 1
            elif comparison == -1:
                return -1
            i += 1
        if i==len(thing1) and i<len(thing2):
            return -1
        elif i==len(thing2) and i<len(thing1):
            return 1
        else:
            return 0
    elif isinstance(thing1,int) and isinstance(thing2, list):#
        return compare([thing1], thing2)
    else:
        return compare(thing1,[thing2])


packets = []
total=0
for i in range(len(inp)//3+1):
    arr1 = inp[i*3]
    arr2 = inp[i*3+1]
    arr1 = eval(arr1) #most important part of this whole thing and why no C#
    arr2 = eval(arr2)
    packets.append(arr1)
    packets.append(arr2)
    if (compare(arr1,arr2)) == -1:
        total += i+1
print(f"Part 1: {total}")


#part 2
packets.append([[2]])
packets.append([[6]])
sorted = False

while not sorted: #bubbly sort - originally I just counted how many were smaller but bubble sort ╰（‵□′）╯
    sorted = True
    for i in range(len(packets)-1):
        if compare(packets[i],packets[i+1]) >= 0:
            packets[i], packets[i+1] = packets[i+1], packets[i]
            sorted = False
total2 = 1
for i,p in enumerate(packets):
    if p==[[2]] or p==[[6]]:
        total2 *= i+1
print(f"Part 2: {total2}")
