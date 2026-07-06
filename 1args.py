def fun(*args):
    for i in args:
        print(i)

fun('rimlee','i','love','you')


def fun1(**args):
    for i,j in args.items():
        print(f'{i}={j}')

fun1(name='Ananta',age=27)
