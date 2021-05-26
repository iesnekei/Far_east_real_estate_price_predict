import json

from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from requests.exceptions import ConnectionError
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import DataRequired

import urllib.request
import json

class ClientDataForm(FlaskForm):
    rooms = StringField('Number of  rooms: ', validators=[DataRequired()])
    m2 = StringField('Squares : ', validators=[DataRequired()])
    floor = StringField('Floor: ', validators=[DataRequired()])
    total_floor = StringField('Total Floor: ', validators=[DataRequired()])
    city_or_village = StringField('If city input 1, opposite 0', validators=[DataRequired()])


app = Flask(__name__)
app.config.update(
    CSRF_ENABLED=True,
    SECRET_KEY='you-will-never-guess',
)

def get_prediction(rooms, m2, floor, total_floor, city_or_village ):
    body = {
        'rooms': rooms,
        'm2': m2,
        'floor': floor,
        'total_floor': total_floor,
        'city_or_village': city_or_village
    }

    myurl = "http://0.0.0.0:8180/predict"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    #print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    return json.loads(response.read())['predictions']

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predicted/<response>')
def predicted(response):
    response = json.loads(response)
    print(response)
    return render_template('predicted.html', response=response)


@app.route('/predict_form', methods=['GET', 'POST'])
def predict_form():
    form = ClientDataForm()
    data = dict()
    if request.method == 'POST':
        data['rooms'] = request.form.get('rooms')
        data['m2'] = request.form.get('m2')
        data['floor'] = request.form.get('floor')
        data['total_floor'] = request.form.get('total_floor')
        data['city_or_village'] = request.form.get('city_or_village')


        try:
            response = str(get_prediction(
                data['rooms'],
                data['m2'],
                data['floor'],
                data['total_floor'],
                data['city_or_village']
                                          ))
            print(response)
        except ConnectionError:
            response = json.dumps({"error": "ConnectionError"})
        return redirect(url_for('predicted', response=response))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
