import read_photo
from write_json import write_json

if __name__ == '__main__':
    data = read_photo.read_dir()
    for photo in data:
        print(f'File: {photo["filename"]}\tTime to read: {photo["time"]}',end='\n')
        print(f'    Name: {photo["data"]["full_name"]}',end='\t')
        print(f'Date: |{photo["data"]["dates"]["left"]}| - |{photo["data"]["dates"]["right"]}|',end='\n\n')
    
    write_json(data)
