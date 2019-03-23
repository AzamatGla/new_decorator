def try_except(fn):
    def wrapped():
        try:
            fn()
        except Exception as e:
            print('Exception: ', e)


    return wrapped


class User():

    @try_except
    def get_account_balance():
        return username

    @try_except
    def change_password():
        return password

u = User
u.get_account_balance()
