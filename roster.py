# 7 Official 2023-24 UNC Basketball Roster

import pandas as pd

player = {
        "Last Name": ['High', 'Cadeau', 'Ryan', 'Davis', 'Bacot', 'Trimble', 'Wojcik', 'Washington', 'Lebo', 'Landry,', 'Okonkwo', 'Farris', 'Ingram'],
        "First Name": ['Zayden', 'Elliot', 'Cormac', 'RJ', 'Armando', 'Seth', 'Paxson', 'Jalen', 'Creighton', 'Rob', 'James', 'Duwe', 'Harrison'],
        "height": [83, 72, 73],
        "weight": [240,180,180]
         }   

data = pd. DataFrame (player)

data['bmi'] = (data['weight']/2.205)/((data['height']/39.37)**2)
data['bmi'] = data['bmi'].round(2)

print (data)

data.to_csv('bmi.csv')
