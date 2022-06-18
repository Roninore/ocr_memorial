#Libraries
#Files
import read_photo

if __name__ == '__main__':
    data = read_photo.read_dir()
    for photo in data:
        print(f'File: {photo["filename"]}\tTime to read: {photo["time"]}',end='\n')
        print(f'    Name: {photo["data"]["full_name"]}',end='\t')
        print(f'Date: |{photo["data"]["dates"]["left"]}| - |{photo["data"]["dates"]["right"]}|',end='\n\n')
