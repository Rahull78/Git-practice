lst=[int(x)for x in input("enter: ").split()]
fno=int(input("number: "))
for x in lst:
    if x==fno:
        print("found: "),lst.index(x)
        break
    else:
        print("not found")
