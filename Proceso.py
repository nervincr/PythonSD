class Proceso:
    def __init__(self, id, tTotal, tCompletado, estado):
       self.id = id
       self.tTotal = tTotal
       self.tCompletado = tCompletado
       self.estado = estado

    def ejecutar(self):
        print('Proceso: {0}, Estado: {1}'.format(self.id, self.estado))
        self.estado = "Ejecutando"
        for x in range(0, self.tTotal):
            self.tCompletado += 1
            print('Proceso: {0}, Estado: {1}, Completado: {2}'.format(self.id, self.estado, self.tCompletado))
            time.sleep(1)
        self.estado = "Finalizado"
        print('Proceso: {0}, Estado: {1}'.format(self.id, self.estado))