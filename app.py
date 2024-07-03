from flask import Flask, request, jsonify

app = Flask(__name__)

posts = {
    0: {
        'id': 0,
        "title": "Hello World",
    }
}
post_id_counter = 1
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/api/posts/", methods={"GET"})
def get_all_posts():
    return jsonify({"posts": list(posts.values())}), 200
    
if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)





