# Create
# - first_name 
# - last_name
# - email

# Request 
# type: PUT, DELETE

# Response 
# Status

from flask import Request, jsonify
from config import app, db
from models import Contact





if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)