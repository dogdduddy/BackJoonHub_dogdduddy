while True:
    n = int(input())
    if n == -1:
        break
    total = [1]
    for i in range(2,n):
        if n%i == 0:
            total.append(i)
    if n == sum(total):
        print(n,end=" =")
        for i, v in enumerate(total):
            if i != 0:
                print("+", end="")
            print(" {} ".format(v),end="")
        print()
    else:
        print(n,"is NOT perfect.")
