import web
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas
from controllers.personas.agregar_persona import AgregarPersona as AgregarPersona
from controllers.personas.detalle_persona import DetallePersona as DetallePersona
from controllers.personas.editar_persona import EditarPersona as EditarPersona
from controllers.personas.borrar_persona import BorrarPersona as BorrarPersona

# Configuración de las rutas
urls = (
    '/', 'Index',  # Página de inicio
    '/personas/lista_personas', 'ListaPersonas',
    '/personas/agregar_persona', 'AgregarPersona',
    '/personas/detalle_persona/(.*)', 'DetallePersona',  # El (.*) captura cualquier valor después
    '/personas/editar_persona/(.*)', 'EditarPersona',
    '/personas/borrar_persona/(.*)', 'BorrarPersona',
        )
app = web.application(urls, globals())

# Ejecutar aplicación
if __name__ == "__main__":
    app.run()