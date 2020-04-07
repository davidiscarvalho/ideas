class Data(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username_ = db.Column(db.String(120))
    nif_ = db.Column(db.Integer, unique=True)

    def __init__(self, name_, nif_):
        self.username_ = username_
        self.nif_ = nif_
