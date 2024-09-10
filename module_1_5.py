immutable_var = ("hello", [1, 3, 5])
print(immutable_var)
#immutable_var[0] = "Привет"
#print(immutable_var)
#TypeError: 'tuple' object does not support item assignment
#Кортеж - это последовательность элементов, которая является неизменяемым типом.
#Поэтому не получится изменить содержимое кортежа после его создания
mutable_list = ["hello", [1, 3, 5]]
mutable_list[0] = "Привет"
print(mutable_list)