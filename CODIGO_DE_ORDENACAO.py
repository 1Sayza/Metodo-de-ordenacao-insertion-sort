import os, sys, time
from datetime import datetime
import ordenacao_lib

# ----------------------------------------------------------------------
# Documentação: https://docs.python.org/3/library/time.html
# Documentação: https://docs.python.org/3/library/datetime.html
# ----------------------------------------------------------------------

# Obtendo o diretório (caminho) do arquivo .py
diretorio = os.path.dirname(os.path.realpath(__file__))

# Montando o nome do arquivo
nome_arquivo_input  = diretorio + '\\dados_coleta.csv'
nome_arquivo_output = diretorio + '\\dados_coleta_ordenado.csv'

try:
    arquivo_input = open(nome_arquivo_input, 'r', encoding='utf-8')
except FileNotFoundError:
    print('Deu ERRO...\nArquivo NÃO EXISTE...')
except PermissionError:
    print('Deu ERRO...\nArquivo JÁ ABERTO...')
except:
    print('Deu ERRO...', sys.exc_info()[0])
else:
    print('\nLendo os dados do arquivo...\n')
    dados_coletados = list()
    while True:
        linha = arquivo_input.readline()[:-1]
        if linha == '': break
        dados_coletados.append(int(linha))

    tempo_1 = time.time()
    dados_coletados_ordenados = ordenacao_lib.ordena_insertion(dados_coletados)
    tempo_2 = time.time()
    delta_tempo = tempo_2 - tempo_1
    print('\nTempo Decorrido... {0}\n'.format(delta_tempo))

    # Salvar a lista Ordenada em arquivo
    # TODO: Implementar
    arquivo_output = open(nome_arquivo_output, "w" , encoding = "utf-8")
    for valor in dados_coletados_ordenados:
        arquivo_output.write(str(valor) + "\n")
    arquivo_output.close()
    
finally:
    data_hora_2 = datetime.today()
    print('\nPrograma Encerrado... {0}\n')