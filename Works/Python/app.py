def foo():
    print(5)
    def bar():
        print(4)
    return bar

foo()()