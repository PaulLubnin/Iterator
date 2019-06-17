import json

class FileOpen:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, encoding='utf8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

class IterFile:

    def __init__(self, collection):
        self.collection = collection
        self.count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == len(self.collection):
            raise StopIteration
        return self.collection[self.count]


if __name__ == '__main__':
    with FileOpen('countries.json') as json_file:
        file = json.load(json_file)
        country_list = []
        for countries in file:
            country_list.append(countries['name']['common'])

        country_links = open('country_links.txt', 'w', encoding='utf8')
        for countries in IterFile(country_list):
            country_links.write(f'{countries}: https://wikipedia.org/wiki/{countries}' + '\n')
        country_links.close()
