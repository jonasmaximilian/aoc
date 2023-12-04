import regex as re

with open('input', encoding='utf-8') as f:
    content = f.readlines()

content = [x.strip() for x in content]

convert_tabel = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

pattern = "\\d"
for key in list(convert_tabel.keys()):
    pattern += '|'+key

content = [re.findall(pattern, content[i], overlapped=True) for i in range(len(content))]
for line in content:
    for i, s in enumerate(line):
        if s in convert_tabel.keys():
            line[i] = convert_tabel.get(s)

result = sum(int(x[0])*10 + int(x[-1]) for x in content)
print(result)
