class PlayerCharacter:
    def __init__(self, name='Tuffy', life=0):
        if(life>0):
            self.name = name
            self.life = life

    def run(self):
        print('running')
        return 'ok'

    def returnSefl(self):
        return self

p1 = PlayerCharacter('Django',2) # if we don't pass life, it errors out

print(p1)
print(p1.name)
print(p1.life)
print(p1.run())
print(p1.returnSefl())