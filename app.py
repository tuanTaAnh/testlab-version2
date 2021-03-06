from flask import *
import time

app=Flask(__name__,template_folder='templates')

c = 0 # global variable
idG = int(time.time())

@app.route('/')
def upload():
    return render_template("index.html", data={}), 200

@app.route('/save', methods=["POST", "GET"])
def save_btn():
    id = idG

    data = request.form['data']
    print(json.loads(data))

    notes = request.form['notes']
    print(notes)

    with open(f'./savesong/song_{id}.json', 'w+') as fp:
        json.dump(data, fp)

    f = open(f'./savesong/song_{id}.txt', "a")
    f.truncate(0)
    f.write(notes)
    f.close()

    print("SAVE SUCCESS!")

    url = request.url.split("/save")[0]
    return jsonify({"id" : id, "url" : url + f"/song/{id}"}), 200


@app.route('/song/<id>', methods=["POST", "GET"])
def load_song(id=None):
    with open(f'./savesong/song_{id}.json') as fp:
        data = json.load(fp)
    return render_template('index.html'), 200

@app.route('/data/<id>', methods=["POST", "GET"])
def load_song_data(id=None):
    print('aaaaaaaaa')
    with open(f'./savesong/song_{id}.json') as fp:
        data = json.load(fp)
    print("Data: ", data)
    return data, 200


@app.route('/notes/<id>', methods=["POST", "GET"])
def load_notes(id=None):
    # open and read the file after the appending:
    f = open(f'./savesong/song_{id}.txt', "r")
    notes = f.read()
    data = {"notes" : notes}
    print("ACCESS LOAD_NOTES")
    return data, 200


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(debug=True)