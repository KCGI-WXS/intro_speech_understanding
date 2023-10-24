

def cancellation(input_list, stop_word):
    new_list = []
    for i in input_list:
        if i !=stop_word:
            new_list.append(i)
        else:
            break
    return new_list
        

def copy_all_but_skip_word(input_list, skip_word):
    output_list = []
    for i in input_list:
        if i != skip_word:
            output_list.append(i)
    return output_list


def my_average(input_list):
    sum_input_list = 0
    for i in input_list:
        sum_input_list = sum_input_list + float(i)
    return sum_input_list/len(input_list)

