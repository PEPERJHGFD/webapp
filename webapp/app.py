import web
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas

# Configuración de las rutas
urls = (
    '/', 'Index',  # Página de inicio
    '/personas/lista_personas', 'ListaPersonas',  # Lista de personas
)

# Crear aplicación
app = web.application(urls, globals())

# Ejecutar aplicación
if __name__ == "__main__":
    app.run()