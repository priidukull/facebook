from flask import render_template, request

from app import app
from models import News, Post
from publish import Publishing


@app.route('/')
@app.route('/index')
def index():
    news = News().all()
    return render_template('index.html',
                           news=news)

@app.route('/post', methods=['POST', 'GET'])
def post():
    a_news_id = request.form.get('id')
    if a_news_id:
        a_news = News().one(a_news_id)
        Publishing().publish_one(a_news)
    news = News().all()
    posts = [Post(a_news) for a_news in news]
    return render_template('post.html',
                           posts=posts)

