from flask import render_template

from app import app
from models import News, Post


@app.route('/')
@app.route('/index')
def index():
    news = News().all()
    return render_template('index.html',
                           news=news)

@app.route('/post')
def post():
    news = News().all()
    posts = [Post(a_news) for a_news in news]
    return render_template('post.html',
                           posts=posts)