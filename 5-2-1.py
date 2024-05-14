def test(p0,p1,*args):
    print(p0)
    print(p1)
    print(args)
    args[0]

# test(1,'dddd',3,4,5)
a=range(10)
test(*a)