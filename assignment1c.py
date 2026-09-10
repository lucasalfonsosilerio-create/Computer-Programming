#Lucas Silerio
#Assignment 1c

#STEP 1: INPUT
movingObject1 = [input("What is the object?").title().strip()]
massOfObject1 = [float(input("What is the mass of the object?"))] #converted into float
massOfObjectUnits1 = [input("Is this in pounds or kilograms or bald eagles?").strip().lower()] #get units
print(massOfObjectUnits1[0])

velocityOfObject1 = [float(input("What is the velocity of the object?"))] #converted into float
velocityOfObjectUnits1 = [input("Is this in miles per hour or meters per seconds or in milimeters per hour?").strip().lower()]
print(velocityOfObjectUnits1[0])

kineticEnergy1 = [1/2 * massOfObject1[0] * velocityOfObject1[0]**2]
caloriesInKE = [kineticEnergy1[0]/4.184]
ERGinKE = [kineticEnergy1[0] * 10**7]

isThereASecondObject = input("Is there a second object? (Yes or No)").strip().lower() #Get info if there's a second object

print(isThereASecondObject)

if isThereASecondObject.startswith("y"):
    #STEP 1B: APPEND
    movingObject1.append(input("What is the object?").title().strip())
    print(movingObject1)

    massOfObject1.append(float(input("What is the mass of the object?")))
    massOfObjectUnits1.append(input("Is this in pounds or kilograms?").strip().lower())

    velocityOfObject1.append(float(input("What is the velocity of the object? (in m/s)")))
    velocityOfObjectUnits1.append(input("Is this in miles per hour or meters per seconds?").strip().lower())

    #STEP 2A: CALCULATE FOR JOULES
    kineticEnergy1.append(1/2 * massOfObject1[1] * velocityOfObject1[1]**2)
    
    #STEP 3A: CONVERSION INTO CAL AND ERG
    caloriesInKE.append(kineticEnergy1[1]/4.184)
    ERGinKE.append(kineticEnergy1[1] * 10**7)
    
    #STEP 4A: CONVERSION FROM LBS OR MPH
    if massOfObjectUnits1[0].startswith("pounds" or "lbs"):
        massOfObject1[0] = massOfObject1[0] * 0.4536
    elif massOfObjectUnits1[0].startswith("bald" or "eagle"):
        massOfObject1[0] = 10.25*massOfObject1[0] * 0.4536

    if velocityOfObjectUnits1[0].startswith("miles per hour" or "mph"):
        velocityOfObject1[0] = velocityOfObject1[0] * 0.447
    elif velocityOfObjectUnits1[0].startswith("millimeters"):
        velocityOfObject1[0] = velocityOfObject1[0]*1000*3600*0.4470
    
    if massOfObjectUnits1[1].startswith("pounds" or "lbs"):
        massOfObject1[1] = massOfObject1[1] * 0.4536
    elif massOfObjectUnits1[1].startswith("bald" or "eagle"):
        massOfObject1[1] = 10.25*massOfObject1[1] * 0.4536
    
    if velocityOfObjectUnits1[1].startswith("miles per hour" or "mph"):
        velocityOfObject1[1] = velocityOfObject1[1] * 0.4470
    elif velocityOfObjectUnits1[1].startswith("millimeters"):
        velocityOfObject1[1] = velocityOfObject1[1]*1000*3600*0.4470

    #STEP 5B: PRINT THE REPORT
    object1Report = f"Kinetic Energy Report for: {movingObject1[0].strip().title()}\n----------------\nJoules: {kineticEnergy1[0]} J\nCalories: {caloriesInKE[0]} cal\nErgs: {ERGinKE[0]} ergs"
    object2Report = f"Kinetic Energy Report for: {movingObject1[1].strip().title()}\n----------------\nJoules: {kineticEnergy1[1]} J\nCalories: {caloriesInKE[1]} cal\nErgs: {ERGinKE[1]} ergs"

    print(f"{object1Report}\n{object2Report}")

    if kineticEnergy1[1] > kineticEnergy1[0]:
        print(f"{movingObject1[1]} has greater kinetic energy than {movingObject1[0]}!")
    elif kineticEnergy1[0] > kineticEnergy1[1]:
        print(f"{movingObject1[0]} has greater kinetic energy than {movingObject1[1]}!")
else:
    #STEP 4B: CONVERSION FROM LBS OR MPH
    if massOfObjectUnits1[0].startswith("pounds" or "lbs"):
        massOfObject1[0] = massOfObject1[0] * 0.4536
    elif massOfObjectUnits1[0].startswith("bald" or "eagle"):
        massOfObject1[0] = 10.25*massOfObject1[0] * 0.4536
   
    if velocityOfObjectUnits1[0].startswith("miles per hour" or "mph"):
        velocityOfObject1[0] = velocityOfObject1[0] * 0.447
    elif velocityOfObjectUnits1[0].startswith("millimeters"):
        velocityOfObject1[0] = velocityOfObject1[0]*100*60*0.4470
       

    #STEP 5A: PRINT THE REPORT
    print(f"Kinetic Energy Report for: {movingObject1[0].strip().title()}\n----------------\nJoules: {kineticEnergy1[0]} J\nCalories: {caloriesInKE[0]} cal\nErgs: {ERGinKE[0]} ergs")
