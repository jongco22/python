with open('target_file.txt', 'w') as f:
    f.write('this is a sample file with some text datas.')
    
import os

file_path='target_file.txt'
file_size=os.path.getsize(file_path)

print(f'The size of {file_path} is: {file_size} bytes')
