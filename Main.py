# # Create an Intramural score tracker
# Each team entry is a list that includes
# print("How Many Teams We Have?")
# team_amount = int(input())
# if team_amount <= 1:
#     print("You Need At Least Two Teams!\nBye!")
#
# else:
#         #   - Name
#     for counter in range(team_amount):
#         print("Gor it!\nWhat's The Team's Name? ")
#         team_name = input()
#         #   - Games Played
#         print("How many Games Played? ")
#         games = int(input())
#         #   - Wins
#         print("How Many Wins? ")
#         wins = int(input())
#         #   - Losses
#         print("How Many Loses? ")
#         loses = int(input())
#         #   - Ties
#         print("How Many Ties? ")
#         ties = int(input())
#         #   - Goals For
#         print("How Many Goals For? ")
#         goals_for = int(input())
#         #   - Goals against
#         print("And How Many Goals Against? ")
#         goals_against = int(input())
#
#         team_score = wins + ties + goals_for - loses - goals_against
#         print(team_name,"has",wins,"wins,",loses,"loses,", ties,"ties,",goals_for,"goals for, and",goals_against,"goals against.",team_name,"current score:",team_score,"points")
#
#         print("BYE!!!")
        # You will ask how many teams are playing.
        # Loop that many times, create a team and set all scores to 0, then append it to your list of teams
        # Start an infinite loop for main menu
        #   1) Add score
        #   2) See Team stats
        #   3) See Overall Standings
        #   4) Quit

        #   1) Enter team 1, team 2, goals for team 1, goals for team 2
        #       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie

        #   2) Print a list of team names.
        #       Once the user selects, Print out their stats

        #   3) Print out the teams in order from most team points to least
        #   - Team points = wins*2 + ties*1
        #   - If they have the same points, look for most goals for
        #   - If they have the same goals for, take the least goals against.
        #   - If those are the same, then just output the teams.

        #   4) Say goodbye and break out of the lo_opf

print("1) Add Score\n"
      "2) See Team stats\n"
      "3) See Overall stats\n"
      "4) Quit\n")
main_menu = int(input())
if main_menu == 1:
    # if team_amount <= 1:
    #     print("You Need At Least Two Teams!\nBye!")
    # else:
    #     for counter in range(team_amount):
        print("OK!\nWhat's The First Team's Name? ")
        team_name = input()
        print("What's The Second Team's Name? ")
        team_name2 = input()
        #- Games Played
        print("How Many Games First Team Played? ")
        games = int(input())
        print("how Many Games Second Team Played?")
        games2 = int(input())
        #   - Wins
        print("How Many First Team Won? ")
        wins = int(input())
        print("How Many Second Team Won? ")
        wins2 = int(input())
        #   - Losses
        print("How Many Games First team Lost? ")
        loses = int(input())
        print("How Many Games Second Team Lost?")
        loses2 = int(input())
        #   - Ties
        print("How Many Ties First Team Have?")
        ties = int(input())
        print("How Many Ties Second Team Have?")
        ties2 = int(input())
        #   - Goals For
        print("How Many Goals For First Team Have?")
        goals_for = int(input())
        print("How Many Goals For Second Team Have?")
        goals_for2 = int(input())
        #   - Goals against
        print("How Many Goals Against First Team Have?")
        goals_against = int(input())
        print("And How Many Goals Against Second Team Have?")
        goals_against2 = int(input())
        team_score = wins + ties + goals_for - loses - goals_against
        team_score2 = wins2 + ties2 + goals_for2 - loses2 - goals_against2
        print(team_name,"has", team_score, "points")
        print(team_name2,"has", team_score2, "points")
        if team_score > team_score2:
            print(team_name,"Won!")
        elif team_score < team_score2:
            print(team_name2,"Won!")
        else:
            print("TIE!")
elif main_menu == 2:
    print("which team's stats do you want top see?")
    if find_team_name == team_name:
         print(team_name,"has",wins,"wins,\n",loses,",loses\n", ties,"ties,\n",goals_for,"goals for,\nand",goals_against,"goals against.\n",team_name,"current score:",team_score,"points")
         print(team_name2,"has", wins2,"wins,\n",loses2,"loses,\n",ties2,"ties,\n",goals_for2,"goals for",goals_against2,"goals againsts.\n",team_name2,"current score:",team_score2,"points" )
    else:
        print("That Team Was Not Found")
elif main_menu == 3:
    print("Coming Soon!")
elif main_menu == 4:
    print("\nEND!")