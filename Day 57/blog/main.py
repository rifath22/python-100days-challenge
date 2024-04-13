from flask import Flask, render_template
from post import Post

app = Flask(__name__)
all_posts = Post()
@app.route('/')
def home():
    show_posts = all_posts.get_all_data()
    return render_template("index.html", posts=show_posts)

@app.route('/blog/<int:id>')
def blog(id):
    single_posts = all_posts.single_post(id)
    return render_template("post.html", posts=single_posts)

if __name__ == "__main__":
    app.run(debug=True)
