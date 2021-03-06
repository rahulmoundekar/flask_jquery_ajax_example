# Flask Jquery Ajax:

![python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)

#### Project Setup

  - Making the project as :
    ```
    mkdir flask_jquery_ajax_example
	cd flask_jquery_ajax_example
    ```
  - Install flask:
    ```
    pip install flask
    ```
 - Integrating SqlAlchemy
    ```
    pip install sqlalchemy
    ```
  - create project architecture like below
     ![N|Solid](structure.PNG) 
     
  - Create Setting.py for development
     ```python
    # configuration
    class Config:
        DEBUG = True
        # db
        SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/flaskapp'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
     ```   
  - Create app.py for development
     ```python
    from flask import Flask, render_template, request, jsonify, json
    from db.db import db
    from models.app_model import Messages
    
    app = Flask(__name__)
    app.secret_key = 'asrtarstaursdlarsn'
    app.config.from_object('settings.Config')
    
    # initialization
    db.init_app(app)
    
    
    @app.route('/', methods=['GET'])
    def indexView():
        return render_template('index.html')
    
    
    @app.route('/comments', methods=['GET', 'POST'])
    def comments():
        if request.method == 'POST':
            message = request.form.get('message')
            try:
                messages_entry = Messages(message=message)
                db.session.add(messages_entry)
                db.session.commit()
                return jsonify({'status': 200, 'success': 'Your comment Registered.!!',
                                'message': messages_entry.serialize()})
            except Exception as e:
                return jsonify(
                    {'status': 500, 'error': e.__str__(), 'message': 'Something Internal Server Error! try later.!!'})
        else:
            messages = Messages.query.order_by(Messages.id.desc()).all()
            return jsonify(messages=[e.serialize() for e in messages])
    
    
    # licenses = License.query.filter_by(person_id=person_id).first()
    # run always put in last statement or put after all @app.route
    if __name__ == '__main__':
        app.run(host='localhost')

     ```
  - Declaring Models:
     ```python
    from db.db import db
    class Messages(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        message = db.Column(db.String(400))
    
        def serialize(self):
            return {"id": self.id,
                    "message": self.message}
     ``` 
  - In order to run app:
     ```
	   python app.py
     ```
  - run on your Browser: 
    * You should run get employees: http://localhost:5000/         