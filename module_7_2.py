def custom_write(file_name, strings):
    strings_positions = {}
    index = 1
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        position = file.tell()  
        file.write(string + '\n')  
        strings_positions[(index, position)] = string
        index += 1  

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
