from flask import *
from check import *


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        site = request.form['site']
        res = check_site(site)
        isUp = res[1]
        status_code = res[0] 
        return render_template('index.html', site=site, isUp=isUp, status_code=status_code)

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
