from infra.config.connection import DBConnectionHandler
from infra.entities.uniforme import Uniforme


class UniformeRepository:

    @staticmethod
    def select_uniforme_by_id(id_uniforme):
        with DBConnectionHandler() as db :
            return db.session.query(Uniforme).filter(Uniforme.id == id_uniforme).first()


    @staticmethod
    def select_uniforme_by_name(name_uniforme):
        with DBConnectionHandler() as db :
            return db.session.query(Uniforme).filter(Uniforme.nome == name_uniforme).first()

    @staticmethod
    def select_all_uniformes():
        with DBConnectionHandler() as db :
            return db.session.query(Uniforme).all()


    @staticmethod
    def select_first_uniforme():
        with DBConnectionHandler() as db :
            return db.session.query(Uniforme).first()

    @staticmethod
    def insert_many_uniformes(uniformes):
        with DBConnectionHandler() as db :
            if isinstance(uniformes, list):
                db.session.query(Uniforme).add_all(uniformes)
                db.session.commit()
            else:
                print(uniformes)

    @staticmethod
    def insert_one_uniforme(uniforme):
        with DBConnectionHandler() as db :
            db.session.add(uniforme)
            db.session.commit()

    @staticmethod
    def update_uniforme(uniforme):
        with DBConnectionHandler() as db :
            db.session.query(Uniforme).filter(Uniforme.id == uniforme.id).update({'nome': uniforme.nome})
            db.session.commit()

    @staticmethod
    def delete_uniforme(uniforme):
        with DBConnectionHandler() as db :
            db.session.query(Uniforme).filter(Uniforme.id == uniforme.id).update({'ativo': False})
            db.session.commit()
