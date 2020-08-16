import web 
import page.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render=web.template.render('page/views/alumnos/')

class Update():
    def GET(self, matricula):
      try:
        result=model_alumnos.view(matricula)[0]
        return render.update(result)
      except Exception as e:
        return "--E-R-R-0-R--" + str(e.args)

    def POST(self, matricula):
      try:
        form = web.input()
        matricula = form.matricula
        nombre = form.nombre
        papellido = form.papellido
        sapellido = form.sapellido
        edad = form.edad
        naci = form.naci
        genero = form.genero
        estado = form.estado
        model_alumnos.update(matricula,nombre,papellido,sapellido,edad,naci,genero,estado)
        web.seeother('/list')
      except Exception as e:
        print(e)
        return "--E-R-R-0-R--" + str(e.args)
