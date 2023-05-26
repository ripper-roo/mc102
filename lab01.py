sheila = input()
reginaldo = input()

relacoes = {
        ("pedra", "papel") : False,     ("papel", "pedra") : True,
        ("pedra", "tesoura") : True,    ("papel", "tesoura") : False,
        ("pedra", "spock") : False,     ("papel", "spock") : True,
        ("pedra", "lagarto") : True,    ("papel", "lagarto") : False,

        ("tesoura", "papel") : True,    ("spock", "papel") : False,
        ("tesoura", "pedra") : False,   ("spock", "pedra") : True,
        ("tesoura", "spock") : False,   ("spock", "tesoura") : True,
        ("tesoura", "lagarto") : True,  ("spock", "lagarto") : False,

        ("lagarto", "papel") : True,
        ("lagarto", "pedra") : False,
        ("lagarto", "spock") : True,
        ("lagarto", "tesoura") : False,
        }

if sheila == reginaldo:
        print("empate")
elif relacoes[(sheila, reginaldo)]:
        print("Interestelar")
else:
        print("Jornada nas Estrelas")


