user_nums1 = input('Введите через запятую цифры первого списка: ')
user_nums2 = input('Введите через запятую цифры второго списка: ')

user_set1 = set(user_nums1)
user_set1.discard(' ')
user_set1.discard(',')
user_set1.discard('/')
user_set1.discard(';')

user_set2 = set(user_nums2)
user_set2.discard(' ')
user_set2.discard(',')
user_set2.discard('/')
user_set2.discard(';')

user_set1.symmetric_difference_update(user_set2)
user_list = list(user_set1)

print(user_list)