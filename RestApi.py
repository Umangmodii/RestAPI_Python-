from flask import Flask, request, jsonify

# Create a Flask

api = Flask(__name__)


# Route Define
@api.route("/get-user/<user_id>")
def get_user(user_id):

    user_data = {
        "User_ID": user_id,
        "Username": "Umang",
        "Email": "Umangmodi003@gmail.com"
    }

    page = request.args.get("page")
    
    if page:
        user_data["page"] = page
    
    return jsonify(user_data), 200 # Success

# Postman

@api.route("Create-user", method=["Post"])

def create_user():
    data = request.get_json()
    
    return jsonify(data), 201  #Success

# Four APi
# Get
# Post
# Put/Update
# Delete

if __name__ == "__main__":
    api.run(debug=True)
    
    
# Output

