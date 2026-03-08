
def person(**data):
    print(data)

    for i,j in data.items():
        print(i,j)

person(name='Amit',age=20,mob=9883178750)