def dec_fn(fn):
    def inner_fn(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fn



@dec_fn
def sub(n1,n2):
    return n1-n2
@dec_fn
def div(n1,n2):
    return n1/n2
print(sub(10,30))
print(sub(10,4))
print(div(30,60))
print(sub(30,10))