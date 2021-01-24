from sqlalchemy.exc import IntegrityError

from extensions import db


class Manager:
    Model = None

    def __init__(self):
        if self.Model is not None:
            self.model = self.Model

    def retrieve(self, pk, *args):
        query = self.Model.query.get(pk)
        return True, query

    def list(self, *args):
        query = self.Model.query.filter_by(*args)
        return True, query.all()

    def create(self, data, commit=True):
        data = self.Model(**data)
        db.session.add(data)
        try:
            if commit:
                db.session.commit()
            else:
                db.session.flush()
        except IntegrityError as e:
            return False, {'database': [str(e.orig)]}
        return True, data

    def delete(self, pk, commit=True):
        instance = self.Model.query.get(pk)
        if instance:
            db.session.delete(instance)
        else:
            return False, {'critical': ['Resource was not found.']}
        try:
            if commit:
                db.session.commit()
            else:
                db.session.flush()
        except IntegrityError as e:
            return False, {'critical': [str(e.orig)]}
        return True, None
