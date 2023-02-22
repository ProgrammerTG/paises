import json, requests, time, sys

lista = ["https://restcountries.com/v2/all/", "https://restcountries.com/v2/name/"]

def req(alvo, argumento=None):
    if not argumento:
        while True:
            try:
                return len(json.loads(requests.get(alvo).text))
            except:
                time.sleep(1)
    else:
        while True:
            try:
                reqi = requests.get(f"{lista[1]}{alvo}")
                requisi = json.loads(reqi.text)
                if reqi.status_code != 200:
                    print("País inválido!")
                    return
                break
            except Exception as error:
                print("Não foi possível solicitar, tentando novamente..")
                time.sleep(1)
        tradu = {"moeda": "currencies", "população": "population"}
        for e in requisi:
            if argumento == "moeda":
                moeda = e['currencies'][0]
                print(f"A moeda do {alvo} é:{moeda['name']}")
            else:
                print(f"A {argumento} do {alvo} é: {e[tradu[argumento]]}!")


if __name__ == "__main__":
    print("#"*20)
    print("Bem-vindo ao sistema de países!")
    print("#"*20)
    if len(sys.argv) <= 1 or len(sys.argv) > 3 or len(sys.argv) == 2 and sys.argv[1].lower() != "all":
        print("Modo de utilização: python paises.py (pais) (moeda, população) | paises.py all")
    else:
        if len(sys.argv) == 2:
            print(f"Há {req(lista[0])} países no mundo")
        elif sys.argv[2].lower() not in ["moeda", "população"]:
            print("Digite uma opção válida!")
        else:
            req(sys.argv[1], sys.argv[2])