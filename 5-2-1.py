def test(p0,p1,*args): #p0: 첫 번째 위치 매개변수, p1: 두 번째 위치 매개변수, *args: 가변 위치 인수. 나머지 모든 인수는 tuple로 전달됨.
    print(p0)
    print(p1)
    print(args)
    print(args[0]) #args의 첫 번째 index element

# test(1,'dddd',3,4,5)
a=range(10)
test(*a) #range 객체 'a'를 언패킹하여 'test'함수에 전달. 언패킹은 'a'의 모든 요소를 개별 인수로 변환함. 즉, 'test(*a)는 'test(0,1,2,3,4,5,6,7,8,9)와 동일함.