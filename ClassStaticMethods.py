class PlayerCharacter:
    def __init__(self, name='Tuffy', life=0):
        if(life>0):
            self.name = name
            self.life = life

    @classmethod
    def adding_things(cls,num1, num2):
        return cls('Tony', num1+num2)

player1 = PlayerCharacter.adding_things(2,3)
print(player1)
print(player1.name)
print(player1.life)
