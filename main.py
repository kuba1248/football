"""
FOOTBALL MATCH SIMULATOR!!!
PLEASE READ INTRO BEFORE RUNNING!!!
15 FOOTBALL TEAMS:
BARCELONA
MADRID
SEVILLA
ATLETICO MADRID
VALENCIA
MANCHESTER CITY
MANCHESTER UNITED
CHELSEA
TOTTENHAM
LIVERPOOL
NAPOLI
JUVENTUS
INTER MILAN
AS ROMA
LAZIO

SAMPLE INPUT IS TWO TEAM(FROM ABOVE LIST)ON DIFFERENT LINES E.G
BARCELONA
MADRID


PLEASE ONLY TEAMS LISTED ABOVE ARE AVAILABLE AND TEAM NAMES SHOULD BE SPELT AS SEEN IN THE ABOVE LIST!
"""
import time
import random

# global variables
# spanish teams
barcelona = ['Barcelona', 'LUIS SUAREZ', 'MESSI', 'DEMBELE', 'RAKITIC', 'SERGIO.B', 'A. INIESTA', 'SEMEDO', 'PIQUE',
             'ALBA', 'MASCHERANO', 'TER STEGEN']
madrid = ['Real Madrid', 'RONALDO', 'BALE', 'BENZEMA', 'KROOS', 'MODRIC', 'ISCO', 'CARVAJAL', 'SERGIO RAMOS', 'MARCELO',
          'CASEMIRO', 'KEYLOR NAVAS']
valencia = ['Valencia', 'GEOFFREY KONDOGBIA', 'RAFAEL', 'FERRAN TORRES', 'NEMANJA', 'PAREJO', 'ANDRREAS PERERIA',
            'JOSE LUIS', 'MARTIN', 'EZEQUEIL GARAY', 'JAVIER JIMENEZ', 'GABRIEL PAULISTA']
amadrid = ['Atlético Madrid', 'FERNANDO TORRES', 'KEVIN GAMEIRO', 'ANTOINE GRIEZMAN', 'SAUL', 'KOKE', 'GABI',
           'JUANFRAN', 'STEFAN SAVIC', 'DIEGO GODIN', 'FILIPE LUIS', 'JAN OBLAK']
sevilla = ['Sevilla', 'STEVAN JOVETIC', 'POZO', 'LUCIANO VIETTO', 'SAMIR NASRI', 'PABLO SARABIA', 'FRANCO VASQUEZ',
           'GABRIEL MERCADO', 'NICOLAS PAREJA', 'ADIL RAMI', 'BENOIT TREMOULINAS', 'SERGIO RICO']
# english teams
manc = ['Manchester City', 'KUN AGUERO', 'GABRIEL JESUS', 'RAHEEM STERLING', 'DAVID SILVA', 'KEVIN DE BRUYNE',
        'FERNANDINHO', 'BENJAMIN MENDY', 'NICOLAS OTAMENDI', 'JOHN STONES', 'KYLE WALKER', 'CLAUDIO BRAVO']
manu = ['Manchester United', 'ZLATAN IBRAHIMOVIC', 'ROMELU LUKAKU', 'ANTHONY MARTIAL', 'MATA', 'NEMANJA MATIC',
        'PAUL POGBA', 'ERIC BAILLY', 'CHRIS SMALLING', 'ANTINIO VALENCIA', 'ASHLEY YOUNG', 'DE GEA']
chelsea = ['Chelsea', 'EDEN HAZARD', 'MORATA', 'WILLIAN', 'CESC FABREGAS', "N'GOLO KANTE", 'MARCOS ALONSO',
           'AZPILICUETA', 'DAVID LUIZ', 'ANTONIO RUDIGER', 'DAVIDE ZAPPACOSTA', 'THIBAUT COURTOIS']
tottenham = ['Tottenham', 'HARRY KANE', 'HEUNG-MIN SON', 'DELE ALLI', 'MOUSA DEMBELE', 'ERIC DIER', 'CHRISTIAN ERIKSON',
             'TOBY ALDERWEIRALD', 'DANNY ROSE', 'KIERAN TRIPPIER', 'KYLE WALKER', 'HUGO LLORIS']
liverpool = ['Liverpool', 'SADIO MANE', 'ROBERTO FIRMINO', 'DANIEL STURRIDGE', 'COUTINHO', 'MOHAMED SALAH',
             'GEORGINIO WIJNALDUM', 'ALBERTO MORENO', 'NATHANIEL CLYNE', 'JOEL MATIP', 'JAMES MILNER', 'SIMON MIGNOLET']
