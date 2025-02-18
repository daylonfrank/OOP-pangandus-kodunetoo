# -----------------------------
# KONSPEKT
# -----------------------------
# See programm simuleerib pangasüsteemi kasutades objektorienteeritud programmeerimist (OOP).
# Programm koosneb kahest klassist:
# 1. User - põhiandmete (nimi, vanus, sugu) haldauseks.
# 2. Bank - kasutaja pangakonto haldamiseks (sissemaksed, väljamaksed, saldo vaatamine).
# Bank klass pärib omadused User klassilt, kasutades inheritance-i.
# Programm võimaldab kasutajatel oma isiklikke andmeid vaadata ning raha oma kontole lisada või sealt välja võtta.
# -----------------------------

# Kasutaja klass, mis salvestab põhiandmed (nimi, vanus, sugu)
class User():
    def __init__(self, name, age, gender):
        self.name = name  # Kasutaja nimi
        self.age = age  # Kasutaja vanus
        self.gender = gender  # Kasutaja sugu

    # Meetod, mis kuvab kasutaja andmed
    def show_details(self):
        print("Personal Details")  
        print("")  
        print("Name ", self.name)  
        print("Age ", self.age)  
        print("Gender ", self.gender)  


# Panga klass, mis pärib User klassilt (kasutaja andmed + pangakonto haldus)
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)  # Kutsub välja User konstruktori
        self.balance = 0  # Algne konto saldo on 0

    # Meetod, mis võimaldab kasutajal raha oma kontole lisada
    def deposit(self, amount):
        self.amount = amount  # Sissemakse summa
        self.balance = self.balance + self.amount  # Lisab summa saldole
        print("Account balance has been updated : £", self.balance)  # Kuvab uuendatud saldo

    # Meetod, mis võimaldab kasutajal raha oma kontolt välja võtta
    def withdraw(self, amount):
        self.amount = amount  # Väljamakse summa
        if self.amount > self.balance:  # Kontrollib, kas kontol on piisavalt raha
            print("Insufficient Funds | Balance Available : £", self.balance)  # Kui pole piisavalt raha, kuvab hoiatuse
        else:
            self.balance = self.balance - self.amount  # Lahutab summa saldost
            print("Account balance has been updated : £", self.balance)  # Kuvab uuendatud saldo

    # Meetod, mis kuvab kasutaja andmed ja konto saldo
    def view_balance(self):
        self.show_details()  # Kuvab kasutaja andmed
        print("Account balance: £", self.balance)  # Kuvab kontojäägi
