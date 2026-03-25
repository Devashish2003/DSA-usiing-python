def func(x):
    if x == 0:
        return
    func(x-1)
    print(x)



func(5)
