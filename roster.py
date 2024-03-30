# https://goheels.com/sports/mens-basketball/roster

# 2a
import pandas as pd
roster = ['Bacot', 'Davis', 'Ryan']
data = pd.DataFrame(roster)
print(data)

'''
roster = ['Bacot', 'Davis', 'Ryan']
for player in roster:
    print(player)
'''

# 3a
import pandas as pd
roster = ["Bacot", "Davis", "Cadeau"]
player = {"Last Name": roster}
data = pd. DataFrame (player)
print

# 4
import pandas as pd
roster = ["Bacot", "Davis", "Cadeau"]
player = {"Last Name":["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [83, 72, 731],
          "weight": [240,180,180]
           }
data = pd. DataFrame (player)
print(data)

# 5
import pandas as pd

player = {"Last Name":["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [83, 72, 731],
          "weight": [240,180,180]
           }
data = pd.DataFrame (player)
print(data)

# 6
import pandas as pd

player = {"Last Name":["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando", "RJ", "Elliot"],
          "height": [83, 72, 731],
          "weight": [240,180,180]
           }

data = pd. DataFrame (player)

# bmi = weight in kg/ height in meters squared
data['bmi'] = (data['weight']/2.205)/((data['height']/39.37)**2)
data['bmi'] = data['bmi'].round(2)

print (data)

data.to_csv('bmi.csv')