# The Color class represents a color with a name and an RGB value.
# class Color:
#     def __init__(self, rgb_value: int, name: str) -> None:
#         self._rgb_value = rgb_value
#         self._name = name
    
#     def set_name(self, name: str) -> None:
#         self._name = name
    
#     def get_name(self) -> str:
#         return self._name
    
#     def set_rgb_value(self, rgb_value: int) -> None:
#         self._rgb_value = rgb_value

#     def get_rgb_value(self) -> int:
#         return self._rgb_value


# c = Color(0xff0000,"bright red")
# print(c.get_name())

# c.set_name("red")
# print(c.get_name())


# class Color_V:
#     def __init__(self, rgb_value: int, name: str) -> None:
#         self._rgb_value = rgb_value
#         if not name:
#             raise ValueError(f"Invalid name {name!r}")
#         self._name = name

#     def set_name(self, name:str) -> None:
#         if not name:
#             raise ValueError(f"Invalid name {name!r}")
#         self._name = name




# class Color_VP:
#     def __init__(self, rgb_value: int, name: str) -> None:
#         self._rgb_value = rgb_value
#         if not name:
#             raise ValueError(f"Invalid name {name!r}")
#         self._name = name
    
#     def _set_name(self, name: str) -> None:
#         if not name:
#             raise ValueError(f"Invalid name {name!r}")
#         self._name = name
    
#     def _get_name(self):
#         print("hello")
#         return self._name
    
#     name = property(_get_name, _set_name)

# c = Color_VP(0xff0000, "bright red")
# print(c.name)


class NorwegianBlue:
    def __init__(self, name:str) -> None:
        self._name = name
        self._state: str
    
    def _get_state(self) -> str:
        print(f"Getting {self._name}'s State")
        return self._state
    
    def _set_state(self, state:str) -> None:
        print(f"Setting {self._name}'s State to {state!r}'")
        self._state = state
    
    def _del_state(self) -> None:
        print(f"{self._name} is pushing up daisies")
        del self._state
    
    silly = property(_get_state, _set_state, _del_state, "this is a silly property")

# p = NorwegianBlue("Polly")
# p.silly = "XR5"
# print(p.silly)

# del p.silly


class NorwegianBlue_P:
    def __init__(self, name: str) -> None:
        self._name = name
        self._state: str
    
    @property
    def silly(self) -> str:
        """This is a silly property"""
        print(f"Getting {self._name}'s State")
        return self._state
    
    @silly.setter
    def silly(self, state: str) -> None:
        print(f"Setting {self._name}'s State to {state!r}'")
        self._state = state

from urllib.request import urlopen
from typing import Optional, cast

class WebPage:
    def __init__(self, url: str) -> None:
        self._url = url
        self._content: Optional[bytes] = None
    
    @property
    def content(self) -> bytes:
        if self._content is None:
            print("Retrieving New Page...")
            with urlopen(self._url) as response:
                self._content = response.read()
        return self._content

import time

webpage = WebPage("http://www.python.org")
now = time.perf_counter()
content1 = webpage.content
first_fetch = time.perf_counter() - now

now = time.perf_counter()
content2 = webpage.content
second_fetch = time.perf_counter() - now

assert content2 == content1
print(f"Initial Request {first_fetch:.5f}")
print(f"Subsequent Request {second_fetch:.5f}")
