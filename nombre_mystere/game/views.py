import random
from django.shortcuts import render

def play_game(request):
    # Reset the game if 'rejouer' is clicked
    if 'rejouer' in request.POST:
        request.session.clear()  # This will clear the session data and restart the game

    # Initialize the game state if it's a new game
    if 'target_number' not in request.session:
        request.session['target_number'] = random.randint(0, 100)
        request.session['attempts'] = 10
        request.session['attempts_left'] = 10
        request.session['guesses'] = []

    # Initialize game state variables
    target_number = request.session['target_number']
    attempts_left = request.session['attempts_left']
    guesses = request.session['guesses']

    # Handle the user's guess if they have submitted one
    if request.method == "POST" and 'guess' in request.POST:
        user_guess = int(request.POST.get('guess'))
        guesses.append(user_guess)
        attempts_left -= 1
        request.session['attempts_left'] = attempts_left
        request.session['guesses'] = guesses

        # Check if the guess is correct
        if user_guess == target_number:
            result = "Félicitations, vous avez trouvé le nombre mystère!"
            game_over = True
        elif user_guess < target_number:
            result = "Le nombre mystère est plus grand."
        else:
            result = "Le nombre mystère est plus petit."

        # End the game if the user runs out of attempts
        if attempts_left == 0 or user_guess == target_number:
            game_over = True
        else:
            game_over = False

        # Update the session with the results
        request.session['attempts_left'] = attempts_left
        request.session.modified = True

        return render(request, 'game/play_game.html', {
            'result': result,
            'guesses': guesses,
            'attempts_left': attempts_left,
            'game_over': game_over,
            'target_number': target_number,
        })

    return render(request, 'game/play_game.html', {
        'attempts_left': attempts_left,
        'guesses': guesses,
        'game_over': False,
    })
