class Animal():

    def __init__(self, 
                    hair:bool,
                    feathers:bool,
                    eggs:bool,
                    milk:bool,
                    airborne:bool,
                    aquatic:bool,
                    predator:bool,
                    toothed:bool,
                    backbone:bool,
                    breathes:bool,
                    venomous:bool,
                    fins:bool,
                    legs:int,
                    tail:bool,
                    domestic:bool,
                    catsize:bool,
                    type:int):
        """
            Cria um Animal

            Arguments:
            hair: possui pelos (True ou False)
            feathers: possui penas (True ou False)
            eggs: põe ovos (True ou False)
            milk: produz leite (True ou False)
            airborne: capaz de voar (True ou False)
            aquatic: vive na água (True ou False)
            predator: é um predador (True ou False)
            toothed: possui dentes (True ou False)
            backbone: possui coluna vertebral (True ou False)
            breathes: respira (True ou False)
            venomous: é venenoso (True ou False)
            fins: possui barbatanas (True ou False)
            legs: número de pernas (inteiro)
            tail: possui cauda (True ou False)
            domestic: é domesticado (True ou False)
            catsize: tem tamanho de gato (True ou False)
            type: tipo do animal (classificação em inteiro)
        """
        self.hair = hair
        self.feathers = feathers
        self.eggs = eggs
        self.milk = milk
        self.airborne = airborne
        self.aquatic = aquatic
        self.predator = predator
        self.toothed = toothed
        self.backbone = backbone
        self.breathes = breathes
        self.venomous = venomous
        self.fins = fins
        self.legs = legs
        self.tail = tail
        self.domestic = domestic
        self.catsize = catsize
        self.type = type
