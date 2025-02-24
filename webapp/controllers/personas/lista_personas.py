import web
from models.personas import Personas

render = web.template.render("views/personas", base="../master")

class ListaPersonas:
    def GET(self):
        try:
            persona = Personas()
            datos_personas = persona.lista_personas()
            if datos_personas["status"] == 200:
                return render.lista_personas(datos_personas["personas"])
            else:
                return render.lista_personas([])
        except Exception as error:
            print(f"Error al cargar la lista de personas: {error}")
            return render.lista_personas([])