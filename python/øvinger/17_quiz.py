# ============================================================
# PROSJEKT 17 – QUIZ
# ============================================================

poeng = 0

quiz = [
    {
        "spørsmål": "Hva er den kjemiske formelen for vann?",
        "svar": "h2o"
    },
    {
        "spørsmål": "Hvilken planet er nærmest sola?",
        "svar": "merkur"
    },
    {
        "spørsmål": "Hva kalles prosessen der planter bruker sollys til å lage energi?",
        "svar": "fotosyntese"
    },
    {
        "spørsmål": "Hva er det største organet på menneskekroppen?",
        "svar": "huden"
    }
]

print("===== QUIZ =====")

for spørsmål in quiz:
    print()
    print(spørsmål["spørsmål"])

    svar = input("Svar: ").lower()

    if svar == spørsmål["svar"]:
        print("Riktig!")
        poeng += 1
    
    else:
        print(f"Feil! Riktig svar er {spørsmål['svar']}.")


print()
print("===== RESULTAT =====")
print(f"Du fikk {poeng} av {len(quiz)} riktige.")

if poeng == len(quiz):
    print("Full pott!")

elif poeng >= len(quiz) / 2:
    print("Bra jobba!")

else:
    print("Prøv igjen!")
