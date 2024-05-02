from app import app
from model.userModel import userModel
obj = userModel() 

@app.route('/user/signup')
def signup():
    return obj.user_signup_model()