user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'

invalid_file_name_chars = [
    chr(0), chr(1), chr(2), chr(3), chr(4), chr(5), chr(6), chr(7), chr(8), chr(9), chr(10), chr(11),
    chr(12), chr(13), chr(14), chr(15), chr(16), chr(17), chr(18), chr(19), chr(20), chr(21), chr(22), chr(23), chr(24),
    chr(25), chr(26), chr(27), chr(28), chr(29), chr(30), chr(31), chr(34), chr(60), chr(62), chr(124), ':', '*', '?',
    '\\', '/'
]
invalid_directory_name_chars = [
    '|', '\0', chr(1), chr(2), chr(3), chr(4), chr(5), chr(6), chr(7), chr(8), chr(9), chr(10), chr(11),
    chr(12), chr(13), chr(14), chr(15), chr(16), chr(17), chr(18), chr(19), chr(20), chr(21), chr(22), chr(23), chr(24),
    chr(25), chr(26), chr(27), chr(28), chr(29), chr(30), chr(31), ':', '*', '?', '\\', '/'
]


def replace_char_in_string(string: str, list_of_char: list[str], string_replace: str) -> str:
    temp_string_list = list(string)
    for i in range(0, len(string)):
        if string[i] in list_of_char:
            temp_string_list[i] = string_replace

    return "".join(temp_string_list)
