# i는 index 0부터 시작
for i, c in enumerate(range(2,5)): #enumerate: 반복 가능한 객체(iterable)을 입력 받아 인덱스와 요소를 동시에 반환하는 iterator를 생성함.
   if i % 2 == 1:
      continue
   print(f'{i},{c}')
    