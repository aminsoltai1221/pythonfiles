print("hi dear")
x=2.0/11.0
print(x)

print(repr("hi dear"))
print(repr(2.0/11.0))

class Person:
    def __init__(self,name) -> None:
        self.name=name
    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return  f"{self.name}"
ali=Person("ali")
print(ali)