# italian teams
napoli = ['Napoli', 'LORENZO INSIGNE', 'JOSE CALLEJON', 'LEONARDO PAVOLETTI', 'ALLAN', 'MAREK HAMSIK', 'JORGINHO',
          'VLAD CHIRICHES', 'KALIDOU KOULIBALY', 'CHRISTIAN MAGGIO', 'RAUL ALBIOL', 'PEPE REINA']
juventus = ['Juventus', 'PAULO DYBALA', 'GONZALO HIGUAIN', 'MARIO  MANDZUKIC', 'KWADWO ASAMOAH', 'JUAN CAUDRADO',
            'SAMI KHEDIRA', 'MEDHI BENATIA', 'LEONARDO BONUCCI', 'GIORGIO CHIELLINI', 'DANI ALVES', 'GIANlUIGI BUFFON']
inter = ['Inter Milan', 'MOHAMED BAKAYOKO', 'EDER', 'GABRIEL BARBOSA', 'MARCELO BROZOVIC', 'ANTONIO CANDREVA',
         'GARY MEDEL', 'MARCO ANDREOLLI', 'CRISTIAN ANSALDI', "DANILO D'AMBROSIA", 'MIRANDA', 'SAMIR HANDANOVIC']
roma = ['AS Roma', 'EDIN DZEKO', 'STEPHAN EL SHAARAWAY', 'FRANCESCO TOTTI', 'DANIELE DE ROSSI', 'ALESSANDRO FLORENZI',
        'LORENZO GROSSI', 'BRUNO PERES', 'EROS DE SANTIS', 'EMERSON', 'FEDERICO FAZIO', 'WOJCIECH SZCZESNY']
lazlo = ['Lazio', 'FELIPE CAICEDO', 'CIRO IMMOBILE', 'NAANI', 'DAVIDE DI GENNARO', 'FELIPE ANDERSON', 'NICOLO ARMINI',
         'DUSAN BASTA', 'BASTOS', 'JORDAN LUKAKU', 'MAURICIO', 'THOMAS STRAKOSHA']

bra = ['Barcelona', 'LUIS SUAREZ', 'MESSI', 'DEMBELE', 'RAKITIC', 'SERGIO.B', 'A. INIESTA', 'SEMEDO', 'PIQUE',
       'ALBA', 'MASCHERANO', 'TER STEGEN']
rm = ['Real Madrid', 'RONALDO', 'BALE', 'BENZEMA', 'KROOS', 'MODRIC', 'ISCO', 'CARVAJAL', 'SERGIO RAMOS', 'MARCELO',
      'CASEMIRO', 'KEYLOR NAVAS']

gpause = time.sleep(18)

team1 = chelsea
team2 = manu
goals = 0
scorers = []


# randoms
def select_team():
    global team1, team2, checker, checker2
    checker2 = True
    checker = None
    teams = {'BARCELONA': barcelona, 'MADRID': madrid, 'VALENCIA': valencia, 'ATLETICO MADRID': amadrid,
             'SEVILLA': sevilla, 'MANCHESTER CITY': manc, 'MANCHESTER UNITED': manu, 'CHELSEA': chelsea,
             'TOTTENHAM': tottenham, 'LIVERPOOL': liverpool, 'NAPOLI': napoli, 'JUVENTUS': juventus,
             'INTER MILAN': inter, 'AS ROMA': roma, 'LAZIO': lazlo, 'BRA': bra, 'RM': rm}
    team1 = input('First Team:  ').upper()
    print(team1)
    if team1 in teams.keys():
        team1 = teams[team1]
        checker = True
    else:
        print(team1, 'Does not exist or has not yet been added!!!')
        checker = False
    print('')

    team2 = input('Second Team: ').upper()
    print(team2)
    if team2 in teams.keys():
        team2 = teams[team2]
        if checker != False:
            checker = True
    else:
        print(team2, 'Does not exist or has not yet been added')
        checker = False
    print('')

    if team2 == team1:
        checker2 = False


select_team()


def find_team(player):
    if player in team1:
        return team1
    else:
        return team2


def randomness():
    global team, w, teams, strikers, midfielders, re, rea
    w = random.randint(1, 2)
    teams = (team1, team2)
    team = random.choice(teams)
    strikers = random.choice(team[1:3])
    midfielders = random.choice(team[4:6])
    re = [strikers, midfielders]
    rea = random.choice(re)
    gpause


randomness()
defenders = None


