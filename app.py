from flask import Flask, request,jsonify,render_template


app= Flask(__name__)


@app.route("/")

def home():
    return render_template("index.html")


@app.route("/regiter",methods=["POST"])

def register():
    data-request.get_json()

    print("Received data:")


    return jsonify(
        {
            "success": True,
            "message": "Registration Sucessfully"
        }
    )

if __name__=="__main__":
    app.run(debug=True)