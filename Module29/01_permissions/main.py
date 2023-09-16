import functools

user_permissions = ['admin', 'moder']


def check_permission(user_name):
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if user_name in user_permissions:
                func(*args, **kwargs)
            else:
                raise PermissionError('У пользователя {name} недостаточно прав для выполнения этого действия'.format(
                    name=user_name
                ))
        return wrapped_func
    return decorator


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('moder')
def add_article():
    print('Добавляем новую статью')


@check_permission('user')
def add_comment():
    print('Добавляем комментарий')


try:
    delete_site()
    add_article()
    add_comment()
except PermissionError as exc:
    print(exc)
