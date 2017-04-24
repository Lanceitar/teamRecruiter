""" The Hello_Bitcamp project is a simple program to ask
people to be on my team at Bitcamp until the team
was full. """

# TODO: Equip the program to take in different more responses other than y and n.
# TODO: Tool a better UI for users.

# Variables for Hello_Bitcamp
type = 'Programmer'
teamNum = 4
hlp = 'Plz hlp join me plz!'
yis = "We did it! We are a team.(*・∀・*)人(*・∀・*)"
team = ['Ian']

"""Keep asking for people to join the team until
the team has four members."""
while teamNum > 0:
    message = hlp

    """Print to user what my skills categorize, the number of people
    are on the team, and the appropriate help message (hlp or yis)."""
    def print_message():
        print("{0} looking for {1} more team mates! {2}".format(type, teamNum, message))

    print_message()

    person = input('Will you help and join? Y/N')
    answer = person.upper() # convert the users input to upper case

    if answer == 'Y':
        teamNum -= 1
    else:
        print(message)

message = yis
print_message()