class Car: #super class Car정의
    def __init__(self, brand, color, size, speed):  #초기화 함수 정의, car의 속성인 brand, color, size, speed정의 
        self.speed=speed # 다른 함수에서도 speed를 사용하기 위해 self로 정의해준다.
        print(f'Car brand is {brand}. Car color is {color}. Car size is {size}')
    
    def acceleration(self, sp): #가속도 함수정의 
        self.speed += sp #__init__함수에서 정의한 speed에 가속도를 더해주어서 새로운 속도를 정의해준다.
        print('car acceleration is', self.speed)
        
    def deceleration(self, sp): #감속 함수 정의
        self.speed -= sp #__init__ 함수에서 정의한 speed에 감속속도를 더해서 새로운 속도를 정의한다.
        print('car deceleration is', self.speed)
    def clarksion(sound): #clarksion 함수 정의
        print(f'Basic car clarksion in {sound}')
           
class volvo(Car): #Car class를 상속받은 volvo class를 정의해준다.
    def __init__(self, color, size, speed):
        super().__init__('volvo', color, size, speed) #super class Car를 상속받았고, brand는 volvo로 확정.
               
    def clarksion(): #Car class에서 상속받은 method를 sub-class에서 재정의함.
        print('Car clarksion is bbang')
        
class bmw(Car): #Car class를 상속받은 bmw class를 정의해준다.
    def __init__(self,color,size,speed): 
        super().__init__('bmw',color,size,speed) #super class Car를 상속받았고, brand는 bmw로 확정.
    
    def clarksion(): #Car class에서 상속받은 method를 sub-class에서 재정의함.
        print('Car clarksion is bbipp')
            
my_car=bmw('red','medium',30) #bmw class data에 expression 할당 및 bmw class 실행 
my_car.acceleration(3) #가속도 함수에 expression을 넣어주어서 실행
my_car.deceleration(10) #감속 함수에 expression을 넣어주어서 실행
print('') # 줄 띄기
volvo.clarksion() #volvo의 clarksion
print('')
Car.clarksion('boop') #기본 car의 clarksion



    



    