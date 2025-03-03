import web
from models.personas import Personas

render = web.template.render("views/personas", base="../master")

class DetallePersona:
    def GET(self, id):
        try:
            persona = Personas()
            datos = persona.obtener_persona(id)
            if datos["status"] == 200:
                return render.detalle_persona(datos["persona"])
            else:
                # Redirigir a lista si no se encuentra la persona
                raise web.seeother('/personas/lista_personas')
        except Exception as error:
            print(f"Error al cargar detalles de persona: {error}")
            raise web.seeother('/personas/lista_personas')