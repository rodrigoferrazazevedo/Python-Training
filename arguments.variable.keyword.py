def func(**kwargs):
    print(kwargs)

func(a=1, b=42)
func(**{'a':1, 'b':42})
func(**dict(a=1,b=42))
