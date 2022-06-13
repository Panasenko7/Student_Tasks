from flask import Flask, escape, request, render_template, redirect
app = Flask(__name__)

# чтобы запустить зайди в папку и напиши в консоли flask run
# , добавь "--host 0.0.0.0"чтобы можнобыло заходить с других устройств
#  ctrl+c в консоли чтобы остановить
list_with_data = []


@app.route('/')  # что будет если зайти по адресу главной странички
def hello():

    return f'Andrew Panasenko, 777'


@app.route('/input_data')  # что будет если зайти по адресу главной странички
def input_data():
    return render_template('my_first_html.html')


@app.route('/show_data')  # что будет если зайти по адресу главной странички
def show_data():
    return f'{list_with_data}'


@app.route('/show_inverted_data')  # что будет если зайти по адресу главной странички
def show_inverted_data():
    return f'{list_with_data}'[::-1]


@app.route('/save_data', methods=['POST'])  # что будет если зайти по адресу главной странички
def save_data():
    list_with_data.append(f"input_1 value is {request.form['input_1']}, input_2 value is {request.form['input_2']}")
    return redirect('/input_data')


if __name__ == '__main__':
    app.run('0.0.0.0')



# @app.route('/hui')  # что будет если зайти по адресу /hui
# def pizda():
#
#     return 'pizda!'
