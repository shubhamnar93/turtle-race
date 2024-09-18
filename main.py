from turtle import Screen
from turtle_race import TurtleRace

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

if user_input:
    race = TurtleRace()
    race.run_race()

    if race.winner == user_input:
        print("You win!")
    else:
        print("You lose.")
    print(f"{race.winner} wins the race")

screen.exitonclick()
