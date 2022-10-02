from typing import List, NoReturn, Union

def never_returns() -> NoReturn:
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("I hope I will be execute")
    return "Would I be returned?"


def call_exceptor() -> None:
    print("call exceptor starts here")
    never_returns()
    print("abc")
    print("call exceptor ends here")


# call_exceptor()


# class EvenOnly(List[int]):
#     def append(self, value: int) -> None:
#         if not isinstance(value, int):
#             raise TypeError('Only integers can be added')
#         if value % 2:
#             raise ValueError('Only even numbers can be added')
#         super().append(value)


def funny_division(divisor: float) -> Union[str, float]:
    try:
        return 42 / divisor
    except ZeroDivisionError:
        return "You can't divide by zero!"


print(funny_division('asdas'))
