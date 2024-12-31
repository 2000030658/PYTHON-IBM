from abc import ABC, abstractmethod

class Accouns:
    def bank(self):
        print("ABC Bank")

class Loan(ABC):
    @abstractmethod
    def pl(self):
        pass
        print("Savings account")

    def hl(self):
        print("Home loans")

class Final(Loan):
    def pl(self):
        print("Savings account")

o1 = Final()
o1.pl()
o1.hl()
o2=Accouns()
o2.bank()