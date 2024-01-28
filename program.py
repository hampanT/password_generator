import secrets
import string
import random
import pyperclip



chars_lower = string.ascii_lowercase
chars_upper = string.ascii_uppercase
numbers =  [0,1,2,3,4,5,6,7,8,9]
spec_chars = "!@#$%^&*()_-+=<>?"
password = ''

element_list = [chars_lower, chars_upper, numbers, spec_chars]
loops = secrets.choice(range(12,14))



#metod som först lägger till 1 slumpad sak per lista
#sen shufflar vi runt valen så att de inte är i samma ordning varje gång
def all_list():
    global password
    password += secrets.choice(chars_lower)
    password += secrets.choice(chars_upper)
    password += str(secrets.choice(numbers))
    password += secrets.choice(spec_chars)

    shuffle_password = list(password)
    random.shuffle(shuffle_password)
    password = "".join(shuffle_password)

    return password


password += all_list()

for iterations in range (loops):
    test = secrets.choice(element_list)
    addition = secrets.choice(test)
    password += str(addition) 


pyperclip.copy(password)

print(f'Här är ditt lösenord: {password}')
print('Lösenordet har sparats till din clipboard :D')



#kolla på denna https://www.youtube.com/watch?v=jnUpSK3D3is&t=1s






