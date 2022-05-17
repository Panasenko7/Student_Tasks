from flask import Flask , escape ,request
app = Flask(__name__)

# чтобы запустить зайди в папку и напиши в консоли flask run
# , добавь "--host 0.0.0.0"чтобы можнобыло заходить с других устройств
#  ctrl+c в консоли чтобы остановить


@app.route('/')  # что будет если зайти по адресу главной странички
def hello():
    name = request.args.get('name','World')
    return f'Andrew Panasenko, 777'
if __name__ == '__main__':
    app.run('0.0.0.0')



# @app.route('/hui')  # что будет если зайти по адресу /hui
# def pizda():
#
#     return 'pizda!'
