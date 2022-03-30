while True:
    inp = input()
    if inp == '0':
        break
    for i in range(len(inp)//2):
        if inp[i] != inp[(i+1)*-1]:
            print("no")
            break
    else:
        print("yes")
