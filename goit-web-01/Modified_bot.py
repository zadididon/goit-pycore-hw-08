from abc import ABC, abstractmethod
from functools import wraps
from collections import UserDict
from datetime import datetime
import pickle

class UserInterface(ABC):
    @abstractmethod
    def show_message(self, message):
        pass

    @abstractmethod
    def get_input(self, prompt):
        pass

class ConsoleInterface(UserInterface):
    def show_message(self, message):
        print(message)

    def get_input(self, prompt):
        return input(prompt)

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except KeyError:
            return "Enter contact name."
        except IndexError:
            return "Check the phone number."
    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            date = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

def main():
    interface = ConsoleInterface()
    address_book = AddressBook()
    interface.show_message("Welcome to the assistant bot!")
    
    while True:
        user_input = interface.get_input("Enter a command: ")
        command, *args = user_input.split()
        command = command.lower()
        
        if command in {"close", "exit"}:
            interface.show_message("Good bye!")
            break
        elif command == "hello":
            interface.show_message("How can I help you?")
        elif command == "all":
            interface.show_message(str(address_book))
        else:
            interface.show_message("Invalid command.")

if __name__ == "__main__":
    main()