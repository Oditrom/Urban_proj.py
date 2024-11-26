calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    b = (len(string), string.upper(), string.lower())
    return b

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [_.lower() for _ in list_to_search]
    return string_lower in list_lower


