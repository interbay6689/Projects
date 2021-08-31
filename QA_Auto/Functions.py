
def login_name_generator(length):
    import string, random

    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return 'qqtst_' + result_str


def email_generator(length):
    import string, random
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return str(result_str)


def password_generator():
    return 'Aa123456'


def zip_code_generator():
    import random
    zip_code_g = str(random.randint(100000, 1000000))
    return zip_code_g


def mobile_generator():
    import random
    mobile = '33-' + str(random.randint(1000000, 10000000))
    return mobile


def city_generator(length):
    import string, random
    letters = string.ascii_lowercase
    city = ''.join(random.choice(letters) for i in range(length))
    return city

# def random_mail_func(ran_mail_var, ):
#     if ran_mail_var.get() == 1:
#         mail_var.set(func_var.email_generator(7))
#         mail_input.config(state=DISABLED)
#     else:
#         mail_input.config(state=NORMAL)
#         mail_var.set('')
