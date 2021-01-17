from django.shortcuts import render
from .modules import add_random_users, get_users


def open_users_list(request):
    # create a faker list of users { first_name , last_name , email}
    # add_random_users.start_adding_users()
    return render(request, 'users/index.html', context={'users': get_users.get_users_list()})
