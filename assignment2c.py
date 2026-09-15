# Silerio, Lucas
# Computer Programming, period 4
# Assignment: Homework 2C
# Sep 9, 2026

#STEP 1: PRINT FULL LIST
altitude_readings = [512.1, 1012.2, 1421.3, 1754.6, 2812.0, 3512.6, 4237.5, 6820.2]
print(altitude_readings)

#STEP 2: APPEND NEW VALUE TO LIST
altitude_readings.append(4321.4),altitude_readings.append(7912.6)
print(f"New altitude readings at {altitude_readings[8]} and {altitude_readings[9]}.")
print(altitude_readings)

#STEP 3: POP OUT CERTAIN VALUES
print(altitude_readings[0], altitude_readings[1])
errors = [altitude_readings.pop(0), altitude_readings.pop(0)]
print(errors)
print(f"First two altitude readings were sensor noise, removing {errors[0]} and {errors[1]}.")
print(altitude_readings)

#STEP 4: INSERT A VALUE AT A CERTAIN INDEX
altitude_readings.insert(4, 5612.7)
print(f"Missing altitude reading recovered at index 4: {altitude_readings[4]}")

#STEP 5: PRINT NEW LIST + SPECIFIC VALUE AT A CERTAIN INDEX
print(f"Full altitude readings: {altitude_readings}, reading at index 3: {altitude_readings[3]}")