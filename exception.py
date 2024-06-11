def divide_num():
    try:
        numerator=int(input('Enter numerator:'))
        denominator=int(input('Enter denominator:'))
        result=numerator/denominator
    except ValueError: #ValueError- 입력 값이 기대하는 값의 범위나 형식에 맞지 않을 때 발생하는 python 내장 예외.
        print('invalid input. please enter integers only.') #숫자가 작성되지 않음. ValueError 예외 발생시 출력됨.
    except ZeroDivisionError: #ZeroDivisionError-숫자를 0으로 나누려고 시도할 때 발생하는 python 내장 예외.
        print('division by zero is not allowed.') #분모는 0이 될 수 없음. ZeroDivisionError 발생시 출력됨.
    else:
        print(f'the result is: {result}')
    finally:
        print('execution completed')
        
divide_num()