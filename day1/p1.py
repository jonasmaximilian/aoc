import re

with open('input', encoding='utf-8') as f:
    content = f.readlines()

result = sum(int(re.findall(r"\d", content[i])[0]) * 10 + int(re.findall(r"\d", content[i])[-1]) for i in range(len(content)))

