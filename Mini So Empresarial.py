#Objetivo do codigo será montar 3 classes. A classe 1 devera ter funções de adicionar e respectivas | A classe 2 deverá ter funções de adicionar colaboradores e respectivos e a Classe 3 devera ter saldo e balanço mensal.
#Começando a criar e aprimorar a classe 1(Classe de adicionar produtos um mini CRUD com salvamento no arquivo respectivo.) e agora importarei o json e nomearei o arquivo da classe 1.
import json
arquivo_classe_produto = ('Arquivo CRUD de produtos 2026.json')
print('='* 65)

#Agora comecarei a criação da classe de adicionar produtos.
class GerenciadorProdutos:
    def __init__(self):
        pass
    
    def adicionando_produtos(self, produto_adicionado, quantidade_recebida, data_recebimento):
        self.produto = produto_adicionado
        self._quantidade = quantidade_recebida
        self.__data = data_recebimento

        try:
            with open(arquivo_classe_produto, 'r', encoding='utf-8') as arquivo_produtos:
                arquivos = json.load(arquivo_produtos)
        
        except (FileNotFoundError, json.JSONDecodeError):
            arquivos = []
        
        adicionando_produtos = {
            'Produto Recebido': produto_adicionado,
            'Quantidade Recebida': quantidade_recebida,
            'Data do recebimento': data_recebimento,
        }

        arquivos.append(adicionando_produtos)

        with open(arquivo_classe_produto, 'w', encoding='utf-8') as arquivo_produtos:
            json.dump(arquivos, arquivo_produtos, ensure_ascii=False, indent=6)
        return f'----- INFORMAÇÕES DO PRODUTO -----\n--> Nome do produto: {self.produto}\n--> Quantidade Adicionada: {self._quantidade}\n--> Data do Cadastro do Produto: {self.__data}\n-----------'
    
    def atualizando_produtos(self,nome_produto , nova_quantidade):
        try:
            with open(arquivo_classe_produto, 'r', encoding='utf-8') as arquivo_produtos:
                arquivos = json.load(arquivo_produtos)

        except (FileNotFoundError, json.JSONDecodeError):
            arquivos = []

        for prod in arquivos:
            if prod['Produto Recebido'] == nome_produto:
                prod['Quantidade Recebida'] = nova_quantidade
                break

        with open(arquivo_classe_produto, 'w', encoding='utf-8') as arquivo_produtos:
            json.dump(arquivos, arquivo_produtos, ensure_ascii=False, indent=6)
        return f'O produto {nome_produto} Teve a quantidade atualizada com sucesso!, Verificar na opção VISUALIZAR!'
        
    def removendo_produto(self, nome_produto):
        try:
            with open(arquivo_classe_produto, 'r', encoding='utf-8') as arquivo_produtos:
                arquivos = json.load(arquivo_produtos)

        except (FileNotFoundError, json.JSONDecodeError):
            arquivos = []

        for prod in arquivos:
            if prod['Produto Recebido'] == nome_produto:
                arquivos.remove(prod)

        with open(arquivo_classe_produto, 'w', encoding='utf-8') as arquivo_produtos:
            json.dump(arquivos, arquivo_produtos, ensure_ascii=False, indent=6)
        return f'O produto {nome_produto} Foi removido com sucesso!, Verificar na opção VISUALIZAR!'
    
    def listando_produtos(self):
        try:
            with open(arquivo_classe_produto, 'r', encoding='utf-8') as arquivo_produtos:
                arquivos = json.load(arquivo_produtos)

        except  (FileNotFoundError, json.JSONDecodeError):
            return 'Nenhum produto cadastrado no estoque!!'

        for indice, produtos in enumerate(arquivos, start=1):
            print(indice, produtos)

    def saindo_da_função(self):
        print('Saindo da função, voltando para o SUBMENU!')
        return

print('='* 65)

