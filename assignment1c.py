#STEP 1: INPUT
movingObject = input("What is the object?")
massOfObject = float(input("What is the mass of the object? (in kg)")) #converted into float
velocityOfObject = float(input("What is the velocity of the object? (in m/s)")) #converted into float

#STEP 2: CALCULATE FOR JOULES
kineticEnergy = 1/2 * massOfObject * velocityOfObject**2

#STEP 3: CONVERSION INTO CAL AND ERG
caloriesInKE = kineticEnergy/4.184
ERGinKE = kineticEnergy * 10**7

#STEP 4: PRINT THE REPORT
print(f"Kinetic Energy Report for: {movingObject.strip().title()}\n----------------\nJoules: {kineticEnergy} J\nCalories: {caloriesInKE} cal\nErgs: {ERGinKE} ergs")