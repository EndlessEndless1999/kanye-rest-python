from application import db, app


app.app_context().push()


class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(100), nullable=False)

    @property
    def json(self):
        return {"id": self.id, "quote": self.quote}

