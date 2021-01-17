from users.models import users_list


def get_users_list():
    list = users_list.objects.all()
    return list