#Agora vamos começar a Classe de gerenciamento de colaboradores, com funções de adicionar, pesquisar, atualizar, remover e exibir todos os colaboradores cadastrados | Designando o nome do arquivo JSON.
arquivo_classe_colaboradores = ('Arquivo CRUD de Gerenciamento de Colaboradores 2026.json')
class GerenciadorColaboradores:
    def __init__(self):
        pass
    
    def adicionando_colaboradores(self, nome, idade, email, cargo, renda):
        self.__nome = nome
        self._idade = idade
        self._email = email
        self.__cargo = cargo
        self.__salario = renda

        try:
            with open(arquivo_classe_colaboradores, 'r', encoding='utf-8') as arquivo_colaboradores:
                arquivos_colab = json.load(arquivo_colaboradores)
        
        except (FileNotFoundError, json.JSONDecodeError):
            arquivos_colab = []

        adicionando_colaboradores = {
            'Nome do Colaborador(a)': self.__nome,
            'Idade do Colaborador(a)': self._idade,
            'Email do Colaborador(a)': self._email,
            'Cargo Designado': self.__cargo,
            'Salario Mensal': self.__salario,
        }
        arquivos_colab.append(adicionando_colaboradores)

        with open(arquivo_classe_colaboradores, 'w', encoding='utf-8') as arquivo_colaboradores:
            json.dump(arquivos_colab, arquivo_colaboradores, ensure_ascii=False, indent=6)
        return f'---- INFORMAÇÕES DO COLABORADOR ----\n-> Nome do Colaboradorador(a): {self.__nome}\n-> Idade do Colaborador(a): {self._idade}\n-> Email Cadastrado: {self._email}\n-> Cargo: {self.__cargo}\nSalario: R${self.__salario}.'
    
    def atualizando_colaboradores(self,nome, nova_idade, novo_email, novo_cargo, novo_salario):
        try:
            with open(arquivo_classe_colaboradores, 'r', encoding='utf-8') as arquivo_colaboradores:
                arquivos_colab = json.load(arquivo_colaboradores)
        
        except (FileNotFoundError, json.JSONDecodeError):
            arquivos_colab = []

        for colaborador in arquivos_colab:
            if colaborador['Nome do Colaborador(a)'] == nome:

                if nova_idade:
                    colaborador['Idade do Colaborador(a)'] = nova_idade

                if novo_email:
                    colaborador['Email do Colaborador(a)'] = novo_email

                if novo_cargo:
                        colaborador['Cargo Designado'] = novo_cargo

                if novo_salario:
                    colaborador['Salario Mensal'] = novo_salario
                    break
        
        with open(arquivo_classe_colaboradores, 'w', encoding='utf-8') as arquivo_colaboradores:
            json.dump(arquivos_colab, arquivo_colaboradores, ensure_ascii=False, indent=6)
        return f'Informações do colaborador: {nome} Foram atualizadas com sucesso, Favor verificar na opção (Listando Colaboradores!!)'
    
    def removendo_colaborador(self, nome):
        try:
            with open(arquivo_classe_colaboradores, 'r', encoding='utf-8') as arquivo_colaboradores:
                arquivos_colab = json.load(arquivo_colaboradores)
        
        except(FileNotFoundError, json.JSONDecodeError):
            arquivos_colab = []

        for colaborador in arquivos_colab:
            if colaborador['Nome do Colaborador(a)'] == nome:
                arquivos_colab.remove(colaborador)

        with open(arquivo_classe_colaboradores, 'w', encoding='utf-8') as arquivo_colaboradores:
            json.dump(arquivos_colab, arquivo_colaboradores, ensure_ascii=False, indent=6)

    def listando_colaboradores(self):
        try:
            with open(arquivo_classe_colaboradores, 'r', encoding='utf-8') as arquivo_colaboradores:
                arquivos_colab = json.load(arquivo_colaboradores)

        except  (FileNotFoundError, json.JSONDecodeError):
            return 'Nenhum produto cadastrado no estoque!!'

        for indice, colaboradores in enumerate(arquivos_colab, start=1):
            print(indice, colaboradores)

    def saindo_da_função(self):
        print('Saindo da função, voltando para o SUBMENU!')
        return

print('='* 65)
#Agora vamos para a ultima CLasse, A classe de exibição de lucros, Entradas | Saidas e o balanço mensal de lucro.
#URGENTE, RODANDO O CODIGO PRIMEIRO PARA VERIFICAR ERROS.
while True:
    print('Funções do codigo.\n1 - Gerenciamento de Produtos\n2 - Gerenciamento de Colaboradores\n3 - Sair do Programa\n')
    opção = int(input('1 - Gerenciadomento de Produtos\n2 - Gerenciadomento de Colaboradores\n3 - Sair do Programa\n-'))

    if opção == 1:
        produto = input('Qual o nome do Produto?\n->')
        quantidade = int(input('Qual a quantidade que foi recebida do produto?\n->'))
        data = input('Qual a data do recebimento?\n->')
        

        opção_produtos = int(input('Qual função do menu de produtos deseja acessar?\n1 - Adicionando\n2 - Atualizando\n3 - Removendo\n4 - Listando\n0 - Retornando para o menu principal\n->'))
        produto1 = GerenciadorProdutos()

        if opção_produtos == 1:
            print(produto1.adicionando_produtos(produto, quantidade, data))
            print(f'Produto {produto} foi adicionado com sucesso!!')
            
        elif opção_produtos == 2:
            print(produto1.atualizando_produtos(produto, 100))
            print(f'Produto {produto} foi atualizado com sucesso!!')

        elif opção_produtos == 3:
            print(produto1.removendo_produto(produto))
            print(f'Produto {produto} foi removido com sucesso!!')

        elif opção_produtos == 4:
            print(produto1.listando_produtos())

        elif opção_produtos == 0:
            print('Saindo do menu de PRODUTOS!') 
            produto1.saindo_da_função()

    elif opção == 2:
        colaborador = input('Qual o nome do colaborador?\n->')
        idade = int(input('Quantos anos o colaborador tem?\n->'))
        email = input('Qual o email do colaborador?\n->')
        cargo = input('Qual o cargo atual do colaborador?\n->')
        salario = float(input('Qual o salario mensal do colaborador?\n->'))

        opção_colaborador = int(input('Qual função do menu de colaboradores deseja acessar?\n1 - Adicionando\n2 - Atualizando\n3 - Removendo\n4 - Listando\n0 - Retornando para o menu principal\n->'))
        colaborador1 = GerenciadorColaboradores()

        if opção_colaborador == 1:
            print(colaborador1.adicionando_colaboradores(colaborador, idade, email, cargo, salario))
            print(f'O colaborador {colaborador} foi adicionado com sucesso!!')

        elif opção_colaborador == 2:
            print(colaborador1.atualizando_colaboradores(19, 'Painelvip2703@gmail.com', 'Analista de dados', 3.899))
            print(f'Colaborador {colaborador} foi atualizado com sucesso!!')
        
        elif opção_colaborador == 3:
            print(colaborador1.removendo_colaborador('Wellington Silva'))
            print(f'O Colaborador {colaborador} foi removido com sucesso!!')

        elif opção_colaborador == 4:
            colaborador1.listando_colaboradores()
        
        elif opção_colaborador == 0:
            print('Saindo do menu de COLABORADORES!')
            print(colaborador1.saindo_da_função())
