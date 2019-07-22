
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
    
    except FileNotFoundError:
        print("[ERRO] Não foi possível encontrar o arquivo de configuração")

    print("FASE 1: APRENDIZAGEM")
    print("")
    print("ndig_treino = {}".format(m))
    print("          p = {}".format(p))
    print("")
    
    classificadores = dict()
    for d in range(10):
        print("Aprendendo {} ...".format(d))
        inicio = time.time()
        classificadores[d] = learner.train_dig(fp, d, m, p, itmax=10)
        duracao = time.time() - inicio
        print("Digito {} foi aprendido em {} s!".format(d, duracao))
    
    print("----------------------------------------------------------------------")
    print("")
    print("FASE 2: CLASSIFICACAO")
    print("")

    inicio = time.time()

    A = learner.read_test(fp,n_test)
    digs = np.zeros(n_test)
    erro = np.repeat(float_info.max, n_test)
    for d in range(10):
        novo_erro = learner.test_images(classificadores[d], A, 784, p, n_test)
        for i in range(n_test):
            if novo_erro[i] < erro[i]:
                erro[i] = novo_erro[i]
                digs[i] = d

    duracao = time.time() - inicio
    
    print("{} digitos classificados em {} s!".format(n_test, duracao))
    
    print("----------------------------------------------------------------------")
    print("")
    print("FASE 3: RESULTADO")
    print("")
    summary = learner.statistics(fp, digs, n_test)
    print(summary)


if __name__ == "__main__":
    run()