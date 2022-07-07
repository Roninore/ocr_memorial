#Files
import read_photo
from write_json import write_json

if __name__ == '__main__':
    data = read_photo.read_dir()
    write_json(data)
    print('Success!')
