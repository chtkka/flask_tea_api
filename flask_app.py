import flask
from flask import request, jsonify
from flask_cors import cross_origin, CORS

app=flask.Flask('application')
app.config["DEBUG"]=True
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

teas=[
    {'id':0,
    'title':'Genmaicha',
    'type':'Green Tea',
    'shortDesc':'A distinctive blend of Japanese green tea and whole roasted brown rice',
    'longDesc':'Genmaicha is sometimes referred to as "popcorn tea" due to the popped rice grains. The sugar and starch from the rice gives it a nutty and full flavor, mixing with the grassy taste found in all green tea.<br/><br/>Genmaicha can also be mixed with mathca powder called "matcha-iri genmaicha" giving it a stronger flavor.',
    'color':'#989f7a',
    'image':'https://i.ibb.co/N1WYQPB/green.png',
    'imageShadow':'https://i.ibb.co/hZfX1FZ/green-Shadow.png'},
    {'id':1,
    'title':'Oolong Tea',
    'type':'Green Tea',
    'shortDesc':'A traditional, nutritious, and relaxing tea.',
    'longDesc':'A traditional Chinese tea produced from the leaves of the Camellia sinensis plant, the same plant that is used to make black and green tea. Oolong tea however, is oxidized to a balance between the less oxidized green tea, and fully oxidized black tea, giving it a unique taste.',
    'color':'#989f7a',
    'image':'https://i.ibb.co/N1WYQPB/green.png',
    'imageShadow':'https://i.ibb.co/hZfX1FZ/green-Shadow.png'},
    {'id':2,
    'title':'Matcha',
    'type':'Green Tea',
    'shortDesc':'Used traditionally as a tea and food dye.',
    'longDesc':'Matcha was first made in the Tang Dynasty when China was exporting green tea as bricks for efficiency. The tea was pulverized and mixed with water and salt. This method was popularized later in the Song Dynasty, and transitioned into the tea we know and love today.<br/><br/>Matcha has since been used as a food dye for noodles, rice, and even ice cream.',
    'color':'#989f7a',
    'image':'https://i.ibb.co/N1WYQPB/green.png',
    'imageShadow':'https://i.ibb.co/hZfX1FZ/green-Shadow.png'},
    {'id':3,
    'title':'Sencha',
    'type':'Green Tea',
    'shortDesc':'The most popular tea in all of Japan',
    'longDesc':'The direct counterpart to matcha, Sencha is made by infusing whole tea leaves in hot water. Sencha has a different flavor depending on when in the year it is harvestedm however Shincha is considered the most delicious, as it is the first harvest containing the most tender leaves.',
    'color':'#989f7a',
    'image':'https://i.ibb.co/N1WYQPB/green.png',
    'imageShadow':'https://i.ibb.co/hZfX1FZ/green-Shadow.png'},
    {'id':4,
    'title':'Earl Grey',
    'type':'Black Tea',
    'shortDesc':'A swift, steady infusion of energy.',
    'longDesc':'A world-famous tea that became popular in the 1830s when Prime Minister Charles Grey of England recieved the tea as a gift from a Chinese envoy.<br/><br/>Traditional Earl Grey tea is made with Bergamot oil found from Bergamot oranges, a winter blossoming tree grown in Calabria, Italy. The orange provides a floral, delicate citrus taste that complements the character of black tea.',
    'color':'#a83939',
    'image':'https://i.ibb.co/k8tsK3K/black.png',
    'imageShadow':'https://i.ibb.co/3mcySHb/black-Shadow.png'},
    {'id':5,
    'title':'Darjeeling',
    'type':'Black Tea',
    'shortDesc':'The “champagne of tea”',
    'longDesc':'Only found in the mountainous town of Darjeeling, India, the taste of this tea can vary depending on when it was harvested, but usually has fruity and floral notes.',
    'color':'#a83939',
    'image':'https://i.ibb.co/k8tsK3K/black.png',
    'imageShadow':'https://i.ibb.co/3mcySHb/black-Shadow.png'},
    {'id':6,
    'title':'Chamomile',
    'type':'Herbal Tea',
    'shortDesc':'Herbs from daisies providing immense health benefits.',
    'longDesc':'A popular tea derived from the Chamomile herb found in daisy-like floweres from the Asteraceae family. It has been used for many centuries as a natural medicine for health conditions.<br/><br/>Chamomile can be enjoyed as a somewhat similar taste to a green or black tea, without the chaffeine.',
    'color':'#fff5b5',
    'image':'https://i.ibb.co/hdKkcCn/herbal.png',
    'imageShadow':'https://i.ibb.co/z5HMnhg/herbal-Shadow.png'},
    {'id':7,
    'title':'Peppermint',
    'type':'Herbal Tea',
    'shortDesc':'A small taste of Christmas.',
    'longDesc':'Peppermint tea is one of the most drank herbal teas in the world. It is made using peppermint oil and sometimes some other herbs. Peppermint oil has had many uses as relaxants, as well as a provider of pain relief.',
    'color':'#fff5b5',
    'image':'https://i.ibb.co/hdKkcCn/herbal.png',
    'imageShadow':'https://i.ibb.co/z5HMnhg/herbal-Shadow.png'},
    {'id':8,
    'title':'Ginger & Honey',
    'type':'Herbal Tea',
    'shortDesc':'Sugar and spice for your health.',
    'longDesc':'Ginger tea provides an alternative spicy taste with the same disease fighting properties and antioxidants found in other herbal teas.<br/><br/>Pairing the ginger with honey gives a smooth drinking experience, with a small kick to give you energy.',
    'color':'#fff5b5',
    'image':'https://i.ibb.co/hdKkcCn/herbal.png',
    'imageShadow':'https://i.ibb.co/z5HMnhg/herbal-Shadow.png'},
    {'id':9,
    'title':'Rooibos',
    'type':'Herbal Tea',
    'shortDesc':'A new contender to the healthy herbal lineup.',
    'longDesc':'Rooibos tea is made from the roots of the rooibos plant, a red bushy plant, found in South Africa. Rooibos tea has a slightly bitter taste with a sweet after taste.<br/><br/>Rooibos tea has just begun to be studied, but some finds indicate it may help promote bone growth and reduce inflammation.',
    'color':'#fff5b5',
    'image':'https://i.ibb.co/hdKkcCn/herbal.png',
    'imageShadow':'https://i.ibb.co/z5HMnhg/herbal-Shadow.png'},
    {'id':10,
    'title':'Strawberry',
    'type':'Black Tea',
    'shortDesc':'Light, yet full.',
    'longDesc':'A Ceylon and Keemun black tea mix combiend with a natural strawberry flavoring to create a light and smooth base with a full-bodied and sweet flavorful taste of strawberry.',
    'color':'#a83939',
    'image':'https://i.ibb.co/k8tsK3K/black.png',
    'imageShadow':'https://i.ibb.co/3mcySHb/black-Shadow.png'},
    {'id':11,
    'title':'Apricot',
    'type':'Black Tea',
    'shortDesc':'Natural fruity notes with a smooth base.',
    'longDesc':'Blended Ceylon and Keemun black teas combined with a ripe apricot flavor and calendula and elder flower petals to provide a full, naturally fruity taste with a smooth base from the Ceylon and Keemun.',
    'color':'#a83939',
    'image':'https://i.ibb.co/k8tsK3K/black.png',
    'imageShadow':'https://i.ibb.co/3mcySHb/black-Shadow.png'},
    {'id':12,
    'title':'Orange & Cinnamon',
    'type':'Black Tea',
    'shortDesc':'Nostalgia in a cup.',
    'longDesc':'A blend of Ceylon and Keemun black teas combined with cinnamon and piquant cloves, complemented by the tangy citrus of fresh oranges. This creates a smooth light blend with a full and rich taste of orange and cinnamon that will remind you of days past.',
    'color':'#a83939',
    'image':'https://i.ibb.co/k8tsK3K/black.png',
    'imageShadow':'https://i.ibb.co/3mcySHb/black-Shadow.png'}
]

@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])

@app.route('/',methods=['GET'])
def home():
    return "Use the endpoints /tea/all with optional argument of pages=number of results, /tea/search with the required argument id=id 0-12, or /tea/type with the required argument type=Black Tea,Green Tea, Herbal Tea and/or pages=number of results"

@app.route('/tea/all',methods=['GET'])
def api_all():
    if 'pages' in request.args:
        pages=int(request.args['pages'])
    else:
        return jsonify(teas)

    results=[]

    for tea in teas:
        if tea['type']==id:
            results.append(tea)

    for tea in teas:
        if tea['id'] < pages:
            results.append(tea)

    return jsonify(results)

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

@app.route('/tea/type',methods=['GET'])
def api_type():
    if 'type' in request.args:
        id=str(request.args['type'])
    else:
        return 'Error: no id specified'


    results=[]
    tr=[]

    for tea in teas:
        if tea['type']==id:
            results.append(tea)

    if 'pages' in request.args:
            pages=int(request.args['pages'])
            for i in range(pages):
                tr.append(results[i])

    if 'pages' in request.args:
        return jsonify(tr)
    else:
        return jsonify(results)