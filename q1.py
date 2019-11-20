def define_data(data):
    lista_datas = data.split("/")

    ano = int(lista_datas[0])
    mes = int(lista_datas[1])
    dia = int(lista_datas[2])

    data_d = {"Ano": ano, "Mes": mes, "Dia": dia}

    return data_d

def campo_ativo(campo):
    if len(campo) == 4:
        campo = campo[:3]
    
    if campo[0] == "S":
        return True
    return False

def separa_string(valor):
    lista_string = valor.split(":")
    return lista_string

def le_linhas(arq):
    arq.seek(0)
    lista_linhas = arq.readlines()

    return lista_linhas

def main():
    pessoas = []
    arq = open("nomes.txt", "r")

    dic_nomes = {"CPF":"",
             "Nome":"",
             "Data_de_nascimento":"",
             "Data_de_cadastro":"",
             "Ativo":""}
    
    arq_linhas = le_linhas(arq)

    for idx in range(len(arq_linhas)):
        dic_atual = dic_nomes.copy()
        dados_atuais = separa_string(arq_linhas[idx])
        dic_atual["CPF"] = dados_atuais[0]
        dic_atual["Nome"] = dados_atuais[1]
        dic_atual["Data_de_nascimento"] = define_data(dados_atuais[2])
        dic_atual["Data_de_cadastro"] = define_data(dados_atuais[3])
        dic_atual["Ativo"] = campo_ativo(dados_atuais[4])
        pessoas.append(dic_atual)

    print(pessoas)

    arq.close()

main()
