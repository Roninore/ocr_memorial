#Files
from write_json import write_json
from classes.PhotoReader import PhotoReader

if __name__ == '__main__':
    # data = read_photo.read_dir()
    photo_reader = PhotoReader()
    data = photo_reader.read_dir()
    write_json(data)
    print('Success!')
