from varasto import Varasto

def lisaa_varastoon(nimi, varaston_nimi, varasto, maara):
    print(f"{nimi}: {varasto}\n{varaston_nimi}.lisaa_varastoon({maara})")
    varasto.lisaa_varastoon(maara)
    print(f"{nimi}: {varasto}")

def ota_varastosta(nimi, varaston_nimi, varasto, maara):
    print(f"{nimi}: {varasto}\n{varaston_nimi}.ota_varastosta({maara})")
    varasto.ota_varastosta(maara)
    print(f"{nimi}: {varasto}")

def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Luonnin jälkeen:\nMehuvarasto: {mehua}\nOlutvarasto: {olutta}")

    print(f"Olut getterit:\nsaldo = {olutta.saldo}\ntilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("Mehu setterit:\nLisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print(f"Virhetilanteita:\nVarasto(-100.0);\n{Varasto(-100.0)}")

    print(f"Varasto(100.0, -50.7)\n{Varasto(100.0, -50.7)}")

    lisaa_varastoon('Olutvarasto', 'olutta', olutta, 1000.0)
    lisaa_varastoon('Mehuvarasto', 'mehua', mehua, -666.0)
    ota_varastosta('Olutvarasto', 'olutta', olutta, 1000.0)
    ota_varastosta('Mehuvarasto', 'mehua', mehua, -32.9)

if __name__ == "__main__":
    main()
