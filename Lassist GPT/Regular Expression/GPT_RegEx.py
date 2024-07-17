import re

simple_string ="""Benim adım Ahmet. Ben 22 yaşındayım. Kardesimin adı da Mehmet."""
pattern='[A-Z][a-z]*'
result=re.findall(pattern,simple_string)
print(result)