from os import path


# print(' '.join(line.replace('"','').split(",")).lower())
# "SWITCH_ID","UNI_A","UNI_B","DEFECTS_MAP","BILL_DTM","DURATION","SERVICE_TYPE","CDR_SET","CDR_SET_OUT","INC_TG","OUT_TG","SEGMENT_A","OUTBLOCK"
# result: switch_id uni_a uni_b defects_map bill_dtm duration service_type cdr_set cdr_set_out inc_tg out_tg segment_a outblock


def create_import():
    print('from os import path\n')

def print_parameters(start_text, list_to_transform):
    print(start_text, "index=None, ", end='', sep='')
    index = 0
    while index < len(list_to_transform):
        out_index = index
        for inner_index in range(index, index + 3):
            if inner_index >= len(list_to_transform):
                continue
            print(list_to_transform[inner_index], '=None', sep='', end='')
            if inner_index != len(list_to_transform) - 1:
                print(',', end='')
            else:
                print('):', end='')
                index += 1
                continue
            if inner_index != out_index + 2:
                print(' ', end='')
            index += 1
        if index < len(list_to_transform):
            print('\n' + ' ' * (len(start_text) - 6), end='')
        else:
            print()


def values_assigment(start_text, list_to_transform):
    start_spases = len(start_text) - 15
    print(' '*start_spases, 'self.index = index', sep='')
    for index in range(len(list_to_transform)):
        print(' '*start_spases, end='')
        print('self.', list_to_transform[index], ' = ',
              list_to_transform[index], sep='')


def create_init(list_to_transform):
    start_text = "    def __init__(self, "
    print_parameters(start_text, list_to_transform)
    values_assigment(start_text, list_to_transform)

               # in next line we delete file_place function pharameter
def create_file_read_function(name_of_records, len_of_elements,
                              class_name, file_name, divider='\t'):
    print(f'\ndef read_{name_of_records}(folder, file_name):')
    print(
    f'    {name_of_records}_file_name = path.join(folder, file_name)',
    f'    {name_of_records}_file = open({name_of_records}_file_name)',
    f'    {name_of_records}_lines = {name_of_records}_file.readlines()',
    f'    size_of_{name_of_records}_list = len({name_of_records}_lines)',
    f'    for index in range(size_of_{name_of_records}_list):',
    f'        {name_of_records}_lines[index] = (',
    f'               {name_of_records}_lines[index].rstrip())',
    f'    {name_of_records} = [None] * size_of_{name_of_records}_list',
    f'    in_{name_of_records}_list_index = 0',
    f'    out_{name_of_records}_list_index = 0',
    f'    while in_{name_of_records}_list_index < size_of_{name_of_records}_list:',
    f'        line_split = (',
    f'               {name_of_records}_lines[in_{name_of_records}_list_index].split("{divider}"))',
    f'        if line_split[-1] == "\\n":',
    f'            line_split.pop()',
    f'        # print(in_{name_of_records}_list_index, "line_split =", line_split)',
    f'        if len(line_split) == {len_of_elements}:',
    f'            {name_of_records}[out_{name_of_records}_list_index] = (',
    f'                            {class_name}(out_{name_of_records}_list_index,',
    f'                            *line_split))',
    f'            in_{name_of_records}_list_index += 1',
    f'            out_{name_of_records}_list_index += 1',
    f'        else:',
    '            print(f"Error in line from file = {file_name}",',
    '                  f"with index = {in_%s_list_index}",' % name_of_records,
    '                  f"with value {line_split}",',
    '                  f"wait for %d parameters",' % len_of_elements,
    '                  f"and got {len(line_split)}")',
    # here could be print into error log file
    f'            size_of_{name_of_records}_list -= 1',
    f'            in_{name_of_records}_list_index += 1',
    f'            {name_of_records}.pop()',
    f'    return {name_of_records}',
    sep='\n')


def create__str__function():
    print('\n    def __str__(self):')
    print('        \'\'\'',
          '        we return a string which almost looks like a list with str value',
          '        of every field in record',
          '        \'\'\'',
          '        list_of_values = [str(t) for name, t in self.__dict__.items()',
          '                          if type(t).__name__ != "function" and',
          '                          not name.startswith("__")]',
          '        line_to_return = "[" + " , ".join(list_of_values) + "]"',
          '        return line_to_return',
          sep='\n')
    
def create_main(name_of_records, folder, file_name):
    print(f'\n\n# main for {name_of_records} part():',
    f'{name_of_records}_folder = r"{folder}"',
    f'{name_of_records}_file_name = "{file_name}"',
    f'list_of_{name_of_records} = read_{name_of_records}('
    f'{name_of_records}_folder, {name_of_records}_file_name)',
    f'print("{name_of_records}_list:")',
    f'for record in list_of_{name_of_records}:',
    f'    print(record)',
    sep='\n')


'''
### TODO
we have some first column in file with 2200 value need to find what is it

we need to create a class with name camel_style
cause we use it in read function

'''
    

# string_to_transform = '''
#         switch_id, uni_a, uni_b, bill_dtm, out_tg, duration, cdr_set_out, substr_service_type, outblock
# '''
# string_to_transform = '''
#        name, hour_0,  date, hour_1, hour_2, hour_3, hour_4, hour_5, hour_6, hour_7, 
#        hour_8, hour_9, hour_10, hour_11, hour_12, hour_13,  switch_id,
#        hour_14, hour_15, hour_16, hour_17, hour_18, hour_19, hour_20,
#        hour_21, hour_22, hour_23,  rs_id
# '''
# string_to_transform = '''SWITCH_ID    SWITCH_NAME    RS_ID    RS_NAME'''
string_to_transform = '''row_number    some_number    ts_full'''


# folder = 'D:\python\double_dno\ms_ntk_same_amount_lviv_out\station_3200'
folder = r'C:\Users\dno\eclipse-workspace\aska kt truvalist\lviv'
divider = ','
file_name = 'lvv csv 3 cols.csv'
name_of_records = 'meta'


file_place = path.join(folder, file_name)
class_name = ''.join(word.title() for word in name_of_records.split('_'))
create_import()

print(f'class {class_name}:')
if string_to_transform.find(',') > 0:
    list_to_transform = string_to_transform.split('\t')
elif string_to_transform.find(' ') > 0:
    list_to_transform = string_to_transform.strip().rstrip().split()
len_of_elements = len(list_to_transform)
for index in range(len_of_elements):
    list_to_transform[index] = list_to_transform[index].strip().rstrip().lower()

# print(list_to_transform)



create_init(list_to_transform)

create__str__function()

create_file_read_function(
    name_of_records, len_of_elements, class_name, file_name, divider)

create_main(name_of_records, folder, file_name)
