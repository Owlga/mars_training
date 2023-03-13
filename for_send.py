from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/training/<prof>')
def mars(prof):
    return render_template('base.html', title=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')