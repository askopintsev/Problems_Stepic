# distinct words count in file
text = []
with open(r'path to file') as full_text:
    for line in full_text:
        for word in line.lower().split():
            text.append(word)

res = {}
for i in text:
    if i in res:
        res[i] += 1
    else:
        res[i] = 1

for i in res:
    print(str(i) + ' ' + str(res[i]))

result = sorted(res.items(), key=lambda item: item[1], reverse=True)

print(result[0])
