def age_dictionary():
    d = {}
    while True:
        person_name = input(
            'Enter name of the person (To stop do not enter anything and hit Enter key): ')
        if person_name == '':
            break
        person_age = int(input('Enter age: '))
        d[person_name] = person_age

    print('Building dictionary is complete. Now enter name of the person and i will tell his/her age')
    while True:
        person_name = input(
            'Enter name of the person (To stop do not enter anything and hit Enter key): ')
        if person_name == '':
            break
        if person_name in d:
            print('Age of name', person_name, 'is:', d[person_name])
        else:
            print('I do not know the age of:', person_name)
    print("Age Dictionary program is finished now.")


age_dictionary()
