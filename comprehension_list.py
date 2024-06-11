#파일을 불러오는 코드로 text file을 가져옴. 'r'은 읽기 모드.
with open('comprehension\introduction.txt', 'r') as infile: #comprehension\introduction.txt인 이유: introduction.txt('py\comprehension'에 존재)일 경우 현재 파일은 py에서 진행을 하는데 directory가 달라서 찾을 수 없다고 뜬다. introduction.txt파일을 찾을 수 있게 경로를 써준 것임.
    com_ls=[line for line in [l.strip() for l in [j.capitalize() for j in infile]]if line != '']
    print(com_ls)
