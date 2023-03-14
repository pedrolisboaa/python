class Pessoa:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def say_name(self):
        print(f'Ola meu nome é {self.name}. Minha classe é {self.__class__.__name__}')


class Teacher(Pessoa):
    ...


class Student(Pessoa):
    ...


teacher1 = Teacher('Rosangela', 'Nascimento')
student1 = Student('Pedro', 'Lisboa')

teacher1.say_name()
student1.say_name()
