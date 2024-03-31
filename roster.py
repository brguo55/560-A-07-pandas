# 2023-24 UNC Basketball Roster

# Step one: create the file and write a list program
roster = ['High', 'Cadeau', 'Ryan', 'Davis', 'Bacot', 'Trimble', 'Wojcik', 'Washington', 'Lebo', 'Landry', 'Okonkwo', 'Farris', 'Ingram']
print(roster)

# Step two: Modify the program to print out a for loop
roster = ['High', 'Cadeau', 'Ryan', 'Davis', 'Bacot', 'Trimble', 'Wojcik', 'Washington', 'Lebo', 'Landry', 'Okonkwo', 'Farris', 'Ingram']
for name in roster:
    print(name)

# Step three:  Import Pandas as pd and create a DataFrame data = pdDataFrame(roster) and print(data)
import pandas as pd

roster = ['High', 'Cadeau', 'Ryan', 'Davis', 'Bacot', 'Trimble', 'Wojcik', 'Washington', 'Lebo', 'Landry', 'Okonkwo', 'Farris', 'Ingram']
data = pd.DataFrame(roster)

print(data)

# Step four: Import Pandas as pd and create a DataFrame and print data
import pandas as pd

roster = ['High', 'Cadeau', 'Ryan', 'Davis', 'Bacot', 'Trimble', 'Wojcik', 'Washington', 'Lebo', 'Landry', 'Okonkwo', 'Farris', 'Ingram']
data = pd.DataFrame(roster, columns=['Last Name'])

print(data)


# Step five: Official 2023-24 UNC Basketball Roster

import pandas as pd

def feet_to_meters(feet, inches):
    meters = (feet * 12 + inches) * 0.0254
    return round(meters, 4)

# Assuming that the 'height' list is meant to be feet and inches,
# 6.11 is 6 feet 11 inches, and 6.10 is 6 feet 10 inches.
heights_in_feet = [6.9, 6.1, 6.5, 6.0, 6.11, 6.3, 6.5, 6.10, 6.1, 6.4, 6.8, 6.7, 6.7]
heights_in_meters = [feet_to_meters(int(h), (h*10 % 10)*12 if '.10' in str(h) else (h % 1)*10) for h in heights_in_feet]

player = {
    "Last Name": ['High', 'Cadeau', 'Ryan', 'Davis', 'Bacot', 'Trimble', 'Wojcik', 'Washington', 'Lebo', 'Landry', 'Okonkwo', 'Farris', 'Ingram'],
    "First Name": ['Zayden', 'Elliot', 'Cormac', 'RJ', 'Armando', 'Seth', 'Paxson', 'Jalen', 'Creighton', 'Rob', 'James', 'Duwe', 'Harrison'],
    "height": heights_in_meters,
    "weight": [225, 180, 195, 180, 240, 195, 195, 230, 180, 190, 240, 210, 225]
}

data = pd.DataFrame(player)

# Calculate BMI
data['bmi'] = (data['weight'] / 2.205) / (data['height'] ** 2)
data['bmi'] = data['bmi'].round(2)

print(data)

# Save to CSV
data.to_csv('bmi.csv', index=False)