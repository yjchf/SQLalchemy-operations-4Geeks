from sqlalchemy import select, Column
from models import People, Planets, Films, Locations,Character


class Database_Operations:
    # Constructor to initialize the object
    def __init__(self, session):
        self.session = session

    #####################
    # Planets operations
    #####################
    def planet_create(self, **kwargs):
        # Validación de los campos importantes
        if not kwargs.get('name'):
            raise ValueError("El campo 'name' es obligatorio para crear un planeta")
        
        planeta = Planets(**kwargs)

        try:

            self.session.add(planeta)

            self.session.commit()
            return planeta

        except Exception as e:
            self.session.rollback()
            print(f"Error al crear la persona: {e}")
            return None


    def planet_get(self, id):
        return self.session.query(Planets).filter_by(id=id).first( )

    def planet_find_by_name(self, name):
      return self.session.query(Planets).filter_by(name=name).first()

    def planet_list(self):
        return self.session.query(Planets).all()

    def planet_edit(self, id,**kwargs):

        planeta = self.session.query(Planets).filter_by(id=id).first()
        if not planeta:
            raise ValueError("No se ha encontrado planeta para el id proporcionado")
        for key,value in kwargs.items():
            if key != "id":
                if hasattr(planeta,key):
                    setattr(planeta,key, value)
        try:
            self.session.commit()
            return planeta
        except Exception as e:
            self.session.rollback()
            print(f"Error al editar el planeta {e}")
        return None

    def planet_delete(self):
        return None

    ###################
    # Films operations
    ###################
    def film_create(self):
        return None

    def film_get(self):
        return None
        
    def film_get_episode(self):
      return None

    def film_list(self):
        return None

    def film_edit(self):
        return None

    def film_delete(self):
        return None

    ###################
    # People operations
    ###################
    def people_create(self):
        return None

    def people_get(self):
        return None

    def people_list(self):
        return None

    def people_edit(self):
        return None

    def people_delete(self):
        return None

    ##############################
    # Operations with relationships
    ##############################

    def film_add_locations(self):
       return None

    def film_add_characters(self):
        return None
    
    def film_remove_locations(self):
        return None

    def film_remove_characters(self):
        return None
