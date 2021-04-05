import flask
from flask import request, jsonify
from flask_cors import cross_origin, CORS

app=flask.Flask('application')
app.config["DEBUG"]=True
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/tea/*": {"origins": "http://localhost:port"}})

teas=[
    {'id':0,
    'title':'Genmaicha',
    'type':'Green Tea'},
    {'id':1,
    'title':'Earl Grey',
    'type':'Black Tea'}
]

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

@app.route('/',methods=['GET'])
def home():
    return "<h1>Let's Go</h1>"

@app.route('/tea/all',methods=['GET'])
def api_all():
    return jsonify(teas)

@app.route('/tea/search',methods=['GET'])
def api_id():
    if 'id' in request.args:
        id=int(request.args['id'])
    else:
        return 'Error: no id specified'

    results=[]

    for tea in teas:
        if tea['id']==id:
            results.append(tea)

    return jsonify(results)

app.run()