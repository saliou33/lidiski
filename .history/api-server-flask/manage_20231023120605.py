from api import app, db
from api.models import User, Role

def create_user(user):
    user.password = User.generate_hash(user.password)
    db.session.add(user)
    db.session.commit()


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
