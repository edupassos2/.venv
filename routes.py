from flask import request, jsonify
from models import User, Transaction
from services.bank_integration import fetch_bank_transactions
from app import db  # Certifique-se de que o db está sendo importado corretamente

def init_routes(app):
    @app.route('/api/register', methods=['POST'])
    def register():
        data = request.json
        user = User(name=data['name'], email=data['email'], password_hash=data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'})

    @app.route('/api/login', methods=['POST'])
    def login():
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and user.password_hash == data['password']:
            return jsonify({'message': 'Login successful'})
        return jsonify({'message': 'Invalid credentials'}), 401

    @app.route('/api/transactions', methods=['GET', 'POST'])
    def transactions():
        if request.method == 'POST':
            data = request.json
            transaction = Transaction(
                user_id=data['user_id'],
                amount=data['amount'],
                category=data['category'],
                date=data['date'],
                description=data['description']
            )
            db.session.add(transaction)
            db.session.commit()
            return jsonify({'message': 'Transaction added successfully'})
        else:
            user_id = request.args.get('user_id')
            transactions = Transaction.query.filter_by(user_id=user_id).all()
            return jsonify([t.to_dict() for t in transactions])

    @app.route('/api/fetch_bank_transactions', methods=['GET'])
    def bank_transactions():
        user_id = request.args.get('user_id')
        transactions = fetch_bank_transactions(user_id)
        return jsonify(transactions)