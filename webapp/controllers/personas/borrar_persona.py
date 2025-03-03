import web
from models.personas import Personas

render = web.template.render("views/personas", base="../master")

class BorrarPersona:
    def GET(self, id):
        try:
            persona = Personas()
            datos = persona.obtener_persona(id)
            if datos["status"] == 200:
                return render.borrar_persona(datos["persona"])
            else:
                # Redirigir a lista si no se encuentra la persona
                raise web.seeother('/personas/lista_personas')
        except Exception as error:
            print(f"Error al cargar datos para borrar: {error}")
            raise web.seeother('/personas/lista_personas')
        
    def POST(self, id):
        try:
            persona = Personas()
            resultado = persona.eliminar_persona(id)
            
            # Siempre redirige a la lista después de borrar o intentar borrar
            raise web.seeother('/personas/lista_personas')
        except Exception as error:
            print(f"Error al borrar persona: {error}")
            raise web.seeother('/personas/lista_personas')