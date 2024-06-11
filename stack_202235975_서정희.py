class stackj: #stackj class 생성
    def __init__(self):
        stackj_list=[1,2,3,4]  #stackj_list 리스트 생성
        self.x=stackj_list
    def stackj_ls(self): #stackj_ls 함수 생성
        self.a_ap=input('참가할 요소를 입력하시오.(쉼표로 구분):').split(',') #push할 element들을 입력받고, ','로 구분하여 a_ap라는 이름의 리스트로 만들어줌.
        for i in self.a_ap: #for 반복문을 이용해 a_ap리스트의 각 요소를 stackj_list에 push해줌
            self.x.append(i)
        
        print('')  #보기 쉽게 한 줄 띄어줌
        print('stack push') #push한 list를 출력해줄 것이라는 설명
        print('push list=', self.x) #element를 push한 list를 출력해줌
        print('')
        print('stack pop') #pop을 할 것이라는 설명
        
        while len(self.x) > 0: #while 반복문을 이용해 stackj_list 요소가 0개보다 크면 pop을 실행하게 되어 있음.
            self.x.pop()
            print(self.x) #pop할 때마다 리스트를 출력해 늦게 들어온 element가 먼저 나간다는 것을 알 수 있음
        
        print('')
        print('pop list=', self.x) #모든 과정을 수행한 stackj_list를 출력해줌
    
    
if __name__ == '__main__': # main script에서만 실행되도록함.
    sj=stackj()
    sj.stackj_ls() #stackj class의 stack_ls 함수 실행
    
        
                    