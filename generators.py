from faker.proxy import Faker

def generate_name():
    name_data = Faker()
    return name_data.name()


def generate_email():
    email_data = Faker()
    return email_data.email()

def generate_description():
    description_data = Faker()
    return description_data.text()


def generate_phone_1():
    phone_data = Faker()
    phone = phone_data.phone_number()
    return phone

def generate_phone_2():
    phone_data = Faker('ru_RU')
    phone = phone_data.msisdn()
    return f'+7{phone[1:11]}'

def generate_phone_3():
    phone_data = Faker('ru_RU')
    phone = phone_data.msisdn()
    return phone[1:]

def generate_long_phone():
    return "9" * 30