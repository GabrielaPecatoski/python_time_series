#O que e um cabecalho para Python dentro de um arquivo
#R E um bloco no inicio do codigo geralmente com comentarios ou docstrings que identifica e descreve o arquivo
#para que serve
#R Serve para documentar o proposito do script indicar o interpretador e facilitar a leitura e manutencao do codigo
#o que e uma docstring
#R Sao strings colocadas logo apos uma funcao classe ou modulo e sao usadas para documenta las Sao delimitadas por aspas triplas e diferem dos comentarios pois docstrings podem ser acessadas em tempo de execucao tornando as uteis para gerar documentacoes automaticas e facilitar a compreensao do codigo
#para que serve
#R Serve para documentar uma funcao classe ou modulo dentro de python tornando as uteis para gerar documentacoes automaticas e facilitar a compreensao do codigo


"""
Exercicios do Professor Fabiano
Descricao Exemplos de funcoes simples em Python para pratica interativa
"""

import re
import unicodedata

def e_par() -> bool:
    """Retona True se for par se nao retorna False"""
    n = int(input("\nDigite um numero "))
    if n % 2 == 0:
        print(f"O numero {n} eh par")
        return True
    else:
        print(f"O numero {n} eh impar")
        return False


def limpa_texto() -> str:
    """Deixa minusculo e remove pontuacao comum"""
    # TODO converta s para minusculo e remova pontuacoes como ,.;:!?'"()-_
    s = input("\nDigite um texto ")
    s = s.lower()
    s = unicodedata.normalize("NFD", s)
    s = s.encode("ascii", "ignore").decode("utf-8")
    resultado = re.sub(r"[,\.;:!?'\"()\-_]", "", s)
    print("Texto limpo", resultado)
    return resultado


def total_por_vendedor() -> dict:
    """
    vendas lista de tuplas nome valor
    Retorna dict nome soma_valores
    """
    # TODO inicialize um dict e va somando
    print("\nDigite vendas no formato nome valor Digite fim para encerrar")
    vendas = []
    while True:
        entrada = input("Venda ")
        if entrada.lower() == "fim":
            break
        try:
            nome, valor = entrada.split()
            valor = valor.replace(",", ".")
            valor = float(valor)
            vendas.append((nome, valor))
        except ValueError:
            print("Formato invalido Use nome valor")

    totais = {}
    for nome, valor in vendas:
        totais[nome] = totais.get(nome, 0) + valor

    print("\nTotais por vendedor", totais)
    return totais


def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Verificar se numero e par")
        print("2 - Limpar texto")
        print("3 - Total por vendedor")
        print("0 - Sair")

        opcao = input("Escolha uma opcao ")

        if opcao == "1":
            e_par()
        elif opcao == "2":
            limpa_texto()
        elif opcao == "3":
            total_por_vendedor()
        elif opcao == "0":
            print("Saindo")
            break
        else:
            print("Opcao invalida Tente novamente")


if __name__ == "__main__":
    menu()
