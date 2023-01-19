# import requests
# requests.get('http://127.0.0.1:8000/account/register/')

def register_link():
    import time
    from django.utils.crypto import get_random_string
    starttime = time.time()
    while True:
        time.sleep(3.0 - ((time.time() - starttime) % 3.0))
        string = get_random_string(8, '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
        register_link = f'register/{string}/'
        print(register_link)

gg = register_link()