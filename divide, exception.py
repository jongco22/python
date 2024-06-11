def divide(a,b):
    return a/b

def main():
    try:
        a_str=input('numerator=')
        a=int(a_str)
        
        
        b_str=input('denumerator=')
        b=int(b_str)
        
        r=divide(a,b)
        print(f'result={r}')
    except ValueError as ve:
        print(ve)
        print(f'check your inputs')
        raise ValueError('잘못된 input value입니다.')
    except ZeroDivisionError as ze: #분모에는 0이 올 수 없음을 알려줌
        print(ze)
        print(f'denominator can not be zero!')
    except Exception as e:
        print(e)
        raise e
    finally:
        print('This python script is finished.')
        
main()

        