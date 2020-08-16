import mysql.connector

class Alumnos():

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(
                user='k0oqq4wnak2ve97u', 
                password='ry80zgqiyde9wsml',
                host='s3lkt7lynu0uthj8.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                port=3306,
                database='ts87c0j2pv9bv8sh'
                )
            self.cursor = self.cnx.cursor()
        except Exception as e:
            print(e)

    def select(self):
        try:
            self.connect()
            query = ("SELECT * from alumnos;")
            self.cursor.execute(query)
            result = []
            for row in self.cursor:
                r = {
                    'id_alumno':row[0],
                    'matricula':row[1],
                    'nombre':row[2],
                    'papellido':row[3],
                    'sapellido':row[4],
                    'edad':row[5],
                    'naci':row[6],
                    'genero':row[7],
                    'estado':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)
            result = []
            return result

    def view(self, matricula):
        try:
            self.connect()
            query = ("SELECT * FROM alumnos where matricula = %s;")
            values = (matricula,)
            self.cursor.execute(query,values)
            result = []
            for row in self.cursor:
                r = {
                    'id_alumno':row[0],
                    'matricula':row[1],
                    'nombre':row[2],
                    'papellido':row[3],
                    'sapellido':row[4],
                    'edad':row[5],
                    'naci':row[6],
                    'genero':row[7],
                    'estado':row[8]
                }
                result.append(r)
            self.cursor.close()
            self.cnx.close()
            return result
        except Exception as e:
            print(e)

    def insert(self, matricula, nombre, papellido, sapellido, edad, naci, genero, estado):
        try:
            self.connect()
            query = ("INSERT INTO alumnos (matricula, nombre, papellido, sapellido, edad, naci, genero, estado) values(%s,%s,%s,%s,%s,%s,%s,%s);")
            values = (matricula, nombre, papellido, sapellido, edad, naci, genero, estado)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def update(self, matricula, nombre, papellido, sapellido, edad, naci, genero, estado):
        try:
            self.connect()
            query = ("UPDATE alumnos SET nombre=%s, papellido=%s,sapellido=%s,edad=%s,naci=%s,genero=%s,estado=%s WHERE matricula=%s;")
            values = (nombre, papellido, sapellido, edad, naci, genero, estado, matricula)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, matricula):
        try:
            self.connect()
            query = ("DELETE FROM alumnos WHERE matricula= %s;")
            values = (matricula,)
            self.cursor.execute(query, values)
            self.cnx.commit()
            self.cursor.close()
            self.cnx.close()
            return True
        except Exception as e:
            print(e)
            return False

objeto = Alumnos()

for row in objeto.select():
    print(row)
