import re

with open('input', encoding='utf-8') as f:
    content = f.readlines()

content = [x.strip() for x in content]

result = sum(int(re.findall("\d", content[i])[0]) * 10 + int(re.findall("\d", content[i])[-1]) for i in range(len(content)))

print(result)
