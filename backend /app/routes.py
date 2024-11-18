from flask import request, jsonify
from app import app, db
from app.models import Lead

@app.route('/leads', methods=['GET'])
def get_leads():
    leads = Lead.query.all()
    return jsonify([lead.to_dict() for lead in leads])

@app.route('/leads', methods=['POST'])
def add_lead():
    data = request.json
    new_lead = Lead(name=data['name'], email=data['email'])
    db.session.add(new_lead)
    db.session.commit()
    return jsonify(new_lead.to_dict()), 201
