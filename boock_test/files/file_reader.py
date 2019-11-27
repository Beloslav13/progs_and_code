filename = 'learning_python.txt'
with open(filename, 'r', encoding='utf8') as file:
    file_read = file.read()
    print(file_read)

print('\n')

with open(filename) as file:
    python = 'Python'
    for line in file:
        if python in line:
            print(line.replace(python, 'C').strip())
        else:
            print(line.strip())



with open(filename, 'r', encoding='utf8') as file:
    file_text = file.readlines()

print('\n')


for line in file_text:
    print(line.strip())