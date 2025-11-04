from faker import Faker

fake = Faker("ru_RU")

print(fake.name())  # Выведет: John Doe
print(fake.address())  # Выведет: 1234 Elm St, Springfield, IL
print(fake.email())  # Выведет: j.doe@example.com

user_data = {"name": fake.name(), "email": fake.email(), "address": fake.address()}

print(user_data)
