from flask import Flask, render_template, request

app = Flask(__name__)


def check_upper_lower(username: str) -> dict:
    result = {"capital": False, "small": False, "number": False}
    letters = list(username)
    if letters[-1].isnumeric():
        result['number'] = True
    for letter in letters:
        if ord('A') <= ord(letter) <= ord('Z'):
            result['capital'] = True
        if ord('a') <= ord(letter) <= ord('z'):
            result['small'] = True
        if result['capital'] and result['small']:
            return result
    return result


@app.route("/results")
def results():
    username = request.args.get("username")
    result = check_upper_lower(username)
    errors = []
    for key, value in result.items():
        if not result[key]:
            if key == 'capital':
                errors.append("You did not use an uppercase character")
            elif key == 'small':
                errors.append("You did not use an smaller case character")
            elif key == 'number':
                errors.append("You did not use a number at the end")
    print(errors)
    return render_template('results.html', errors=errors)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
