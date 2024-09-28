from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "MachineLearning/data/dataset_zoo.csv"
colunas = ['hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize', 'type']

# Carga dos dados
dataset = Carregador.carregar_dados(url_dados, colunas)
array = dataset.values
X = array[:,:-1]
y = array[:,-1]
    
# Método para testar pipeline ExtraTrees a partir do arquivo correspondente
def test_modelo_rf():
    # Importando pipeline de ExtraTrees
    rf_path = 'MachineLearning/pipelines/et_zoo_pipeline.pkl'
    modelo_rf = Pipeline.carrega_pipeline(rf_path)

    # Obtendo as métricas do ExtraTrees
    acuracia_rf = Avaliador.avaliar(modelo_rf, X, y)
    
    # Testando as métricas do ExtraTrees
    assert acuracia_rf >= 0.90
    

