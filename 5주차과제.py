#global scope
def gen_closure(p): # local scope에서 gen_closure(p)함수 정의
    call_cnt = 0 #nonlocal scope. cnt: counting변수. 얼마나 호출되었는지 세는 변수 _ds_power 관점에서는 enclosing scope

    def _ds_power (b, return_cnt=False): #_ds_power입장에서 local scope
        nonlocal call_cnt #nonlocal scope에 있는 call_cnt 변수를 다른 scope에서 사용하기 위해 'nonlocal' 키워드 사용
        call_cnt += 1 #call_cnt에 1을 더해서 반환
        ret = b**p #'ret' variable 생성. b를 p제곱함
        if not return_cnt: #return_cnt가 false일 시
            return ret #ret 반환
        return ret,call_cnt #_ds_power에 대해 ret과 call_cnt반환.(return_cnt=true일 시)

    return _ds_power #gen_closure에 대해 _ds_power반환

p2_func = gen_closure(2) #local scope에서 p2_func변수 생성. expression=gen_closure(2).p=2
print(p2_func(10)) #b=10. return_cnt=False(none은 false이다.). 출력값: 100 #cnt=1

p3_func = gen_closure(3)  #p3이름변경해서 실행 #variable: p3_func, expression=gen_closure(3). p=3
r, c_p3 = p3_func(10, True) #r=p3_func(10), c_p3=p3_func(True). b=10 #cnt=1
print(r) #출력값= 1000

r, c_p2 = p2_func(10, True) #r=p2_func(10). r 재정의, c_p2=p2_func(True) #cnt=2(p2_func는 2번 호출됨.)
print(f'10^2={r}') #출력값=100 
print(f'power2 : call_cnt={c_p2}') #c_p2출력값=2
print(f'power3 : call_cnt={c_p3}') #c_p3출력값=1
for idx,c in enumerate(p3_func.__closure__): #enumerate는 인덱스와 값을 함께 반환함. func.__closure__는 함수의 closure에 접근할 수 있는 방법이다.
    print(f"p3_func's enclosing variable[{idx}]:{c.cell_contents}") #p3_func함수의 closure 변수는 call_cnt와 p 이다.
#출력값 [0]:몇번호출되었는지, [1]:p값
