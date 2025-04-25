import pandas as pd 
import numpy as np

#1
music = pd.read_csv('spotifycsv/Spotify_2024_Global_Streaming_Data.csv')
print(music)
print(music.describe())

#2
# Середня кількість прослуховувань за останній місяць у артистів.
df1 = music.groupby('Artist')[['Streams Last 30 Days (Millions)']].mean()
print(df1)

# Мінімальна кількість прослуховувань за останній місяць у артистів.
df2 = music.groupby('Artist')[['Streams Last 30 Days (Millions)']].min().sort_values(by=['Streams Last 30 Days (Millions)'], ascending=True)
print(df2)

# Максимальна кількість прослуховувань за останній місяць у артистів.
df3 = music.groupby('Artist')[['Streams Last 30 Days (Millions)']].max().sort_values(by=['Streams Last 30 Days (Millions)'], ascending=False)
print(df3)

# Загальна кількість прослуховувань за останній місяць у артистів.
df4 = music.groupby('Artist')[['Streams Last 30 Days (Millions)']].sum()
print(df4)

# Кількість прослуховувань за останній місяць у артистів.
df5 = music.groupby('Artist')[['Streams Last 30 Days (Millions)']].count()
print(df5)

#3
table = pd.DataFrame(
    {
        'Artist': ['Taylor Swift', 'Ed Sheeran ', 'BLACKPINK', 'BTS', 'Doja Cat', 'Billie Eilish'],
        'Country': ['Germany', 'United States', 'Italy', 'Canada', 'Brazil', 'Sweden'],
        'Album': ['1989 (Taylors Version)', 'Autumn Variations', 'BORN PINK', 'Proof', 'Future Nostalgia', 'Happier Then Ever'],
        'Platform Type': ['Free', 'Premium', 'Free', 'Premium', 'Free', 'Premium'],
        'Streams' : [118.51, 166.05, 196.16, 102.72, 192.80, 193.71]
    }
)
print(table)

piv_table = table.pivot_table(values='Streams', index='Artist', columns='Platform Type', aggfunc='mean')
print(piv_table)

