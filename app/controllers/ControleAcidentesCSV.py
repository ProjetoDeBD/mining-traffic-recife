from app.persistence.EnderecoDao import getEnderecoID, getEnderecoLocal
from app.persistence.AcidenteDao import getAcidentesFiltro, getAcidentes, getAcidentesFiltro2

def lerTxt(nome_ficheiro):
    ficheiro = open(nome_ficheiro, encoding="utf8")
    # ficheiro = open(nome_ficheiro, "r")
    lista = ficheiro.readlines()
    ficheiro.close()
    return lista

def getTodosAcidentesFiltro(dados='', tipoDeDado=''):
    coordenadas = []
    ruas = []
    listaLatitude = []
    listaLongitude = []
    listaAcidente = getAcidentesFiltro(dados, tipoDeDado)
    if listaAcidente != None:
        for i in listaAcidente:
            endereco = getEnderecoID(i.endereco_codlocal)
            for endereco in endereco:
                if len((endereco.latitude).split('.')) == 2 and len((endereco.longitude).split('.')) == 2:
                    latitude = float(endereco.latitude)
                    longitude = float(endereco.longitude)
                    listaLatitude.append(latitude)
                    listaLongitude.append(longitude)
                    ruas.append(endereco.local1)
        coordenadas.append(listaLatitude)
        coordenadas.append(listaLongitude)
        coordenadas.append(ruas)
        return coordenadas
    return None

def getTodosAcidentesFiltro2(comp_select_ano ='', comp_select_mes ='', comp_select_bairro ='', comp_select_qtd_vitimas =''):
    listaAcidente = getAcidentesFiltro2(comp_select_ano, comp_select_mes, comp_select_bairro, comp_select_qtd_vitimas)
    listaDados = []
    totalDeAcidente = 0
    automovel = 0
    pedestre = 0
    ciclomotor = 0
    ciclista = 0
    motocicleta = 0
    outros = 0
    colisao = 0
    atropelamento = 0
    colisaoCiclista = 0
    acidentePercurso = 0
    outros2 = 0
    if listaAcidente != None:
        for i in listaAcidente:
            endereco = getEnderecoID(i.endereco_codlocal)
            for endereco in endereco:
                if str(comp_select_bairro.upper()) == endereco.bairro and str(comp_select_ano) in i.data_abertura and \
                        comp_select_mes in i.data_abertura[3::]:
                    totalDeAcidente += 1
                    if i.tipo.upper() == 'ALTOMOVEL':
                        automovel += 1
                    elif i.tipo.upper() == 'PEDESTRE':
                        pedestre += 1
                    elif i.tipo.upper() == 'CICLOMOTOR':
                        ciclomotor += 1
                    elif i.tipo.upper() == 'CICLISTA':
                        ciclista += 1
                    elif i.tipo.upper() == 'MOTOCICLETA':
                        motocicleta += 1
                    else:
                        outros += 1

                    if i.tipo_ocorrencia.upper() == 'COLISÃO':
                        colisao += 1
                    elif i.tipo_ocorrencia.upper() == 'ATROPELAMENTO':
                        atropelamento += 1
                    elif i.tipo_ocorrencia.upper() == 'COLISÃO COM CICLISTA':
                        colisaoCiclista += 1
                    elif i.tipo_ocorrencia.upper() == 'ACIDENTE DE PERCURSO':
                        acidentePercurso += 1
                    else:
                        outros2 += 1
        listaDados.append(totalDeAcidente)
        listaDados.append(automovel)
        listaDados.append(pedestre)
        listaDados.append(ciclomotor)
        listaDados.append(ciclista)
        listaDados.append(motocicleta)
        listaDados.append(outros)
        listaDados.append(colisao)
        listaDados.append(colisaoCiclista)
        listaDados.append(atropelamento)
        listaDados.append(acidentePercurso)
        listaDados.append(outros2)
        return listaDados
    return False

def getBairrosMaisAcidentes():
    listaBairros = ["AFOGADOS", "BAIRRO DO RECIFE", "BOA VIAGEM", "BOA VISTA", "CASA AMARELA", "CASA FORTE", "CORDEIRO",
                    "DERBY", "DOIS UNIDOS", "ENCRUZILHADA",
                    "ESPINHEIRO", "GRAÇAS", "ILHA DO LEITE", "ILHA DO RETIRO", "IPUTINGA", "MADALENA", "PARNAMIRIM",
                    "PINA", "SANTO AMARO", "SANTO ANTÔNIO",
                    "SÃO JOSÉ", "SOLEDADE", "TORRE"]
    listaResultado = []
    codListaAcidentes = []

    lista = getAcidentes()
    if lista != None:
        for ac in lista:
            codListaAcidentes.append(ac.endereco_codlocal)

    for i in listaBairros:
        cont = 0
        listaEnderecos = getEnderecoLocal(i)
        if listaEnderecos != None:
            for end in listaEnderecos:
                if end.codlocal in codListaAcidentes:
                    cont += 1
            listaResultado.append(cont)
    if len(listaResultado) != 0:
        return listaResultado
    return False

def getTodosAcidentes():
    coordenadas = []
    ruas = []
    listaLatitude = []
    listaLongitude = []
    listaAcidente = getAcidentes()
    if listaAcidente != None:
        for i in listaAcidente:
            endereco = getEnderecoID(i.endereco_codlocal)
            for endereco in endereco:
                if len((endereco.latitude).split('.')) == 2 and len((endereco.longitude).split('.')) == 2:
                    latitude = float(endereco.latitude)
                    longitude = float(endereco.longitude)
                    listaLatitude.append(latitude)
                    listaLongitude.append(longitude)
                    ruas.append(endereco.local1)
        coordenadas.append(listaLatitude)
        coordenadas.append(listaLongitude)
        coordenadas.append(ruas)
        return coordenadas
    return None

def getMesesAcidentes():
    listaAcidente = getAcidentes()

    dic_meses ={}
    if listaAcidente != None:
        for i in listaAcidente:
            data = (i.data_abertura).split("/")
            if len(data) != 1:
              mes = data[1]
              if mes in dic_meses:
                dic_meses[mes] += 1
              else:
                dic_meses[mes] = 1
    if len(dic_meses) != 0:
      return dic_meses.keys(), dic_meses.values()
    return None, None

'''
def inseriAcidentes(nomeDoTxt='tabela acidente com  vítimas(2014-2016).txt'):
    lista = lerTxt(nomeDoTxt)
    cont = 0
    for i in lista:
        i = i.replace('\n', '')
        i = i.split(';')
        if i[0] != 'data_abertura' and len(i) == 11:
            data_abertura = i[0]
            hora_abertura = i[1]
            bairro = i[2]
            endereco = i[3]
            complemento = i[4]
            tipo_ocorrencia = i[5]
            quantidade_vitimas = i[6]
            descricao = i[7]
            tipo = i[8]
            latitude = i[9]
            longitude = i[10]
            codEndereco = getEnderecoDao(endereco, latitude, longitude)
            if codEndereco:
                for i in codEndereco:
                    objAcidente = acidente(None, data_abertura, hora_abertura, tipo_ocorrencia,
                                           quantidade_vitimas, descricao, i.codlocal, tipo)
                    postAcidente(objAcidente)
                    cont += 1
    print(("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont))))
    print('*')
    print('**')
    print('***')
    print('****')
    time.sleep(999999999)
    print(("Fim do time."))
    time.sleep(9999999999)

    return ("Fim da inserção.%s dados foram inseridos com sucesso." % (str(cont)))

#print(inseriAcidentes())
'''
