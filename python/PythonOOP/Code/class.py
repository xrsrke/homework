# import math


# class Point:

#     def __init__(self, x:float = 0, y:float = 0) -> None:
#         self.move(x, y)

#     def move(self, x: float, y: float) -> None:
#         self.x = x
#         self.y = y

#     def reset(self) -> None:
#         self.x = 0
#         self.y = 0

    
#     def calculate_distance(self, other: "Point") -> float:
#         return math.hypot(self.x - other.x, self.y - other.y)


# point1 = Point()
# point2 = Point()

# point1.reset()
# point2.move(5, 0)

# print(point2.calculate_distance(point1))


# assert point2.calculate_distance(point1) != point1.calculate_distance(point2), "wrong broadcast distance"

# point = Point(3)
# print(point.x, point.y)
#print(object)


class MySubClass(object):
    pass


class Contact:
    # all_contacts: List["Contact"] = []
    all_contacts = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" f"{self.name!r}, {self.email!r}" f")"


class Supplier(Contact):
    def order(self, order: "Order") -> None:
        print("If this were a real system, we would send "
            f"'{order} order to '{self.name}'"
        )


c = Contact("Some Body", "somebody@example.net")
s = Supplier("Sup Plier", "supplier@example.net")
print(c.name, c.email, s.name, s.email)

from pprint import pprint
pprint(c.all_contacts)

# c.order("I need pliers")
s.order("I need pliers")


print(Contact.all_contacts)