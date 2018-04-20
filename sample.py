import name
n=name.NameClient(username="your_username", token="your_token")

r = n.v4.hello.get()
print(r.__dict__)


