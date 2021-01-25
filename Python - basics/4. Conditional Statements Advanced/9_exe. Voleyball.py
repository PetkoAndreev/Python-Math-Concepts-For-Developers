import math
type_year = input()
weekends = 48
holidays = int(input())
hometown_weekends = int(input())
sofia_weekends = weekends - hometown_weekends

games_sofia = sofia_weekends * 3 / 4
games_hometown = hometown_weekends
games_holidays = holidays * 2 / 3
total_games = games_sofia + games_hometown + games_holidays

if type_year == 'leap':
    total_games += 0.15 * total_games

print(math.floor(total_games))