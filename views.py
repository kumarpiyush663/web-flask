from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")


# http://192.168.29.4:8000/views/
@views.route("/")
def home():
    return render_template("index.html", name="Dunggeon", age=24)


# http://192.168.29.4:8000/views/profile/pk
@views.route("/profile/<username>")
def profileContext(username):
    return render_template("index.html", name=username, age=24)


# http://192.168.29.4:8000/views/profile?name=pk
@views.route("/profile")
def profileVariable():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name, age=24)


# http://192.168.29.4:8000/views/json
@views.route("/json")
def get_json():
    return jsonify({'name': 'PK', 'age': 25})


# http://192.168.29.4:8000/views/data
@views.route("/data", methods=["POST"])
def get_data():
    data = request.json
    # Validate the request body contains JSON
    print(request)
    if request.is_json:

        # Parse the JSON into a Python dictionary
        req = request.get_json()

        # Print the dictionary
        print(req)

        # Return a string along with an HTTP status code
        return jsonify(data)

    else:

        # The request body wasn't JSON so return a 400 HTTP status code
        return "Request was not JSON", 400

# http://192.168.29.4:8000/views/go-to-home
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))