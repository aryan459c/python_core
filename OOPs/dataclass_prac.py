from dataclasses import dataclass


@dataclass
class Calcu:
    name: str
    age: int
    domain: str

    def user_name(self):
        print(person1)


person1 = Calcu('Sunil Kumar Maharana', 23, 'PAT')
person2 = Calcu('Aryan', 29, 'Automatyion Test Engineer')

person1.user_name()
