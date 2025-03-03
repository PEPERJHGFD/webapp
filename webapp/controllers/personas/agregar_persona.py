import web
from models.personas import Personas

# Importar la conexión a la base de datos
from models.personas import db  # Asegúrate de que este import esté disponible

render = web.template.render("views/personas", base="../master")

class AgregarPersona:
    def GET(self):
        # Renderiza el formulario para agregar una persona
        return render.agregar_persona()
    
    def POST(self):
        # Obtiene los datos del formulario
        datos = web.input()
        
        try:
            # Validar que los campos requeridos estén presentes
            if not hasattr(datos, 'nombre') or datos.nombre.strip() == '':
                return render.agregar_persona(mensaje_error="El nombre es obligatorio")
            
            # Crear un diccionario con los datos de la persona
            persona_data = {
                "nombre": datos.nombre,
                "telefono": datos.telefono if hasattr(datos, 'telefono') else ""
            }
            
            # Insertar en Firebase (Firebase generará un ID automáticamente)
            db.child("personas").push(persona_data)
            
            # Redirigir a la lista de personas después de agregar
            raise web.seeother('/personas/lista_personas')
        
        except Exception as error:
            print(f"Error al agregar persona: {error}")
            return render.agregar_persona(mensaje_error=f"Error al procesar los datos: {str(error)}")