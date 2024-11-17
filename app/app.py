from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Rock beats Scissors, Scissors beats Paper, Paper beats Rock
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    
    return "Computer wins!"

@app.route('/', methods=['GET', 'POST'])
def index():
    chosen_move = None
    computer_move = None
    result = None

    if request.method == 'POST':
        chosen_move = request.form.get('move')
        # Randomly select computer's move
        computer_move = random.choice(['rock', 'paper', 'scissors'])
        # Determine the winner
        result = determine_winner(chosen_move, computer_move)

    return render_template('index.html', chosen_move=chosen_move, computer_move=computer_move, result=result)

if __name__ == '__main__':
    app.run(debug=True)
