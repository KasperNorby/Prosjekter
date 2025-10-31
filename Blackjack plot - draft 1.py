import random as rnd
import matplotlib.pyplot as plt


class Spiller:
    def __init__(self, navn, poeng=0, står=False, ess=0):
        self.navn = navn
        self.poeng = poeng
        self.står = står
        self.ess = ess
        self.historikk = []  

    def ess_fjerner(self):
        if self.poeng > 21 and self.ess > 0:
            self.poeng -= 10
            self.ess -= 1

    def ess_teller(self, kortnavn):
        if kortnavn == "Ess":
            self.ess += 1

    def trekk(self):
        global kortstokk, tot
        kort = kortstokk.pop()
        kortnavn = kort.split()[1]
        kortverdi = verdier[kortnavn]
        self.poeng += kortverdi
        self.ess_teller(kortnavn)

        if self.poeng > 21:
            self.ess_fjerner()
            if self.poeng > 21:
                print(f"{self.navn} bustet!")
                self.står = True
                self.poeng = 0
                tot += 1

        print(f"{self.navn} trekker {kort} → {self.poeng} poeng")

        self.historikk.append(self.poeng)



kortnavn = ["Ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Knekt", "Dame", "Konge"]
sorter = ["spar", "ruter", "kløver", "hjerter"]
kortstokk = [f"{s} {v}" for s in sorter for v in kortnavn]
rnd.shuffle(kortstokk)

verdier = {
    "Ess": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Knekt": 10,
    "Dame": 10,
    "Konge": 10,
}


spillere = []
tot = 0


def Lage_spillere():
    antall = int(input("Hvor mange spillere er det? "))
    for i in range(antall):
        navn = input(f"Skriv inn navn på spiller {i+1}: ")
        spillere.append(Spiller(navn))


def spillet():
    global tot
    while tot < len(spillere):
        for s in spillere:
            if s.står:
                s.historikk.append(s.poeng)
                continue

            valg = input(f"{s.navn}, vil du trekke kort eller stå? (t/s): ").lower()

            if valg == "t":
                s.trekk()

            elif valg == "s":
                s.står = True
                tot += 1


def avslutning():
   
    spillere.sort(key=lambda s: s.poeng, reverse=True)
    max_poeng = spillere[0].poeng

    vinnere = [s for s in spillere if s.poeng == max_poeng]

    print("\n-----------------")
    print("  RESULTATER")
    print("-----------------")

    if len(vinnere) == 1:
        print(f"{vinnere[0].navn} vinner med {vinnere[0].poeng} poeng!")
    else:
        print("Uavgjort mellom:")
        for s in vinnere:
            print(f" - {s.navn} ({s.poeng} poeng)")

    for s in spillere:
        plt.plot(s.historikk, label=f's.navn')

    plt.title("Poengutvikling gjennom spillet")
    plt.xlabel("Runde")
    plt.ylabel("Poeng")
    plt.legend()
    plt.show()


# ------------------------
#  KJØR SPILLET
# ------------------------
Lage_spillere()
spillet()
avslutning()


