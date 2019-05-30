'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча
и выводит на стандартный вывод сводную таблицу результатов всех матчей.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Пример ввода:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
'''
table_of_matches = []
list_of_teams = []
score_table = {}
team_stats = []
games = 0
draw = 0
wins = 0
lose = 0
score = 0
# input of data
n = int(input())
for i in range(n):
    match = input().split(';')
    if match[1] > match[3]:
        match.append('w')
    elif match[1] == match[3]:
        match.append('d')
    if match[1] < match[3]:
        match.append('l')
    table_of_matches.append(match)
# print(table_of_matches)

# work with teams
for i in table_of_matches:
    for j in i:
        if len(j) > 1:
            if j not in list_of_teams:
                list_of_teams.append(j)
# print(list_of_teams)

# creating score table
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
for team in list_of_teams:
    for i in table_of_matches:
        for j in i:
            if team == j:
                games += 1
        # score_table[team] = [team_stats[0]]
        # for i[0] in table_of_matches:
        if i[0] == team:
            if i[4] == 'd':
                draw += 1
            elif i[4] == 'w':
                wins += 1
            elif i[4] == 'l':
                lose += 1
        if i[2] == team:
            if i[4] == 'd':
                draw += 1
            elif i[4] == 'l':
                wins += 1
            elif i[4] == 'w':
                lose += 1
    score = wins * 3 + draw
    team_stats.append(str(games))
    team_stats.append(str(wins))
    team_stats.append(str(draw))
    team_stats.append(str(lose))
    team_stats.append(str(score))
    # print(team_stats)
    score_table[team] = [team_stats[0], team_stats[1], team_stats[2], team_stats[3], team_stats[4]]
    games = 0
    draw = 0
    wins = 0
    lose = 0
    score = 0
    team_stats.clear()
for i in score_table:
    t = " ".join(score_table[i])
    print(str(i) + ':' + str(t))
