# URL_FOR used to create dynamic urls
from flask import Flask, render_template, request

flask_app = Flask(__name__, template_folder='templete')


@flask_app.route('/', methods=['GET', 'POST'])
def index():
    # url = request.form.get('url')
    # return render_template('index.html',url=url)
    if request.method == 'POST':
        url = request.form.get('url')
        return render_template('index.html', url=url)

    return render_template('index.html')


if __name__ != "__main__":
    pass
else:
    flask_app.run(debug=False,host='0.0.0.0')
