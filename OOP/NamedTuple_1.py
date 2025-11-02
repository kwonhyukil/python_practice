from typing import Final, NamedTuple, final

class User(NamedTuple):
  name: str
  age: int
  gender: str
  
u1 = User("Hyukil", 26, "Man")

print(u1.name, u1.age, u1.gender)

def create_user(name: str, age: int, gender: str) -> User:
  return User(name, age, gender)

name, age, gender = create_user("Hyukil", 26, "Man")

print(name, age, gender) 

X : Final = 3.14159
X = 12312312
