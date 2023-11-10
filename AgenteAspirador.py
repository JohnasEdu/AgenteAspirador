import random
import time
import msvcrt

class Aspirador:
    def __init__(self):
        self.energia = 100
        self.bolsa = 0
        self.localizacao = 'A'
        self.ambiente = {'A': 'Limpo', 'B': 'Limpo', 'C': 'Sujo', 'D': 'Sujo',  #Ambiente matriz 4x4
                         'E': 'Limpo', 'F': 'Sujo', 'G': 'Limpo', 'H': 'Sujo',
                         'I': 'Sujo', 'J': 'Limpo', 'K': 'Sujo', 'L': 'Limpo',
                         'M': 'Limpo', 'N': 'Limpo', 'O': 'Sujo', 'P': 'Sujo'}
        self.esvaziou_bolsa_inicial = False

    def mostrar_status(self): #Mostrar status de ações de movimentos, energia e limpeza (coleta)
        if self.localizacao == 'A':
            print(f"Em casa (A), Energia: {self.energia}")
        else:
            print(f"Localização: {self.localizacao}, Energia: {self.energia}, Bolsa: {self.bolsa}")

    def limpar_sujeira(self): #Identificar onde estiver sujo para transformar em limpo
        if self.ambiente[self.localizacao] == 'Sujo':
            self.ambiente[self.localizacao] = 'Limpo'
            self.bolsa += 1
            self.energia -= 1
            print(f"Aspirou sujeira em {self.localizacao}. Energia: {self.energia} Valor da bolsa: {self.bolsa}")


            if self.bolsa == 10 and not self.esvaziou_bolsa_inicial: #Condição se a bolsa estiver cheia
                print("Bolsa cheia! Deve voltar para Casa e esvaziar a bolsa.")
                self.voltar_casa()
            elif self.bolsa == 20: #Condição se a bolsa estiver novamente cheia
                print("Bolsa cheia novamente! Deve voltar para Casa e esvaziar a bolsa.")
                self.voltar_casa()

    def mover_aleatorio(self): #Biblioteca random para se mover com as regras das possíveis direções atribuídas
        direcoes_possiveis = ['norte', 'sul', 'leste', 'oeste']
        direcao_escolhida = random.choice(direcoes_possiveis)
        self.mover(direcao_escolhida)

    def mover(self, direcao): #Ações de movimentos dentro do ambiente criado
        movimentos = {'norte': -4, 'sul': 4, 'leste': 1, 'oeste': -1}
        nova_localizacao = ord(self.localizacao) + movimentos[direcao]
        if 'A' <= chr(nova_localizacao) <= 'P':
            self.localizacao = chr(nova_localizacao)
            self.energia -= 1
            print(f"Movido para {self.localizacao}. Energia: {self.energia}")
            self.limpar_sujeira()
        else:
            print("Movimento inválido")

    def mover_para_casa(self): #Ação de movimentação para a "casa" localização 'A'
        primeiro_movimento = True #O primeiro movimento não descontará energia e estará disponiveis as direções sul e leste
        direcoes_disponiveis = ['sul', 'leste']
        while self.localizacao != 'A':
            if primeiro_movimento:
                primeiro_movimento = False
            else:
                self.energia -= 1  # Desconta energia em movimentos subsequentes
            self.mover('norte')
        self.energia -= 1

    def voltar_casa(self): #Volta para a localização inicial A mostrando o status
        self.mover_para_casa()
        print(f"Está em casa (A).")
        self.mostrar_valor_bolsa()

        if not self.esvaziou_bolsa_inicial: #Esvaziar bolsa quando estiver no ponto A
            print(f"Bolsa vazia inicialmente. Energia: {self.energia}")
            self.esvaziou_bolsa_inicial = True
            self.bolsa = 0

        else:
            print("Esvaziou a bolsa.") #Esvaziar bolsa quando voltar na localização inicial A
            self.bolsa = 0
            self.energia += 1

    def aspirar_novamente(self):
        while self.energia < 100 and not self.objetivo_alcancado():
            self.mover_aleatorio()
            self.limpar_sujeira()
        self.voltar_casa()

    def objetivo_alcancado(self): #Limpar a sujeira em uma localização suja
        return all(value == 'Limpo' for value in self.ambiente.values())

    def mostrar_valor_bolsa(self): #Mostrar o valor da bolsa de coleta
        print(f"Valor da bolsa: {self.bolsa}")

    def mostrar_status_final(self): #Mostrar desempenho final das ações
        print("\nDesempenho final:")
        print(f"Energia restante: {self.energia}")
        print(f"Bolsa: {self.bolsa}")
        print(f"Ambiente final: {self.ambiente}")
        print("Objetivo concluído.")
        print("\nPressione qualquer tecla para continuar...") #pausa do sistema
        msvcrt.getch()