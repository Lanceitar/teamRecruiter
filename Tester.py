type = 'Programmer'
teamNum = 4
hlp = 'Plz hlp join me plz!'
yis = "We did it! We are a team.(*・∀・*)人(*・∀・*)"
team = ['Ian']

while teamNum > 0:
    message = hlp

    def printMessage():
        print("{0} looking for {1} more team mates! {2}".format(type, teamNum, message))

    printMessage()

    person = input('Will you help and join? Y/N')
    answer = person.upper()

    if answer == 'Y':
        teamNum -= 1
    else:
        print(message)

message = yis
printMessage()