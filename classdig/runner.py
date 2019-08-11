
import numpy as np
import json
import time

from sys import float_info

from classdig import learner


def run():
    try:
        with open("classdig/config.json") as filename:
            dict_config = json.load(filename)
            fp = dict_config["path"]
            m = dict_config["ndig_treino"]
            p = dict_config["p"]
            n_test = dict_config["n_test"]
       
        print("  ndig_treino = {}".format(m))
        print("            p = {}".format(p))
        
        inicio = time.time()

        classificadores = dict()
        for d in range(10):
            print("Aprendendo {0} ...".format(d))
            classificadores[d] = learner.train_dig(fp, d, m, p)
            print(" {0:d} foi aprendido.".format(d))
    
        A = learner.read_test(fp,n_test)
        digs = np.zeros(n_test)
        erro = np.repeat(float_info.max, n_test)
        for d in range(10):
            print("Classificando {0} ...".format(d))
            novo_erro = learner.test_images(classificadores[d], A, 784, p, n_test)
            for i in range(n_test):
                if novo_erro[i] < erro[i]:
                    erro[i] = novo_erro[i]
                    digs[i] = d

        print(" {0:d} digitos classificados.".format(n_test))
        print("\nTempo da execução: {0:.2f} s.\n".format(time.time() - inicio))

        summary = learner.statistics(fp, digs, n_test)
        
        print("Resultado:\n")
        print("{0},{1},{2}".format("d", "total", "acertos"))
        for d in range(10):
            print("{0:d},{1:d},{2:d}".format(d, summary[d]["total"], summary[d]["acertos"]) )

    except FileNotFoundError:
        print("[ERRO] Não foi possível encontrar o arquivo")


if __name__ == "__main__":
    run()