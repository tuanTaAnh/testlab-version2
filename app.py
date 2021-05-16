from flask import *


app=Flask(__name__,template_folder='templates')



@app.route('/')
def upload():
    return render_template("index.html")

@app.route('/save', methods=["POST"])
def save_btn():
    print(request.form);
    url = request.url.split("/save")[0];
    return jsonify({"id" : 1, "url" : url  + "/song/1"})


@app.route('/song/1', methods=["POST"])
def song():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
