from flask import Flask, redirect, url_for, render_template, request
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from calculate import calculaterBETA


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sendparameter", methods=["POST"])
def sendParameter():
    global firstp, secondp, thirdp
    firstp = float(request.form["params"])
    secondp=float(request.form["paramf"])
    #thirdp= (request.form["filef"])
    print("first parameter: ", firstp)
    print("second parameter: ", secondp)
    #print("Third parameter: ", thirdp)
    f = request.files['filef']
    f.save(os.path.join(app.root_path, 'uploaded_files', secure_filename(f.filename)))
    print ('file uploaded successfully')
    calculaterBETA(firstp, secondp)


    return redirect(request.referrer)

#@app.route("/<varb>/")
#def usecase(varb):
#    return f"Hello {varb}"

#@app.route("/admin")
#def admin():
#    return redirect(url_for("usecase", varb="admin!"))

if __name__ == '__main__':
    app.run(debug=True)