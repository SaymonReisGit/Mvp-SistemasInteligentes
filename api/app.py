from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
animal_tag = Tag(name="Animal", description="Predição de tipo de Animal")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de classificação de animal
@app.post('/animal', tags=[animal_tag],
          responses={"200": AnimalSchema, "400": ErrorSchema, "409": ErrorSchema})
def add_animal(form: AnimalSchema):
    """Realiza a predição do tipo de animal
    Retorna uma representação do animal e seu tipo associado.

    Args:
        hair (bool): possui pelos
        feathers (bool): possui penas
        eggs (bool): põe ovos
        milk (bool): produz leite
        airborne (bool): é capaz de voar
        aquatic (bool): vive na água
        predator (bool): é predador
        toothed (bool): possui dentes
        backbone (bool): possui coluna vertebral
        breathes (bool): respira
        venomous (bool): é venenoso
        fins (bool): possui barbatanas
        legs (int): número de pernas
        tail (bool): possui cauda
        domestic (bool): é domesticado
        catsize (bool): possui tamanho similar a um gato


    Returns:
        type (int): tipo de animal (ex: mamífero, réptil, etc.)
    """
    
    # Recuperando os dados do formulário
    hair = form.hair
    feathers = form.feathers
    eggs = form.eggs
    milk = form.milk
    airborne = form.airborne
    aquatic = form.aquatic
    predator = form.predator
    toothed = form.toothed
    backbone = form.backbone
    breathes = form.breathes
    venomous = form.venomous
    fins = form.fins
    legs = form.legs
    tail = form.tail
    domestic = form.domestic
    catsize = form.catsize

    # Preparando os dados para o modelo de predição
    X_input = PreProcessador.preparar_form(form)  # Ajustar para o contexto de animais
    # Carregando modelo de machine learning
    model_path = 'MachineLearning/pipelines/zoo_pipeline.pkl'
    modelo = Pipeline.carrega_pipeline(model_path)
    
    # Realizando a predição (classificação do animal)
    predicted_type = int(Model.preditor(modelo, X_input)[0])

    # Criando a instância do Animal com a predição
    animal = Animal(
        hair=hair,
        feathers=feathers,
        eggs=eggs,
        milk=milk,
        airborne=airborne,
        aquatic=aquatic,
        predator=predator,
        toothed=toothed,
        backbone=backbone,
        breathes=breathes,
        venomous=venomous,
        fins=fins,
        legs=legs,
        tail=tail,
        domestic=domestic,
        catsize=catsize,
        type=predicted_type  # Resultado da predição
    )
    
    logger.debug(f"Animal classificado como: '{predicted_type}'")
    
    try:
        # Retorna a representação do animal
        return apresenta_animal(animal), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Error ao classificar animal"
        logger.warning(f"Erro ao classificar animal: {error_msg}")
        return {"message": error_msg}, 400

if __name__ == '__main__':
    app.run(debug=True)