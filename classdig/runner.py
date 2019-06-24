
import json

from classdig import learner

def run():
    try:
        with open("classdig/config.json") as filename:
            dict_config = json.load(filename)
            fp = dict_config["path"]
            m = dict_config["ndig_treino"]
            p = dict_config["p"]

        learn_book = dict()
        print("Inicio da aprendizagem com ndig_treino = {0} e p = {1}".format(m, p))
        for d in range(10):
            learn_book[d] = learner.train_dig(fp, d, m, p,itmax=10)
            print("Digito {} foi aprendido!".format(d))

    except FileNotFoundError:
        print("ERRO: não foi possível encontrar o arquivo")

if __name__ == "__main__":
    run()