import hashlib

def hash_generate(file_path):
    """
    Не смог реализовать "красивый" выход из цикла, когда пустая строка останавливает его
    Пытался привязать выход к самой строке, но в таком случае генератор возвращает строки через одну, т.к.
        используется .readline()
    while len(text_file.readline().strip()) == 0
    """
    with open(file_path, 'rb') as text_file:
        while True:
            yield hashlib.md5(text_file.readline().strip()).hexdigest()


print(hash_generate('country_links.txt'))
for line in hash_generate('country_links.txt'):
    print(line)
    if line == 'd41d8cd98f00b204e9800998ecf8427e':
        break
