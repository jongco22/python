class MyOp:

    #----------------------------------------------------------------------
    # 이 부분은 생략가능. class attributes가 필요없는 경우엔
    #class attributes(class variable, class methods, instance methods)
    
    # 1. class variable
    cnt=0
    type='MyOp.'
    version='0.1'
    
    @classmethod #decorate: 어떤 특수한 기능을 아래의 함수에 추가해줌.
    def print_version(cls):
        print(cls.version)
        
    #----------------------------------------------------------------------
    #instance attributes
    
    def __init__(self):
        self.ret_value=None #instance variable. instance attributes
        MyOp.cnt +=1
        
    def run(self, *args):
        return self.ret_value
    
    @staticmethod
    def s_method():
        pass
    
if __name__ == '__main__':
    MyOp.print_version()
    print(MyOp.cnt)
    
    a=MyOp()
    print(Myop.cnt)
    print(a.cnt)
    
    b=MyOp
    print(a.cnt)