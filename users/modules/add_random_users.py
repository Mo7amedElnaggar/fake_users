from os import environ
import django
from faker import Faker
import random
from users.models import users_list

faker_instance = Faker()


def add_user():
    first_name = faker_instance.first_name()
    last_name = faker_instance.last_name()
    email = faker_instance.email()

    new_user = users_list.objects.create(
        first_name=first_name, last_name=last_name, email=email)

    return new_user


def start_adding_users(N=10):

    for index in range(N):
        add_user()


if __name__ == "__main__":
    print("Script is Working")
    start_adding_users(10)
    print("Script Finished work done !")
