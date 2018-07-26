from app.models.RegistroInfracaoObjeto import registro_infracao
from app.persistence.EnderecoDao import getEnderecoDao
from app.persistence.RegistroInfracaoDao import getRegistroInfracaoData, postRegistroInfracao
import time

def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro,  "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista

def getTodosRegistrosDeInfracoes(data):
    datas = []
    listaInfracoes = getRegistroInfracaoData(data)

    for i in listaInfracoes:
        datas.append(i.infracao_codinfracao)

    return datas

'''
def inserirRegistroInfracao(nomeDoTxt='registro de infraçoes 2017(1-3).txt'):
    lista = lerTxt(nomeDoTxt)
    cont = 0
    for i in lista:
        i = i.replace('\n', '')
        i = i.split(';')
        if i[0] != 'DATAINFRACAO' and len(i) == 9:
            data_infracao = i[0]
            hora_infracao = i[1]
            data_implantacao = i[2]
            agente_equipamento = i[3]
            infracao_codinfracao = i[4]
            descricaoinfracao = i[5]
            amparolegal = i[6]
            localcometimento = i[7]
            bairro = i[8]
            codEndereco = getEnderecoDao3(localcometimento,bairro)
            print(codEndereco.codlocal)
            if codEndereco != False:
                objRegistroInfracao = registro_infracao(None, data_infracao, hora_infracao, data_implantacao,
                                                        agente_equipamento,
                                                        infracao_codinfracao, descricaoinfracao, amparolegal,
                                                        codEndereco.codlocal)
                postRegistroInfracao(objRegistroInfracao)
            cont += 1
        print('contador externo: ', cont)

    print(("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont))))
    print('*')
    print('**')
    print('***')
    print('****')
    time.sleep(999999999)
    print(("Fim do time."))
    time.sleep(9999999999)

    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont)))
print(inserirRegistroInfracao())
'''