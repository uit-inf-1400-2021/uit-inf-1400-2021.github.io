def get_lines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines

def convert_list_to_int(str_list):
    result_list = []
    for entry in str_list:
        result_list.append(int(entry))
    return result_list

def get_average(int_list):
    total = sum(int_list)
    average = total / len(int_list)
    return average

def get_average_from_file(filename):
    str_lines = get_lines(filename)
    number_list = convert_list_to_int(str_lines)
    average = get_average(number_list)
    return average

def process_files(filenames):
    for f in filenames:
        average = get_average_from_file(f)
        print("Average for file {} is {}".format(f, average))

def input_filenames():
    files = []
    while True:
        filename = input("Input filenames, enter blank line when done: ")
        if len(filename) == 0:
            break
        files.append(filename)
    return files

if __name__ == "__main__":
    files = input_filenames()
    process_files(files)

