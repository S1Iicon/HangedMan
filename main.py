import json
from random import choice
import graph

with open('spanish.json', 'r', encoding="UTF-8") as f:
    global word
    word = choice(json.load(f)).lower()


def print_word_graph(x: list):
    for i in x:
            print(i, end='')
    print('')

def play():
    print("\n###\nBienvenido al juego del ahorcado, pulse cualquier tecla para continuar\n###\n")
    input("")

    vidas = 6
    win = 0
    n = len(word)
    word_arr = [i for i in word]
    word_graph = ["_" for i in range(n)]
    used_words = []
    letters_found = dict()

    print(f"\n###\nTienes 6 vidas, intenta adivinar la palabra, esta tiene {n} letras\n###\n")
    while vidas > 0:
        if win == n:
            print("\n###\nHas ganado el juego\n###\n")
            input("")
            return 0

        found = 0

        print(graph.hanged_man(6 - vidas))
        print_word_graph(word_graph)
        if len(used_words) > 0:
            print(f"Las letras utilizadas hasta el momento son: {used_words}")
        
        letter = input("\nLetra: ")

        try:
            letter = int(letter)
        except:
            pass
        else:
            print("\n###\nPor favor, introduzca una letra valida\n###\n")
            input("")
            continue

        if len(letter) == 1:
            if letter in used_words:
                print("\n###\nYa has seleccionado esa letra\n###\n")
                input("")
                continue

            used_words.append(letter)

            for index, letter_word in enumerate(word_arr):
                if letter == letter_word:
                    letters_found[index] = letter
                    found += 1

            if found == 0:
                print("\n###\nLa letra que has seleccionado no está en la palabra\n###\n")
                vidas -= 1
                graph.hanged_man(6 - vidas)
                print_word_graph(word_graph)
            else:
                index_found = list(letters_found.keys())[-1:-found-1:-1]
                win += found
                for i in index_found:
                    word_graph[i] = letter
                
                print(f"\n###\nHas encontrado la letra {letter}\n###\n")
                input("")

                graph.hanged_man(6 - vidas)
                print_word_graph(word_graph)
    print(f"\n###\nHas perdido, la palabra era: {word}\n###\n")

play()