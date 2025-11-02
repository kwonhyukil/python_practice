# TypedDict -> 스키마 정의 -> dictionary -> JSON !! 히히힣

from typing import TypedDict

class UserInfo(TypedDict):
  name: str
  age: int
  gender: str

Info : UserInfo = {"name" : "Hyukil", "age" : 20, "gender" : "Man"}

Info = {"name" : "Hyukil", "age" : 20, "gender" : "Man"}

print(Info)

class user(TypedDict):
  name: str
  age: int
  gender: str
  


x = {"name" : "Hyukil", "age" : 20, "gender" : "M"}
#               str             int            str    => Schama
print(x["name"], x["age"], x["gender"])