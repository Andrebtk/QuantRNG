from libRNG import QuantRNG, QuantRNGint


minInput = int(input("Generate a number between: "))
maxInput = int(input("And: "))

if minInput == 0:
    print(QuantRNG(maxInput))
else:
    print(QuantRNGint(minInput, maxInput))

    

