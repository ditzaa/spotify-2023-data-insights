import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importul unei fisier csv sau json în pachetul pandas
data = pd.read_csv("./spotify-2023.csv", encoding='latin-1')
print(data.head(5))

# Identificam coloanele numerice
numeric_cols = data.select_dtypes(include=['number']).columns
# Umplem valorile lipsă numai in coloanele numerice cu media valorilor pe coloana
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

#Problema 1: Analiza celor mai ascultate melodii all time
# Identificarea celor mai populare melodii
top_songs = data.sort_values(by='streams', ascending=False).head(30).reset_index(drop=True)
print("Top 30 songs on spotify all time")
print("------------------------------------------------------------------------------------------------")
pd.set_option('display.max_colwidth', None)
#print(top_songs[['track_name', 'artist(s)_name', 'streams']])
for index, row in top_songs.iterrows():
    print(f"{index + 1:2}. {row['track_name']:50}  {row['artist(s)_name']:30}  {row['streams']} streams")
print("------------------------------------------------------------------------------------------------")

#Problema 2: Functie care calculeaza castigurile artistilor pentru melodiile lansate in 2023
def get_artist_revenue(artist_name):
    rate_per_stream = 0.005
    total_streams = data[data['artist(s)_name'].str.contains(artist_name, case=False)
    & (data['released_year'] == 2023)]['streams'].sum()
    total_revenue = total_streams * rate_per_stream

    return total_revenue

#apel functie
artist_name = "Drake"
total_revenue_drake = get_artist_revenue(artist_name)
print(f"Venitul total al artistului {artist_name} in 2023 este: ${total_revenue_drake:.2f}")

#Problema 3: Colectiile de date din python
#liste
songs_2013 = data[data['released_year'] == 2013]

songs_2013 = songs_2013.sort_values(by='track_name')
songs_2013 = list(songs_2013['track_name'])
print("Most listened songs in 2023 from 2013:")
print(songs_2013)

songs_2013.pop(3) # stergem 'Do I Wanna Know?'
print(songs_2013)

#tupluri
songs_the_weeknd = data[data['artist(s)_name'].str.contains('The Weeknd', case=False)]
songs_the_weeknd = tuple(songs_the_weeknd['track_name'])
print("\nThe Weeknd popular songs:")
print(songs_the_weeknd)
print("After hours position in tuple: ")
print(songs_the_weeknd.index('After Hours'))

#dictionare
old_songs = data[data['released_year'] < 2005]
dict_old_songs = {}

for index, row in old_songs.iterrows():
    artist = row['artist(s)_name']
    song = row['track_name']
    dict_old_songs[artist] = song


print("\nDictionary: ")
print(dict_old_songs)
print(dict_old_songs.get("Eminem"))

#seturi
arist_names = data['artist(s)_name'].unique()
arist_names = set(arist_names)

print("\nSet:")
print(arist_names)
arist_names.clear()
print(arist_names)

#Problema 4
while(True):
    print("\n----------------------------------------")
    print("Please tell me what would you like to do: ")
    print("1- Tell you the longest artist name")
    print("2- Tell you the oldest year for a song in this dataframe")
    print("3- You are bored and you want to exit")
    print("----------------------------------------")
    print("Type your choice: ")
    choice = input()
    if int(choice) == 1:
        longest_artist_name = data['artist(s)_name'].apply(len).idxmax()
        longest_artist = data.loc[longest_artist_name, 'artist(s)_name']
        print("\nThe longest artist name is:", longest_artist)
    elif int(choice) == 2:
        oldest_year = data['released_year'].min()
        print("\nThe oldest year for a song in this dataframe is:", oldest_year)
    elif int(choice) == 3:
        print("\nExiting the program...")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

#Problema 5 iloc si loc:
random_number = 1000
while (random_number > 954):
    print("\nSpune-mi un numar (mai mic de 954 te rog): ")
    random_number = int(input())
print(data[['track_name', 'artist(s)_name']].iloc[random_number])

random_procent = 101
while (random_procent > 100 or random_procent < 0):
    print("\nSpune-mi un numar intre 0 si 100: ")
    random_procent = int(input())
print(data[['track_name', 'artist(s)_name']].loc[data['danceability_%'] == random_procent])

#Problema 6: Modul predominant intr-o melodie care a generat mai multe stream-uri
minor_streams = data['streams'][data['mode']=='Minor'].sum()
print('Numarul total de stream-uri pentru melodiile in modul predominant MINOR: ' + str(f"{minor_streams:,}"))

minor_streams = data['streams'][data['mode']=='Major'].sum()
print('Numarul total de stream-uri pentru melodiile in modul predominant MAJOR: ' + str(f"{minor_streams:,}"))

#Problema 7: pie chart cu numarul de melodii din fiecare an
import matplotlib.pyplot as plt
years = data['released_year'].value_counts().sort_index()

years.index = years.index.astype(str)
print(years)

years_df = pd.DataFrame(columns=['Period', 'Number of Songs'])

years_df.loc['1930-1979'] = years.loc['1930':'1979'].sum()
years_df.loc['1980-1999'] = years.loc['1980':'1999'].sum()
years_df.loc['2000-2009'] = years.loc['2000':'2009'].sum()
years_df.loc['2010-2015'] = years.loc['2010':'2015'].sum()

for year in range(2016, 2024):
    years_df.loc[str(year)] = years.loc[str(year)]
print(years_df)

plt.figure(figsize=(10, 6))
plt.pie(years_df['Number of Songs'], labels=years_df.index, autopct='%1.1f%%',
        startangle=140)
plt.title('Number of Songs by Period')
plt.axis('equal')  # Asigură că aspectul cercului este păstrat
plt.show()

#Problema 8: Grafic cu bare despre popularitatea melodiilor in functie de luna de lansare
 








