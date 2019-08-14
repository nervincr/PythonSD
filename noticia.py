class Noticia:
    def __init__(self, codigo, ambito, fecha, descripcion):
       self.codigo = codigo
       self.ambito = ambito
       self.fecha = fecha
       self.descripcion = descripcion

    def visualizar(self):
        print('Codigo: {0} | Ambito: {1} | Fecha: {2} | Descripcion: {3}'.format(self.codigo, self.ambito, self.fecha, self.descripcion))
