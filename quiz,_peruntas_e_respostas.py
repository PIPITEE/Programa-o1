# -*- coding: utf-8 -*-
"""QUIZ, PERUNTAS E RESPOSTAS

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-tT7MXtJqbnjXXajb_xAt1UCCQ3C886O
"""

import random


perguntas_respostas = [
    ("Qual símbolo é usado para comentários de uma linha em Python?",
     ["a) //", "b) #", "c) /*", "d) --"],
     "b"),

    ("Qual função é usada para imprimir texto na tela em Python?",
     ["a) show()", "b) display()", "c) console.log()", "d) print()"],
     "d"),

    ("Qual estrutura de dados em Python é mais semelhante a um array em outras linguagens?",
     ["a) Tupla", "b) Dicionário", "c) Array", "d) Set"],
     "c"),

    ("Qual palavra-chave é usada para definir uma função em Python?",
     ["a) function", "b) def", "c) func", "d) define"],
     "b"),

    ("Qual operador é usado para verificar igualdade em Python?",
     ["a) =", "b) ===", "c) ==", "d) .equals()"],
     "c")
]

def fazer_pergunta(perguntas_respostas):

    pergunta, alternativas, resposta_correta = random.choice(perguntas_respostas)


    print(pergunta)
    for alternativa in alternativas:
        print(alternativa)


    resposta_usuario = input("Digite a letra da resposta correta: ").strip().lower()


    if resposta_usuario == resposta_correta:
        print("Resposta correta!")
    else:
        print(f"Resposta incorreta. A resposta correta é: {resposta_correta}) {alternativas[ord(resposta_correta)-97][3:]}")

    return pergunta


def executar_quiz(perguntas_respostas):
    perguntas_restantes = perguntas_respostas.copy()
    while perguntas_restantes:
        pergunta_feita = fazer_pergunta(perguntas_restantes)
        perguntas_restantes = [p for p in perguntas_restantes if p[0] != pergunta_feita]


executar_quiz(perguntas_respostas)