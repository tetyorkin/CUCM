FILE1 = 'cucm_dn.txt'
FILE2 = 'css.txt'


# Find number and css
def parser(number, css):
    with open(FILE1, 'r', encoding='utf-8') as file:
        user_dict = {}
        a = 0
        for i in file:
            line = i.replace('\n', '')
            if 'pattern' in line:
                pattern = {'number': line.split(' ')[-1]}
                user_dict.update(pattern)
            elif 'description' in line:
                description = {'description': line.split(' ')[17:]}
                user_dict.update(description)
            elif 'value' in line:
                value = {'css': line.split(' ')[-1]}
                user_dict.update(value)
                if number in user_dict['number'] and css in user_dict['css']:
                    a += 1
                    write_file(f'{user_dict}\n')


# Write file
def write_file(data):
    with open(FILE2, 'a', encoding='utf-8') as f:
        f.write(str(data))


if __name__ == '__main__':
    parser('170', 'ast_limited_css')
