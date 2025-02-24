import web

render = web.template.render("views", base="master")

class Index:
    def GET(self):
        try:
            return render.index()
        except Exception as error:
            print(f"Error en Index.GET: {error}")
            return "Error al cargar la página de inicio."