from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from dotenv import load_dotenv
import os


from .models import User

app = Flask(__name__)
app.secret_key = 'your-secret-key'

# ########## CORS ##########
frontend_url = os.getenv("FRONTEND_URL")
CORS(app, origins=[frontend_url])

login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# ################################
# ########## BLUEPRINTS ##########
# ################################
from .services.home import home_bp
from .services.login import login_bp

app.register_blueprint(home_bp)
app.register_blueprint(login_bp, url_prefix = "/login")

# Projects
from .services.projects.tictactoe import proj_tictactoe_bp
app.register_blueprint(proj_tictactoe_bp, url_prefix = "/api/proj/tictactoe")