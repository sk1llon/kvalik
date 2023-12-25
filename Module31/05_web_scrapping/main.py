import re


with open('examples.html', 'r') as f:
    text = f.read()

res = re.findall(r'<h3>\w*\s*\w*', text)
result = []
for i_string in res:
    if '<h3>' in i_string:
        i_string = i_string[4:]
        result.append(i_string)
print(result)
