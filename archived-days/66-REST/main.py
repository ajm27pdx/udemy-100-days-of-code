from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self):
        dictionary = {}
        
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    
@app.route('/random')
def random_cafe():
    results = db.session.execute(db.select(Cafe)).scalars().all()
    cafe = random.choice(results)
    return jsonify(cafe.to_dict())

@app.route('/all')
def all_cafes():
    results = db.session.execute(db.select(Cafe)).scalars().all()
    all_cafes = []
    for cafe in results:
        all_cafes.append(cafe.to_dict())
        
    return jsonify(all_cafes)

@app.route('/search')
def search_loc():
    loc = request.args.get('loc')
    results = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    
    if results:
        return jsonify(response=[cafe.to_dict() for cafe in results])
    else:
        return jsonify(response={'error' : 'sorry, no cafes found'})

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    new_cafe = Cafe(
                    name = request.form['name'],
                    map_url = request.form['map_url'],
                    img_url = request.form['img_url'],
                    location = request.form['location'],
                    seats = request.form['seats'],
                    has_toilet = request.form['has_toilet'].lower() == 'true',
                    has_wifi = request.form['has_wifi'].lower() == 'true',
                    has_sockets = request.form['has_sockets'].lower() == 'true',
                    can_take_calls = request.form['can_take_calls'].lower() == 'true',
                    coffee_price = request.form['coffee_price']
    )
    
    try:
        db.session.add(new_cafe)
        db.session.commit()
    except:
        return jsonify(response={'error': 'could not add cafe'})
    else:
        return jsonify(response={'sucess': new_cafe.to_dict()})
    
    
@app.route('/update-price/<int:n>', methods=["PATCH"])
def update_price(n):
    new_price = request.args.get('new_price')
    try:
        cafe_to_update = db.session.execute(db.select(Cafe).where(Cafe.id == n)).scalar()
        cafe_to_update.coffee_price = new_price
        db.session.commit()
    except:
        return jsonify(response={'error': 'id not found'}), 404
    else:
        return jsonify(response={'success': f"updated {cafe_to_update.name}'s price to {new_price}"})

@app.route('/delete-cafe/<int:n>', methods=["DELETE"])
def delete_cafe(n):
    user_key = request.args.get('api-key')
    if user_key == 'TopSecret':
        try: 
            cafe_to_delete = db.session.execute(db.select(Cafe).where(Cafe.id == n)).scalar()
            db.session.delete(cafe_to_delete)
            db.session.commit()
        except:
            return jsonify(response={'error': f'{n} not found'}), 404
        else:
            return jsonify(response={'sucess': f'deleted id {n}'})
    else:
        return jsonify(response={'error': 'not allowed'}), 403

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record



if __name__ == '__main__':
    app.run(debug=True)
