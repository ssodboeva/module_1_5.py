immutable_var = (1,2, 'apple', True)
print (immutable_var)
#immutable_var [0] = "mix" # операция недопустима. Тип переменной immutable_var - 'tuple'.
mutable_list = [1,2,3, 'banana', 'd']
mutable_list [0] = 'dance'
mutable_list.remove('d')
print (mutable_list)