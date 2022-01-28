import random

characterSet = {
1: 'abcdefghijklmnopqrstuvwxyz', #lower Case
2: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', #Upper Case
3: '0123456789', #digit
4: '.!"#$%&()*+,-/:;<=>>@[]^_`{|}~' #special character
}

def random_Password():
    length = ask_length()
    special = ask_special()
    password = list()
    counter = 0
    if special:
        while counter < length:
            key = random.randint(1, 4)
            password.append(characterSet[key][random.randint(0, (len(characterSet[key])-1))])
            counter += 1
    else:
        while counter < length:
            key = random.randint(1, 3)
            password.append(characterSet[key][random.randint(0, (len(characterSet[key])-1))])
            counter += 1
    print("Your generated password of {0} characters long: ".format(length) + ''.join(password))
    x = input(r'press Enter to exit this program ')
    return ''.join(password)


def ask_length():
    length = input('How long do you want your password to be? (enter a number) ')
    try:
        length = int(length)
    except ValueError:
        print('ValueError: Please entter an integer.')
        ask_length()
    return length

def ask_special():
    default_answers = ["Y", "N"]  
    special = input('Do you want special characters in your password? (Y/N)').upper()
    if special not in default_answers:
        print('please enter a valid response(ex: Y for yes, N for no)')
        ask_special()
    return special == "Y"


random_Password()
