from flask import Flask, request,jsonify,render_template #Flask  creates our web application
# request → receives data from JavaScript
# jsonify → sends a JSON response back
# render_template → displays your HTML


app= Flask(__name__)  #Creates the Flask application.


@app.route("/")

def home():
    return render_template("index.html")  #first page index page


@app.route("/register",methods=["POST"])  #r JavaScript will send the form data here.

def register():
    data-request.get_json() #receives the JavaScript object.

    print("Received data:")


    return jsonify(
        {
            "success": True,
            "message": "Registration Sucessfully"
        }
    )

if __name__=="__main__":
    app.run(debug=True)