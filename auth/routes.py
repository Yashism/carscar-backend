# auth/routes.py

from . import auth_bp

@auth_bp.route('/auth/login')
def login():
    # Handle login logic
    return {"Login":"Successful"}
