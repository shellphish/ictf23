import logging
from pprint import pprint
from flask import Flask, request, jsonify, session, render_template
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from models import User, Document
from database import db
from __init__ import create_app

app = create_app()

login_manager = LoginManager()
login_manager.init_app(app)

# Retrieves and uses the gunicorn logger if it exists
if __name__ != '__main__':
    try:
        gunicorn_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers = gunicorn_logger.handlers
        app.logger.setLevel(gunicorn_logger.level)
    except Exception as e:
        print(f"Cannot set the logger: {e}")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

logging.debug("Starting the application")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'GET':
            return render_template('register.html')
        elif request.method == 'POST':
            data = request.get_json()
            
            # Validate input
            username = data.get('username')
            password = data.get('password')
            
            if not username or not password:
                return jsonify({"message": "Username and password are required"}), 400

            # Check if the user already exists
            existing_user = User.query.filter_by(username=username).first()

            if existing_user:
                return jsonify({"message": "Username already exists"}), 400

            # Hash the password
            hashed_password = generate_password_hash(password, method='sha256')

            # Create a new user and add to database
            new_user = User(username=username, password=hashed_password)
            
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
            
            user = User.query.filter_by(username=username).first()
            
            if not user or not check_password_hash(user.password, password):
                return jsonify({"message": "Invalid username or password"}), 401
                
            login_user(user)
            
            return jsonify({"message": "Authenticated successfully"}), 200
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/documents', methods=['GET'])
@login_required
def documents():
    try:
        # Fetch all documents for the user
        user_documents = Document.query.filter_by(user_id=current_user.id).all()
        doc_list = [{"id": doc.id, "title": doc.title} for doc in user_documents]
        return render_template('documents.html', documents=doc_list)
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/add_document', methods=['POST'])
@login_required
def add_document():
    try:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')

        new_document = Document(title=title, content=content, user_id=current_user.id)
        
        db.session.add(new_document)
        db.session.commit()

        return jsonify({"message": "Document added"}), 201
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/add_file', methods=['POST'])
@login_required
def add_file():
    try:
        data = request.get_json()
        filename = secure_filename(data.get('fileName'))
        content = data.get('fileContent')

        with open(f"/tmp/app/{filename}", mode="w") as f:
            f.write(content)

        return jsonify({"message": "File added"}), 201
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/add_document_from_file', methods=['POST'])
@login_required
def add_document_from_file():
    try:
        data = request.get_json()
        logging.debug(data)
        title = data.get('title')
        filename = data.get('filename')

        with open(f"/tmp/app/{filename}", mode="r") as f:
            content = f.read()

        new_document = Document(title=title, content=content, user_id=current_user.id)
        
        db.session.add(new_document)
        db.session.commit()

        return jsonify({"success": True, "message": "Document added", "id": new_document.id}), 201
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/read_document/<int:document_id>', methods=['GET'])
@login_required
def read_document(document_id):
    try:
        document = Document.query.filter_by(id=document_id, user_id=current_user.id).first()
        if not document:
            return jsonify({"message": "Document not found"}), 404

        return jsonify({"success": True, "title": document.title, "content": document.content}), 200
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/remove_document/<int:document_id>', methods=['DELETE'])
@login_required
def remove_document(document_id):
    try:
        document = Document.query.filter_by(id=document_id, user_id=current_user.id).first()
        logging.debug((f"Found document {document}"))
        if not document:
            return jsonify({"message": "Document not found"}), 404

        db.session.delete(document)
        db.session.commit()

        return jsonify({"success": True}), 200
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    try:
        if request.method == 'GET':
            return render_template('logout.html')
        elif request.method == 'POST':
            logout_user()  # Ends the user session
            return jsonify({"message": "Logged out successfully"}), 200
    except Exception as e:
        pprint(e)
        return jsonify({"message": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
