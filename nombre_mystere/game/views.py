import random
from django.shortcuts import render, redirect

# View to select the difficulty level
def select_difficulty(request):
    # Check if difficulty has been selected
    if request.method == 'POST':
        difficulty = request.POST.get('difficulty')
        # Save the selected difficulty in the session
        request.session['difficulty'] = difficulty
        return redirect('play_game')  # Redirect to the game page

    return render(request, 'game/select_difficulty.html')

# View to play the game
def play_game(request):
    # Get difficulty from session, default to 'easy' if not set
    difficulty = request.session.get('difficulty', 'easy')

    # Set the range and attempts based on the selected difficulty
    if difficulty == 'easy':
        target_range = (0, 10)
        max_attempts = 5
    elif difficulty == 'medium':
        target_range = (0, 100)
        max_attempts = 7
    else:  # hard
        target_range = (0, 1000)
        max_attempts = 10

    # Initialize the game state if it's a new game or after "Rejouer"
    if 'target_number' not in request.session:
        request.session['target_number'] = random.randint(target_range[0], target_range[1])
        request.session['attempts_left'] = max_attempts
        request.session['guesses'] = []

    # Game state variables
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
            game_over = False
        else:
            result = "Le nombre mystère est plus petit."
            game_over = False

        # End the game if the user runs out of attempts
        if attempts_left == 0 or user_guess == target_number:
            
            if attempts_left == 0 and user_guess != target_number:
                game_over = True
                win = False
            else:
                win = True
                game_over = True
        else:
            win=False
            game_over = False

        # Update the session with the results
        request.session['attempts_left'] = attempts_left
        request.session.modified = True

        return render(request, 'game/play_game.html', {
            'result': result,
            'guesses': guesses,
            'attempts_left': attempts_left,
            'game_over': game_over,
            'win':win,
            'target_number': target_number,
            'difficulty': difficulty,
        })

    # Check if "Rejouer" button was clicked, reset game state
    if 'rejouer' in request.POST:
        # Clear session data for the game
        request.session.flush()
        return redirect('select_difficulty')  # Redirect back to the difficulty selection page

    return render(request, 'game/play_game.html', {
        'attempts_left': attempts_left,
        'guesses': guesses,
        'game_over': False,
        'difficulty': difficulty,
    })