def organize(rea):
    global defenders
    if rea in team1:
        defenders = random.choice(team2[7:-2])
    else:
        defenders = random.choice(team1[7:-2])


def versus():
    print('{0}   VS   {1}'.format(team1[0], team2[0]))


def beautifulgoal():
    global scorers
    global goals
    goals += 1
    print('{0} gets the ball takes it past 1!'.format(rea))
    print('2 PLAYERS!')
    print('3 WHOLE PLAYERS!!')
    if w == 1:
        print('And {0} scores a beautiful goal!'.format(rea))
        entry = (rea, j)
        scorers.append(entry)
    else:
        print('He misses upon all his hardwork')
    gpause


def lineup():
    print('The of lineup of {0} is:'.format(team1[0]))
    for i in team1[1::]:
        print(i)

    time.sleep(3)
    print('\n\nThe of lineup of {0} is:'.format(team2[0]))
    for i in team2[1::]:
        print(i)


def scoresheet():
    global scorers
    c = 0
    minutes = []
    goal_scorers = []
    goalcount1 = 0
    goalcount2 = 0
    for i in scorers:
        goal_scorers.append(scorers[c][0])
        c += 1
    c = 0
    for i in scorers:
        minutes.append(scorers[c][1])
        c += 1
    for i in goal_scorers:
        if i in team1:
            goalcount1 += 1
        else:
            goalcount2 += 1
    print("""
FINAL SCORE:
{0}:{1}
{2}:{3}     
 """.format(team1[0], goalcount1, team2[0], goalcount2))
    print('SCORERS:')
    c = 0
    for i in goal_scorers:
        print("{0} \t '{1}'".format(i, str(minutes[c])))
        c += 1


def penalty():
    global scorers
    global rea
    organize(rea)
    print('{0} dashes into the penalty box'.format(rea))
    print('But is roughly tackled by {0}'.format(defenders))
    r = random.randint(1, 2)
    if r == 1:
        print('THE REFEREE POINTS TO THE SPOT')
        if w == 1:
            print('And {0} smashes it into the net'.format(rea))
            entry = (rea, j)
            scorers.append(entry)
        else:
            print('The keeper saves it!')
    else:
        print('The refree waves it off!!')
    gpause


def freekick():
    global scorers
    i = random.randint(1, 2)
    print('{0} is tackled very close to the box'.format(rea))
    print('ITS A FREE KICK!')
    if i == 1:
        print('{0} Misses!'.format(rea))
    else:
        print('GOAL!!!')
        entry = (rea, j)
        scorers.append(entry)

    i = random.randint(1, 2)
    w = random.randint(1, 2)
    gpause


def header():
    global scorers
    global w
    rea = random.choice(team[1:3])
    print('{0} gets his head on a cross by {1}'.format(rea, midfielders))
    time.sleep(1)
    if w == 1:
        print('But it sails over the post!')
    else:
        print('GOAL!!!')
        entry = (rea, j)
        scorers.append(entry)
    gpause


def longshot():
    global scorers
    rn = random.randint(1, 3)
    rea = random.choice(team[1:6])
    print('{0} fancies his luck from far!!!'.format(rea))
    if rn == 1:
        print('And he smashes it into the net!!!')
        print('GOAL!!!')
        entry = (rea, j)
        scorers.append(entry)
    if rn == 2:
        print('That was nowhere near the post!!!')
        print('What a horrible shot by {0}!!!'.format(rea))
    if rn == 3:
        print('Ooooh so close but it hits the bar!!!')
    gpause


# referee events
def card(player):
    global yellow, red, defend, rea
    card = random.randint(1, 3)
    if card == 1:
        print('The refree gives a hard talk to {0}'.format(player))
    if card == 2:
        print('Its a yellow card for {0}!!!'.format(player))
        yellow.append(player)
    if card == 3 and defend in yellow:
        print('Its a red card for {0}'.format(player))
        print("He's Off!!!")
        t = find_team(player)
        t.remove(player)
    if card == 3 and defend not in yellow:
        if player != rea:
            print('The refree says play on!!!')
    gpause


def booking():
    global yellow, red, defend
    yellow = []
    red = []
    rea = random.choice(team[1:6])
    organize(rea)
    defend = defenders
    rn = random.randint(1, 3)
    wound = random.randint(1, 10)
    if rn == 1:
        print('{0} tries to get past {1} with a few cheeky skills!!!'.format(rea, defend))
        print('But {0} delivers a hard takle!!!'.format(defend))
        card(defend)
    if rn == 2:
        print('{0} and {1} are in a tight struggle for the ball!!!'.format(rea, defend))
        print('{0} ends up pushing {1} down!!!'.format(defend, rea))
        card(defend)
    if rn == 3:
        print('{0} goes down easily from a challenge'.format(rea))
        print('The refree says its a dive!!!')
        card(rea)
    if wound == 7 and rn != 3:
        injury(rea)
    gpause


