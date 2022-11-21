from __future__ import annotations
import code
from typing import Optional, Protocol


class ContactList(list["Contact"]):

    def search(self, name: str) -> list["Contact"]:
        matching_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    # all_contacts: List["Contact"] = []
    all_contacts = ContactList()

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" f"{self.name!r}, {self.email!r}" f")"


class LongNameDict(dict[str, int]):
    def longest_key(self) -> Optional[str]:
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone


class Emailable(Protocol):
    email: str


class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email}")


c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@sloop.net")
c3 = Contact("Jenna C", "cutty@sark.io")


# print([c.name for c in Contact.all_contacts.search('A')])


articles_read = LongNameDict()
articles_read['lucy'] = 42
articles_read['2'] = 6
articles_read['steve'] = 7
print(articles_read.longest_key())


def add_numbers(a: int, b: int, c: int) -> int:
    return a + b + c


class AddressHolder:
    def __init__(self, street: str, city: str, state: str, code: str) -> None:
        self.street = street
        self.city = city
        self.state = state
        self.code = code



class Friend(Contact, AddressHolder):
    def __init__(
        self,
        name: str,
        email: str,
        phone: str,
        street: str,
        city: str,
        state: str,
        code: str
    ) -> None:

        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
        