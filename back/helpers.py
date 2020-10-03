from data.model import db
from sqlalchemy.exc import SQLAlchemyError

class DataManager():

    def add(self, *args):
        try:
            for request in args:
                db.session.add(request)
                db.session.commit()
                return 'welcome'
        except SQLAlchemyError as e:
            print(e)
        except:
            return 'error'
    
    def update(self):
        try:
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            print(e)
        except:
            return 'error'
    
    def delete(self,id_a):
        try:
            db.session.delete(id_a)
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            print(e)
        except:
            return 'error'

    def consult(self, id_e):
        try:
            db.session.query(id_e).first()
            db.session.commit()
            return 'ok'
        except SQLAlchemyError as e:
            print(e)
        except:
            return 'error'

import bcrypt

class EncrypyPass():
    
    def do(self, password):
        hash_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        return hash_password