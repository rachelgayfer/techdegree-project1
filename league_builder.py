import csv

# make sure the script doesn't execute when imported
if __name__ == "__main__":

    # open and road the CSV file as dictionary
    with open("soccer_players.csv") as csvfile:
        players = csv.DictReader(csvfile, delimiter=",")

        # make empty lists for different categories of players and teams
        experienced_players = []
        inexperienced_players = []
        raptors = []
        dragons = []
        sharks = []

        # append players to the appropriate list depending on experience
        for row in players:
            if row['Soccer Experience'] == 'YES':
                experienced_players.append(row)
            else:
                inexperienced_players.append(row)

        # add players to their teams incorporating even mix of experienced and no experience
        raptors.append(experienced_players[0])
        raptors.append(experienced_players[1])
        raptors.append(experienced_players[2])
        raptors.append(inexperienced_players[0])
        raptors.append(inexperienced_players[1])
        raptors.append(inexperienced_players[2])

        sharks.append(experienced_players[3])
        sharks.append(experienced_players[4])
        sharks.append(experienced_players[5])
        sharks.append(inexperienced_players[3])
        sharks.append(inexperienced_players[4])
        sharks.append(inexperienced_players[5])

        dragons.append(experienced_players[6])
        dragons.append(experienced_players[7])
        dragons.append(experienced_players[8])
        dragons.append(inexperienced_players[6])
        dragons.append(inexperienced_players[7])
        dragons.append(inexperienced_players[8])

# Create text file names teams.txt
with open("teams.txt", "w") as file:
        file.write("Raptors\n")
        # write each team in the required format
        for item in raptors:
            file.write("{Name}, {Soccer Experience}, {Guardian Name(s)}\n".format(**item))
        file.write("Sharks\n")
        for item in sharks:
            file.write("{Name}, {Soccer Experience}, {Guardian Name(s)}\n".format(**item))
        file.write("Dragons\n")
        for item in dragons:
            file.write("{Name}, {Soccer Experience}, {Guardian Name(s)}\n".format(**item))