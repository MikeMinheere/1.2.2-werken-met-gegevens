#peter gaat met 4 vrienden naar de Speelhal-dag. de entree kost 6.65, eten kost 3.32 en drinken kost 1.10.
#Peter trakteert en iedereen neem 1 keer eten en 2 keer drinken, behalve Tim want die nam 3 keer.

Entree = 6.65
Eten = 3.32
Drinken = 1.10
Totaal = 4*(Entree + Eten + 2*(Drinken)) + Drinken

Tekst = 'Ik kan niet geloven dat die geweldige dag in de speelhal maar ' + str(Totaal) + ' euro kostte!'
print(Tekst)