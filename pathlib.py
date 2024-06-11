from pathlib import Path #'pathlib'모듈에서 Path 클래스를 가져옴.

#file 생성
file_path=Path('example.txt')
file_path.write_text('This is simple text file.')

#파일 여부 확인
print('파일 여부:', file_path.is_file())

#디렉토리 생성
dir_path= Path('example_dir') #'Path' 객체를 생성하고, 이 객체는 'example_dir'이라는 디렉토리 경로를 나타낸다. 'example_dir'은 생성하려는 디렉토리의 이름임.
dir_path.mkdir(parents=True, exist_ok=True) #parents=True: 만약 경로에 상위 디렉토리가 포함되어 있다면, 상위 디렉토리들도 함께 생성함. exist_ok=True: 디렉토리가 이미 존재하는 경우에도 오류를 발생시키지 않음.
#dir_path라는 경로에 'example_dir'이라는 directory 생성

#디렉토리 여부 확인 
print('디렉토리 여부:', dir_path.is_dir())

#파일 읽기
file_content=file_path.read_text()
print('파일 내용:', file_content)

#디렉토리 삭제
dir_path.rmdir()

#파일 이름 변경
file_path.rename('new_example.txt')