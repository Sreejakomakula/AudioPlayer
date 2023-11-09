from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")
    
@app.route('/songs/<path:filename>')
def serve_songs(filename):
    return send_file('songs/' + filename)
    
@app.route('/songs/<path:filename>')
def serve_image(filename):
    return send_file('songs/' + filename)

if __name__ == '__main__':
    app.run(debug=True)

