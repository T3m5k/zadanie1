x = 1
meme = {
    "LOL": "odpowiedź na coś zabawnego",
    "CRINGE": "coś dziwnego lub wstydliwego",
    "ROFL": "odpowiedź na żart",
    "SHEESH": "lekka dezaprobata",
    "CREEPY": "straszny, złowieszczy",
    "AGGRO": "stać się agresywnym/zły",
}
print("wypisz słowo którego nie rozumiesz")
print("lub naciśnij enter by wyjść")
print("lub 1 by zobaczyć listę słów")
while x == 1:
    slowo = input()
    if slowo == "1":
        print()
        print("oto lista słów:")
        for i in meme:
            print(i)
    elif slowo == "":
        print()
        print("wychodzenie z programu")
        x -= 1
    elif slowo in meme.keys():
        print()
        print(meme[slowo])
    else:
        print()
        print("nie ma takiej komendy")
