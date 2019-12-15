# Ссылка на схемы
# https://drive.google.com/file/d/14vLKzw007Cj8Ld8VYsGee5cxRGMk5lHL/view?usp=sharing

a, b = input("Введите две заглавные буквы английского алфавита, разделенные пробелом: ").split()
a = ord(a) - ord('A') + 1
b = ord(b) - ord('A') + 1
c = abs(a - b)
print(f"Это {a} и {b} буквы алфавита. Между ними {c} букв")