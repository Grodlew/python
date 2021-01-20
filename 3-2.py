def my_func(name=None, f_name=None, date_of_birth=None, city=None, email=None, phone_num=None):
    print(f'{name} {f_name} {date_of_birth} года рождения, проживает в городе {city}. Адрес почты: {email}, телефон: '
          f'{phone_num}')


my_func(name='Василий', f_name='Пупкин', date_of_birth=1976, city='Бобруйск', email='v.pupkin@gmail.com',
        phone_num=89123456789)
