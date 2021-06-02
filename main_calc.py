def add(string_numbers):
    if string_numbers == "":
        return 0
    elif string_numbers.isnumeric():
        return int(string_numbers)
    else:
        string_length = len(string_numbers)
        cleaned_string = string_numbers

        for j in range(0, string_length):

            loop_character = string_numbers[j:j + 1]

            if loop_character.isnumeric() == False:
                if loop_character == '-':
                    if string_numbers[j+1:j + 2].isnumeric():
                        pass
                else:
                    replacement_character = ','
                    cleaned_string = skimmer(string_length, 1, j, cleaned_string, string_numbers, replacement_character)

        string_split = list(filter(None, cleaned_string.split(',')))
        string_split = [int(i) for i in string_split]

        only_positive_string = ['' if i < 0 or i > 1000 else i for i in string_split]
        only_positive_string = list(filter(None, only_positive_string))

        only_negative_string = ['' if i > 0 else i for i in string_split]
        only_negative_string = list(filter(None, only_negative_string))

        positive_string_total = sum(only_positive_string)

        if only_negative_string:
            return 'Negatives not allowed: ' + str(only_negative_string)[1:-1]

        return positive_string_total


def skimmer(total_length, num_chars_to_replace, where_to_start, clean_side, dirty_side, replacement_character):
    final_string = clean_side[0:where_to_start] + replacement_character + dirty_side[where_to_start+1:total_length]
    return(final_string)
