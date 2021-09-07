budget = 113
aantalBanden = 2
bandenPrijs = 47.98
bandArbeid = 15.00

print(budget - aantalBanden * (bandenPrijs + bandArbeid))

Saldo = budget - aantalBanden * (bandenPrijs + bandArbeid)
isReparatieBetaalbaar = Saldo >= 0

print()

print("kan ik de scooterReparatie betalen?")
if isReparatieBetaalbaar:
    print("ja, dat kan want je hebt genoeg")
else:
    print("nee, want je hebt te weinig geld") 

