from abc import ABC,abstractmethod


class Musician():
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def get_instrument(self):
        return str()

    @abstractmethod
    def play_solo(self):
        pass

class Band(Musician):
    def __init__(self,name,list):
        self.name=name
        self.members=list
    def play_solos():
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def to_list():
        return members

    def play_solo(self):
        pass    


    @classmethod    
    def to_list(self):
        pass



class Guitarist(Musician):
    
    def get_instrument(self):
        return "guitar"
    def __str__(self):
        return f"My name is {self.name} and I play guitar"
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    def get_instrument(self):
        return "bass"
    def __str__(self):
        return f"My name is {self.name} and I play bass"
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    def get_instrument(self):
        return "drums"
    def __str__(self):
        return f"My name is {self.name} and I play drums"
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def play_solo(self):
        return "rattle boom crash"

