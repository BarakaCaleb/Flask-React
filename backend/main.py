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

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = map(lambda x: x.to_json(), contacts)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)