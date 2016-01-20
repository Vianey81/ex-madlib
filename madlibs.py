from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_game_form():
    
    player = request.args.get("person")
    answer = request.args.get("playgame")

    if answer == "No":
        return render_template("goodbye.html",
                                person=player)
    else:
        return render_template("game.html")

@app.route('/madlib', methods=["POST"])
def show_madlib():
    name = request.form.get("name")
    color = request.form.get("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    quantity = request.form.get("quantity")
    theme = request.form.get("theme")

    return render_template("madlib.html",
                            name=name,
                            color=color,
                            noun=noun,
                            adjective=adjective,
                            quantity=quantity,
                            theme=theme)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
