def uppercase(text):
    """Функция возвращает слова в строке, со всеми заглавными буквами"""
    return text.upper()
def capitalized_words(word):
    """Функция возвращает каждое слово в строке, с заглавной буквой"""
    return ' '.join(word.capitalize() for word in word.split())