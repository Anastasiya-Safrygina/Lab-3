f = open('input.txt')
lines = f.readlines()
f.close()
max_string = ''
max_value = 0
for i in range(len(lines)):
    if lines[i].find('>String') != -1:
        num = lines[i].strip()
        dna = lines[i + 1]
        count = dna.count('G') + dna.count('C')
        percent = count / len(dna) * 100
        if percent > max_value:
            max_value = percent
            max_string = num
print(f'Фрагмент max: {max_string}\nДоля G/C: {max_value}')
