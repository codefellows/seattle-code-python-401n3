class ForceUser:
    def attacking(self):
        return f'{self.name} is Force attacking!'

    def getting_hit(self):
        return f'{self.name} is being attacked!'

    @classmethod
    def get_count(cls):
        return JediMaster.count + SithLord.count

class JediMaster(ForceUser):

    count = 0
    
    def __init__(self, name = 'Random Master'):
        self.name = name
        JediMaster.count += 1

    def __str__(self):
        return f'{self.name} is in the House!'
    
    def __repr__(self):
        return f'JediMaster( "{self.name}" )'

    def attacking(self):
        return f'{self.name} is Good Force attacking!'

    @staticmethod
    def code():
        return "There is no emotion, there is PEACE."

    @classmethod
    def get_count(cls):
        return cls.count


class SithLord(ForceUser):

    count = 0

    def __init__(self, name = 'Random Master'):
        self.name = name
        SithLord.count += 1

    @staticmethod
    def code():
        return "Peace is a lie, there is only PASSION."

    @classmethod
    def get_count(cls):
        return cls.count





# if __name__ == '__main__':
    yoda = JediMaster('Yoda')
    print(yoda.__repr__)
    # quigon = JediMaster('QuiGon')
    # print(quigon.code())
    # print(quigon.getting_hit())
    # yoda = JediMaster('Yoda')
    # print(yoda.attacking())
    # print(quigon.getting_hit())
