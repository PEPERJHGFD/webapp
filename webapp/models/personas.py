import pyrebase

config = {
  "apiKey": "AIzaSyBnMWgOtB2XVRUZgPlZVG64Tl14EHFacgc",
  "authDomain": "perla-10493.firebaseapp.com",
  "databaseURL": "https://perla-10493-default-rtdb.firebaseio.com",
  "storageBucket": "perla-10493.firebasestorage.app"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

class Personas:
    def __init__(self):
        pass
    
    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            personas_py = [] 
            
            if personas.each():  
                for item in personas.each():
                    persona = {
                        'id': item.key(),
                        'nombre': item.val().get('nombre', ''),
                        'telefono': item.val().get('telefono', '')
                    }
                    personas_py.append(persona)

            response = {
                "status": 200,
                "message": "Todo bien",
                "personas": personas_py
            }
            return response

        except Exception as error:
            print(f"Error: {error}")
            response = {
                "status": 400,
                "message": "Error en el servidor",
                "personas": []
            }
            return response
    
    def agregar_persona(self, datos):
        try:
            # Validar que los campos requeridos estén presentes
            if not hasattr(datos, 'nombre') or datos.nombre.strip() == '':
                return {"status": 400, "mensaje": "El nombre es obligatorio"}
            
            # Crear un diccionario con los datos de la persona
            persona_data = {
                "nombre": datos.nombre,
                "telefono": datos.telefono if hasattr(datos, 'telefono') else ""
            }
            
            # Insertar en Firebase (Firebase generará un ID automáticamente)
            db.child("personas").push(persona_data)
            
            return {"status": 200, "mensaje": "Persona agregada correctamente"}
        
        except Exception as error:
            print(f"Error al agregar persona: {error}")
            return {"status": 500, "mensaje": f"Error al procesar los datos: {str(error)}"}
    
    def obtener_persona(self, id_persona):
        try:
            # Obtener la persona con el ID especificado
            persona = db.child("personas").child(id_persona).get()
            
            if persona.val():
                return {
                    "id": id_persona,
                    "nombre": persona.val().get('nombre', ''),
                    "telefono": persona.val().get('telefono', '')
                }
            else:
                return None
                
        except Exception as error:
            print(f"Error al obtener persona: {error}")
            return None
    
    def editar_persona(self, id_persona, datos):
        try:
            # Validar que los campos requeridos estén presentes
            if not hasattr(datos, 'nombre') or datos.nombre.strip() == '':
                return {"status": 400, "mensaje": "El nombre es obligatorio"}
            
            # Crear un diccionario con los datos actualizados
            persona_data = {
                "nombre": datos.nombre,
                "telefono": datos.telefono if hasattr(datos, 'telefono') else ""
            }
            
            # Actualizar en Firebase
            db.child("personas").child(id_persona).update(persona_data)
            
            return {"status": 200, "mensaje": "Persona actualizada correctamente"}
            
        except Exception as error:
            print(f"Error al editar persona: {error}")
            return {"status": 500, "mensaje": f"Error al actualizar los datos: {str(error)}"}
    
    def borrar_persona(self, id_persona):
        try:
            # Eliminar la persona con el ID especificado
            db.child("personas").child(id_persona).remove()
            
            return {"status": 200, "mensaje": "Persona eliminada correctamente"}
            
        except Exception as error:
            print(f"Error al borrar persona: {error}")
            return {"status": 500, "mensaje": f"Error al eliminar los datos: {str(error)}"}