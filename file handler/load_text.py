print('전체 한꺼번에 읽기')
f = open('text.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)

print('한줄 씩 읽기')
f = open('text.txt', 'r', encoding='utf-8')
while True:
    line = f.readline()
    if line == '':      #빈칸이면 끝내라
        break
    print(line.rstrip())
f.close()

print('전체를 한꺼번에 읽고, 줄 별로 리스트')
f = open('text.txt', 'r', encoding='utf-8')
lines = f.readline()
f.close()
for line in lines:
    print(line.rstrip())

