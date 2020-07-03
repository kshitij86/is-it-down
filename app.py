from flask import *


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    lyrics = None
    artist = None

    if request.method == 'POST':
        artist = request.form['artist']
        lyrics = request.form['lyrics']
        return render_template('index.html', lyrics=lyrics, artist=artist)

    else:
        return render_template('index.html', lyrics=lyrics, artist=artist)


if __name__ == "__main__":
    app.run(debug=True)
