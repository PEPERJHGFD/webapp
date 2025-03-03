import web
from models.personas import Personas

render = web.template.render("views/personas", base="../master")

class EditarPersona:
    def GET(self, id):
        try:
            persona = Personas()
            datos = persona.obtener_persona(id)
            if datos["status"] == 200:
                return render.editar_persona(datos["persona"])
            else:
                # Redirigir a lista si no se encuentra la persona
                raise web.seeother('/personas/lista_personas')
        except Exception as error:
            print(f"Error al cargar datos para editar: {error}")
            raise web.seeother('/personas/lista_personas')
        
    def POST(self, id):
        try:
            datos = web.input()
            persona = Personas()
            resultado = persona.actualizar_persona(id, datos)
            
            if resultado["status"] == 200:
                # Redirige a la lista después de actualizar
                raise web.seeother('/personas/lista_personas')
            else:
                # Si hubo error, muestra el formulario con error
                return render.editar_persona(datos, mensaje_error=resultado["mensaje"])
        except Exception as error:
            print(f"Error al actualizar persona: {error}")
            return render.editar_persona(datos, mensaje_error="Error al procesar los datos")