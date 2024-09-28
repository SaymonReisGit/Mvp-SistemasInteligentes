# Machine Learning - MVP - Classificação de Animais
## Desenvolvido por Saymon Reis

Este projeto tem como objetivo a classificação de animais com base em suas características físicas e comportamentais. Utilizamos um dataset que contém informações detalhadas sobre diversos animais, permitindo a aplicação de técnicas de aprendizado de máquina para categorizá-los em sete tipos diferentes.

## Descrição do Dataset

O dataset é composto por 17 atributos, sendo 16 relacionados a características dos animais e 1 coluna de classe (`type`), que define a categoria do animal. Cada instância no dataset representa um animal identificado por seu nome.

### Atributos do Dataset:

- `animal name`: Nome único de cada animal.
- `hair`: Indica se o animal possui pelos (Booleano).
- `feathers`: Indica se o animal possui penas (Booleano).
- `eggs`: Indica se o animal põe ovos (Booleano).
- `milk`: Indica se o animal produz leite (Booleano).
- `airborne`: Indica se o animal pode voar (Booleano).
- `aquatic`: Indica se o animal vive na água (Booleano).
- `predator`: Indica se o animal é predador (Booleano).
- `toothed`: Indica se o animal tem dentes (Booleano).
- `backbone`: Indica se o animal possui espinha dorsal (Booleano).
- `breathes`: Indica se o animal respira (Booleano).
- `venomous`: Indica se o animal é venenoso (Booleano).
- `fins`: Indica se o animal possui nadadeiras (Booleano).
- `legs`: Número de pernas do animal (Valores possíveis: 0, 2, 4, 5, 6, 8).
- `tail`: Indica se o animal possui cauda (Booleano).
- `domestic`: Indica se o animal é domesticado (Booleano).
- `catsize`: Indica se o animal é de porte semelhante ao de um gato (Booleano).
- `type`: Atributo de classe que categoriza os animais em sete grupos distintos, representados por valores inteiros de 1 a 7.

### Classes de Animais:

O atributo `type` classifica os animais nos seguintes grupos:

- **Tipo 1: Mamíferos** (41 animais) - Exemplo: urso, elefante, gato doméstico.
- **Tipo 2: Aves** (20 animais) - Exemplo: galinha, pinguim, falcão.
- **Tipo 3: Répteis** (5 animais) - Exemplo: víbora, tartaruga.
- **Tipo 4: Peixes** (13 animais) - Exemplo: robalo, atum, cavalo-marinho.
- **Tipo 5: Anfíbios** (4 animais) - Exemplo: rã, sapo.
- **Tipo 6: Insetos** (8 animais) - Exemplo: pulga, abelha, joaninha.
- **Tipo 7: Invertebrados** (10 animais) - Exemplo: polvo, estrela-do-mar, verme.

## Objetivo do Projeto

O principal objetivo deste projeto é desenvolver um modelo de machine learning capaz de classificar animais em seus respectivos tipos, com base em seus 17 atributos. Isso pode facilitar a categorização de novos animais e oferecer uma melhor compreensão sobre suas características e semelhanças com outras espécies já conhecidas.
