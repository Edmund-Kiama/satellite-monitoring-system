@app.py
from Flask_bcrypt import Bycrypt

bcrypt = Bcrypt(app)

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return str(e)

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"message": "Username and password required"}, 400
        
        existing_user = User.query.filter_by(username = username).first()

        if existing_user:
            return {"message": "User already exists"}

        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "User created successfully"}, 201
api.add_Resource(Register, "/register")

class Login(Resource):

    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        user = User.query.filter(User.username = username).first()

        if not user or not user.check_password(password):
            return {"message": "Unauthorized Access"}

        session['user_id'] = user.id
        
        return user.to_dict()