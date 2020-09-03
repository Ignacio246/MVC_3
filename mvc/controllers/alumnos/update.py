import web
import mvc.models.model as alumnos

model_alumnos = alumnos.Alumnos()

render = web.template.render("mvc/views/alumnos/", base="template")

class Update():
    
    def GET(self,matricula):
        try:
            result = model_alumnos.view(matricula)[0]
            #print(result)
            return render.update(result) 
        except Exception as e:
            return "Error " + str(e.args)

    def POST(self, matricula):
        try:
            form = web.input()
            matricula = form.matricula
            nombre = form.nombre
            apellido_paterno = form.apellido_paterno
            apellido_materno = form.apellido_materno
            edad = form.edad
            fecha_nacimiento = form.fecha_nacimiento
            sexo = form.sexo
            estado_civil = form.estado_civil
            result = model_alumnos.update(matricula,nombre,apellido_paterno,apellido_materno,edad,fecha_nacimiento,sexo,estado_civil)
            web.seeother('/list')
        except Exception as e:
            return "Error " + str(e.args)