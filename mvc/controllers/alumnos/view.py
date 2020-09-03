import web
import mvc.models.model as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class View():

    def GET(self,matricula):
        try:
            result = model_alumnos.view(matricula)[0]
            return render.view(result) 
        except Exception as e:
            return "Error " + str(e.args)