from pydantic import BaseModel
from model.animal import Animal

class AnimalSchema(BaseModel):
    """ Define como um novo animal a ser inserido deve ser representado
    """
    hair: bool = True
    feathers: bool = False
    eggs: bool = False
    milk: bool = True
    airborne: bool = False
    aquatic: bool = False
    predator: bool = True
    toothed: bool = True
    backbone: bool = True
    breathes: bool = True
    venomous: bool = False
    fins: bool = False
    legs: int = 4
    tail: bool = True
    domestic: bool = False
    catsize: bool = False

class AnimalViewSchema(BaseModel):
    """ Define como um animal será retornado
    """
    hair: bool = True
    feathers: bool = False
    eggs: bool = False
    milk: bool = True
    airborne: bool = False
    aquatic: bool = False
    predator: bool = True
    toothed: bool = True
    backbone: bool = True
    breathes: bool = True
    venomous: bool = False
    fins: bool = False
    legs: int = 4
    tail: bool = True
    domestic: bool = False
    catsize: bool = False
    type: int = 1

# Apresenta apenas os dados de um animal    
def apresenta_animal(animal: Animal):
    """ Retorna uma representação do animal seguindo o schema definido em
        AnimalViewSchema.
    """
    return {
        "hair": animal.hair,
        "feathers": animal.feathers,
        "eggs": animal.eggs,
        "milk": animal.milk,
        "airborne": animal.airborne,
        "aquatic": animal.aquatic,
        "predator": animal.predator,
        "toothed": animal.toothed,
        "backbone": animal.backbone,
        "breathes": animal.breathes,
        "venomous": animal.venomous,
        "fins": animal.fins,
        "legs": animal.legs,
        "tail": animal.tail,
        "domestic": animal.domestic,
        "catsize": animal.catsize,
        "type": animal.type
    }
