import hashlib

puzzle_input = 'yzbqklnj'

n = 1

while True:
    n += 1

    num = hashlib.md5((puzzle_input + str(n)).encode('utf-8')).hexdigest()

    if num.startswith("00000"):
        print(n)
        break
