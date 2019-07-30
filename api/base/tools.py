
def camel_to_underline(camel_format):
    '''
        驼峰命名格式转下划线命名格式
    '''
    underline_format=''
    if isinstance(camel_format, str):
        for _s_ in camel_format:
            underline_format += _s_ if _s_.islower() else '_'+_s_.lower()
    return underline_format


def underline_to_camel(underline_format):
    '''
        下划线命名格式驼峰命名格式
    '''
    camel_format = ''
    if isinstance(underline_format, str):
        for _s_ in underline_format.split('_'):
            camel_format += _s_.capitalize()
    return camel_format


def camel_to_slash_line(str_format, separator="/"):
    '''
        斜杆命名格式驼峰命名格式
    '''
    camel_format = ''
    if isinstance(str_format, str):
        str_format = str_format[str_format.rfind(separator)+1:]
        camel_format += str_format.capitalize()
    return camel_format

