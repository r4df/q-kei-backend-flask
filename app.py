from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.secret_key = 'your-secret-key'
CORS(app)

login_manager = LoginManager()
login_manager.init_app(app)

# User model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# In-memory user store (for demo purposes)
users = {'testuser': {'password': 'password123'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username in users and users[username]['password'] == password:
        user = User(username)
        login_user(user)
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials!"}), 401

# Protected route
@app.route('/profile')
@login_required
def profile():
    return jsonify({"message": f"Hello, {current_user.id}!"})

# Logout route
@app.route('/logout')
def logout():
    logout_user()
    return jsonify({"message": "Logged out!"})

if __name__ == '__main__':
    app.run(debug=True)
