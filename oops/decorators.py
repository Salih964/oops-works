

def swap_dec(fn):

    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    return wrapper   

@swap_dec
def sub(n1,n2):
    return n1-n2 #largest-smallest

@swap_dec
def div(n1,n2):
    return n1/n2

print(sub(15,10))

print(div(2,10))


def greeting_dec(fn):

    def wrapper(name):
        result=fn(name)
        return f"Hello Programmer{result}"
    return wrapper

@greeting_dec
def afternoon_greeting(name):
        return f"{name} good after noon"

@greeting_dec
def morning_greeting(name):
    return f"{name} good morning"        

print(morning_greeting("sai"))
print(afternoon_greeting("vipin"))