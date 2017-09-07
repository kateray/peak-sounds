import random, json
from os import listdir
from os.path import isfile, join

def main():
    file_names = [f for f in listdir('images') if isfile(join('images', f))]
    random.shuffle(file_names)

    data = [{"name": file_name, "tweeted": "false"} for file_name in file_names]
    with open('image-list.json', 'r+') as f:
        json.dump(data, f)

if __name__ == '__main__':
    main()
