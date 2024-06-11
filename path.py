from pathlib import Path

#현재 디렉토리의 모든 파일과 디렉토리 나열
for child in Path('.').iterdir():
    print(child)
    
#특정 패턴과 일치하는 파일 나열
for py_file in Path('.').glob('*py'):
    print(py_file)
    
#**를 통해 재귀적으로 검색할 수 있음.(하위디렉토리 포함)
for py_file in Path('.').glob('**/*.py'):
    print(py_file)
    