
import json
import time

from classdig import learner
from classdig import helper

N_TEST = 10

def run():
    try:
        with open("classdig/config.json") as filename:
            dict_config = json.load(filename)
            fp = dict_config["path"]
            m = dict_config["ndig_treino"]
            p = dict_config["p"]

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
            duracao = int(time.time() - inicio)
            print("Digito {} foi aprendido em {} s!".format(d, duracao))
        
        print("----------------------------------------------------------------------")
        print("")
        print("FASE 2: CLASSIFICACAO")
        print("")

        inicio = time.time()
        A = learner.read_test(fp,N_TEST)
        digs = helper.zero_vector(N_TEST)
        erro = helper.max_vector(N_TEST)
        for d in range(10):
            novo_erro = learner.test_images(classificadores[d], A, 784, p, N_TEST)
            for i in range(N_TEST):
                if novo_erro[i] < erro[i]:
                    erro[i] = novo_erro[i]
                    digs[i] = d
        duracao = int(time.time() - inicio)
        
        print("{} digitos classificados em {} s!".format(N_TEST, duracao))
        
        #TODO: Salvar classificacao num arquivo, no mesmo formato do test_index
        print(digs)

        print("----------------------------------------------------------------------")
        print("")
        print("FASE 3: VALIDACAO")
        print("")
        #TODO: Comparar digs com test_index e salvar percentual de acertos

    except FileNotFoundError:
        print("[ERRO] Não foi possível encontrar o arquivo")


if __name__ == "__main__":
    run()