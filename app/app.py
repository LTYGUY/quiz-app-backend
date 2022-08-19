from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from server import init_server
from config import Config

app = init_server()
app.config.from_object(Config)
db = SQLAlchemy(app)

class Model(db.Model):
    
    __tablename__ = 'Model'
    id = db.Column(db.Integer, primary_key=True)

@app.route('/')
def index() -> str:
    
    return render_template('index.html')

def main():

    port = app.config['PORT']
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == "__main__":
    main()
