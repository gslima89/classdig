# classdig
Fatoração de Matrizes para Sistemas de Classificação de Machine Learning

## Introdução

Algoritmo proposto por um exercício-programa cujo enunciado está disponível em [aqui](https://www.ime.usp.br/~map3121/2019/map3121/programas/EP1-MachineLearning_v2.pdf).


## Pré-requisitos

- Python 3.7
- Numpy!
- Arquivos com os dígitos disponíveis [aqui](https://www.ime.usp.br/~pedrosp/dados_mnist.zip)

## Execução

A execução padrão utiliza a classe runner,

```python

from classdig import runner

classdig.runner.run()

```

É possível executar diretamente através do comando, no diretório raiz do pacote:

```python

python -m runner

```

Os parâmetros de configuração estão disponíveis no arquivo config.json, com o seguinte formato

```json

{
    "path": "C:\\dados_mnist\\",
    "ndig_treino": 100,
    "p": 5,
    "n_test": 10000
}

```

onde: 

- path : caminho no qual os arquivos estão disponíveis
- ndig_treino : números de dígitos utilizados no treinamento
- p : número de colunas da matriz W utilizada na decomposição A = WH
- n_test : número de dígitos utilizados no teste (max 10000)

## Resultados

Foram obtidos os seguintes percentuais de acerto, em função de p e ndig_treino:




| p \ n   | 100         | 1000   | 4000   |
|----|-------------|--------|--------|
| **5**  | 88.59%      | 90.85% | 91.71% |
| **10** | 89.76%      | 93.03% | 93.01% |
| **15** | 90.82%      | 93.68% | 94.01% |

## Referencias

- Base de dígitos manuscritos MNIST: http://yann.lecun.com/exdb/mnist/