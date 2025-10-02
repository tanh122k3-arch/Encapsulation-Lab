#Bai1
class Person:
        def __init__(self,name,age):
                self.__name=name
                self.__age=age
        def get_name(self):
                return self.__name
        def get_age(self):
                return self.__age
person=Person("George",32)
print(person.get_name())
print(person.get_age())
#Bai2
class EmailValidator:
    def __init__ (self, min_length, mails,domains):
        self.min_length=min_length
        self.mails=mails
        self.domains=domains
    def __validate_name(self,name):
        return len(name)>=self.min_length
    def __validate_mail(self,mails):
         return mails in self.mails
    def __valiadate_domain(self,domains):
        return domains in self.domains
    def validate(self,email):
        try:
            user,mail_domain=email.split("@")
            mail,domain=mail_domain.split(".")
        except ValueError:
            return False
        if self.__validate_name(user) and self. __validate_mail(mail) and self.__valiadate_domain(domain):
            return True
        else:
            return False
mails=["gmail","softuni"]
domains=["com","bg"]
mailcheck=EmailValidator(6,mails,domains)
print(mailcheck.validate("theanh123@gmail.com"))
print(mailcheck.validate("hej@gmail.com"))
#bai3
class Mammal:
    __kingdom="animal"
    def __init__ (self,name,type,sound):
        self.name=name
        self.type=type
        self.sound=sound
    def make_sound(self):
        return f"{self.name} makes {self.sound}"
    def info(self):
        return f"{self.name} is of typr{self.type}"
    def get_kingdom(self):
        return Mammal.__kingdom
mm=Mammal("Dof","domestic","bark")
print(mm.make_sound())
print(mm.get_kingdom())
print(mm.info())
#Bai4
class Account:
  def __init__(self, id, balance, pin):
    self.__id = id
    self.balance = balance
    self.__pin = pin

  def get_id(self, pin):
      if pin == self.__pin:
        return self.__id
      return "Wrong pin"

  def change_pin(self, old_pin, new_pin):
    if old_pin == self.__pin:
      self.__pin = new_pin
      return "Pin changed"
    return "Wrong pin"

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))