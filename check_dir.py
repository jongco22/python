#diretory 경로 확인
import os

# 현재 작업 디렉토리 확인
current_dir = os.getcwd()

# 확인할 파일 이름
file_name = 'comprehension_list.py'

# 파일 경로 생성
file_path = os.path.join(current_dir, file_name)

# 파일 존재 여부 확인
if os.path.exists(file_path):
    print(f"'{file_name}' 파일이 현재 디렉토리에 존재합니다.")
else:
    print(f"'{file_name}' 파일이 현재 디렉토리에 존재하지 않습니다.")

# 현재 디렉토리에 있는 파일 출력
print("현재 디렉토리에 있는 파일:")
for filename in os.listdir(current_dir):
    print(filename)