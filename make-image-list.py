import random, json
from os import listdir
from os.path import isfile, join

def main():
    file_names = [f for f in listdir('peak-images') if isfile(join('peak-images', f))]
    random.shuffle(file_names)

    with open('image-list.json', 'r+') as f:
        old = json.load(f)
        data = [s for s in old if s['name'] in file_names]
        names = [x['name'] for x in data]
        for file_name in file_names:
            if file_name not in names:
                data.append({"name": file_name, "tweeted": "false"})
        random.shuffle(data)
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()

if __name__ == '__main__':
    main()
