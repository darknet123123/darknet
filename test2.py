from account.models import Code

answer = input('Введите код: ')
if Code.objects.filter(code=answer).exists():
    print('yes')
else:
    print('no')