import requests
import pandas as pd
rows = []
columns = ['Year', 'State', 'Offense Type', 'Count']
states = ['AK','AL','AS','AR','AZ','CA','CO','CT','DC','DE','FL','GA','GU','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','UT','VA','VI','VT','WA','WI','WV','WY']
offenses = ['aggravated-assault','burglary','larceny','motor-vehicle-theft','homicide','rape','robbery','arson','violent-crime','property-crime']
base_url = 'https://api.usa.gov/crime/fbi/sapi/'
api_key = '?api_key=J12hW2tGJHGaqp9sEOLpuyAZ757BQT1bZsorqpW9'
for state in states:
    for offense in offenses:
        data = requests.get(base_url+
        f'api/nibrs/{offense}/offense/states/{state}/count'
        +api_key).json()
        try:
            print(state)
            print(data['data'])
            for entry in data['data']:
                if entry['key'] == 'Offense Count':
                    rows.append([entry['data_year'], state, offense, entry['value']])
        except:
            continue
df = pd.DataFrame(rows, columns=columns)
df.to_csv('US_CRIME.csv')
