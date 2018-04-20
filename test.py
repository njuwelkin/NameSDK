import name
n=name.NameClient(username="njuwelkin-test", token="bf67556c7413d93854cd926e3a0379fed8dc34a6")

r = n.v4.hello.get()
print(r.__dict__)