def injury(player):
    rn = random.randint(1, 2)
    if rn == 1:
        print('{0} has suffered a nasty injury!!!'.format(player))
        print('And has to be taken off!!!')
        print('The fans cheer as he walks of the pitch!!!')
        t = find_team(player)
        t.remove(player)
    if rn == 2:
        print('{0} as reveived a slight injury!!!'.format(player))
        print('He has been taken off for treatment at the sidelines')
    gpause


def volley_curler():
    global scorers
    rea = random.choice(team[1:3])
    midfielder = random.choice(team[4:6])
    rn = random.randint(1, 2)
    g = random.randint(1, 2)
    if rn == 1:
        print('{0} tries a shot, but the ball gets deflected!!!'.format(rea))
        print('{0} volleys it back into the box with a thump!!!'.format(midfielder))
        if g == 1:
            print('Flies into the net!!!')
            print('GOAL!!!')
            entry = (rea, j)
            scorers.append(entry)
        else:
            print('OFF TARGET!!!')
    if rn == 2:
        print('{0} dribbles with the ball at the side of the box!!!'.format(rea))
        print('Goes for a curling effort!!!')
        if g == 1:
            print('What an amazing goal!!!!!')
            entry = (rea, j)
            scorers.append(entry)
        else:
            print('What a horrible shot!!')
    gpause


def opposite(player):
    if player in team1:
        return team2
    if player in team2:
        return team1


def counter_attack():
    global scorers
    g = random.randint(1, 2)
    te = find_team(rea)
    te2 = opposite(rea)
    print('{0} failed attack has left {1} on the charge!!!'.format(te2[0], te[0]))
    print('{0} leads the charge!!!'.format(rea))
    print('{0} dribbles past the opposing defenders!!!'.format(rea))
    print('And he goes for goal!!!')
    if g == 1:
        print('Wonderful Goal!!!')
        entry = (rea, j)
        scorers.append(entry)
    else:
        print('Wasted Effort!!!')
    gpause


j = 1


def min(j):
    print('{0} MINUTES'.format(j))


def display(func1, func2):
    print('')


def events():
    global j
    mpause = time.sleep(20)
    spause = time.sleep(5)
    while j <= 90:

        e = random.randint(1, 100)
        spause
        if j == 1:
            print(j, 'MINUTE\nKICK OFF!!!\n')
            j += 1
            mpause

        if j == 45:
            print(j, 'MINUTES\nHALF TIME!!!\n')
            j += 1
            mpause

        if j == 90:
            print(j, 'MINUTES\nFULL TIME!!!\n')
            j += 1
            mpause

        if e in range(1, 2):
            display(min(j), header())
            j += 1
            mpause

        elif e == 99:
            display(min(j), beautifulgoal())
            j += 1
            mpause

        elif e == 94:
            display(min(j), penalty())
            j += 1
            mpause

        elif e in range(45, 47):
            display(min(j), freekick())
            j += 1
            mpause

        elif e == 20:
            display(min(j), booking())
            j += 1
            mpause

        elif e in range(80, 83):
            display(min(j), longshot())
            j += 1
            mpause

        elif e in range(75, 78):
            display(min(j), volley_curler())
            j += 1
            mpause

        elif e == 38:
            display(min(j), counter_attack())
            j += 1
            mpause

        else:
            j += 1

        randomness()
        mpause


def main():
    if checker == True and checker2 == True:
        time.sleep(1)
        lineup()
        time.sleep(1)
        print('*' * 40)
        versus()
        print('*' * 40)

        time.sleep(1)
        randomness()
        time.sleep(1)
        events()

        time.sleep(1)
        scoresheet()
        time.sleep(1)
    if checker == False:
        print("""
PLEASE PICK FROM THE AVAILABLE TEAMS WHICH ARE:
BRA
RM
BARCELONA
MADRID
SEVILLA
ATLETICO MADRID
VALENCIA
MANCHESTER CITY
MANCHESTER UNITED
CHELSEA
TOTTENHAM
LIVERPOOL
""")
    if checker2 == False:
        print('Can Not Play A Team Against Itself!!!')


main()
