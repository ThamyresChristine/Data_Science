#Conditions - if, elif, else
"""
cdt = 15200.50  #float
score = 26.000  #float

if (cdt > 20000.00) and ( score > 25.000):
    print("vc pode ter um carro popular")
elif (cdt> 21000.00) and (score > 45.000):
    print("vc pode comprar um carro top de linha")
else:
    print("vc precisa melhorar seu crédito")
"""

#Nested
cdt1 = 18000.50  #float
score1 = 7.000  #float


if (cdt1< 20000.00) and (score1 > 25.000):
        if (cdt1< 5000.00)and (score1 > 25.000):
            print("vc precisa melhorar seu crédito")
#        if (cdt1< 20000.00) and (score1 < 10.000):
#            print("vc precisa melhorar seu score")
else:
    print("vc não pode ter carro")