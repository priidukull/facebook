from functools import wraps

from flask import render_template, request, g
from flask.ext.login import current_user

from app import app, login_manager
from app.forms import LoginForm
from app.models import News, Post, User
from publish import Publishing


def login_required(func):
    '''
    If you decorate a view with this, it will ensure that the current user is
    logged in and authenticated before calling the actual view. (If they are
    not, it calls the :attr:`LoginManager.unauthorized` callback.) For
    example::

        @app.route('/post')
        @login_required
        def post():
            pass

    If there are only certain times you need to require that your user is
    logged in, you can do so with::

        if not current_user.is_authenticated():
            return current_app.login_manager.unauthorized()

    ...which is essentially the code that this function adds to your views.

    It can be convenient to globally turn off authentication when unit
    testing. To enable this, if either of the application
    configuration variables `LOGIN_DISABLED` or `TESTING` is set to
    `True`, this decorator will be ignored.

    :param func: The view function to decorate.
    :type func: function
    '''
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated():
            return login(func(*args, **kwargs))
        return func(*args, **kwargs)
    return decorated_view

@login_manager.user_loader
def load_user(id):
    return User().get(id)

@app.before_request
def before_request():
    g.user = current_user

def login(func):
    form = LoginForm()
    if form.validate_on_submit():
        return func
    return render_template("login.html", form=form)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    a_news_id = request.form.get('id')
    if a_news_id:
        a_news = News().one(a_news_id)
        Publishing().publish_one(a_news)
    news = News().all()
    posts = [Post(a_news) for a_news in news]
    return render_template('index.html',
                           posts=posts)


