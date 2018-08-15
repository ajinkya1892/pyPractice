def print_two(*args):
	arg1,arg2=args
	print " arg1: %r,arg2: %r"%(arg1,arg2)

def print_again(arg1,arg2):
	print " arg1: %r,arg2: %r"%(arg1,arg2)

def print_one(arg1):
	print " arg1: %r"%(arg1)

def print_none():
	print " I print nothing"


print_two("hello","Mr")
print_again("maria","maria")
print_one("aji!!!")
print_none()