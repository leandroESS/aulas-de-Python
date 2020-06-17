lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
   divisao = 10/1
   numero = lista[1]
   x = a
   print('fechando arquivo')
   # arquivo.close() #arquivo não fechar, pois deu antes o problema da variável
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por zero") # corresponde a divisão por 0
except IndexError   :
    print('erro ao acessar um indice inválido da lista') # correponde tentar acessar índice fora do limite
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print("Exacuta quando não tiver exceção") #caso se tivesse tudo certo
finally:
    print('sempre executa') #dando erro ou não fianlly sempre será executado
    print('fechando arquivo')
    arquivo.close()
