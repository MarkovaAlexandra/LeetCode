# A phrase is a palindrome if, after converting all uppercase letters into lowercase
# letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise

def isPalindrome(s: str) -> bool:
    elements = list(s)                                         # разделяем строку на список
    needed_elements = []                                       # создаем новый список, куда будем складывать только буквы
    for i in range(0,len(elements)):
        if  (elements[i].isalpha() or elements[i].isdigit()):  # если элемент буква
            needed_elements.append(elements[i].lower())        # добавляем ее в список букв в нижнем регистре
    s_new = "".join(needed_elements)                           # переводим список в строку
    if (s_new == s_new[::-1]):
        return True
    else:
        return False

