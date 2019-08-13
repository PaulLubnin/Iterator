import hashlib

def hash_generate(file_path):
    with open(file_path, 'rb') as text_file:
        for line in text_file:
            yield hashlib.md5(line).hexdigest()


print(hash_generate('country_links.txt'))
for line in hash_generate('country_links.txt'):
    print(line)
