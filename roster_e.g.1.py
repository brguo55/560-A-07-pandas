# 2023-24 UNC Basketball Roster

import pandas as pd

def feet_to_meters(feet, inches):
    meters = (feet * 12 + inches) * 0.0254
    return round(meters, 4)

# Assuming that the 'height' list is meant to be feet and inches,
# e.g., 6.9 should be interpreted as 6 feet 9 inches, not 6.9 feet.
# If 6.11 is 6 feet 11 inches, and 6.10 is 6 feet 10 inches.
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
data['bmi_example'] = (data['weight'] / 2.205) / (data['height'] ** 2)
data['bmi_example'] = data['bmi_example'].round(2)

print(data)

# Save to CSV
data.to_csv('bmi_example.csv', index=False)

