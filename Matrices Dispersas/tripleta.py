class Tripleta():
    """Método constructor"""
    def __init__(self, fila, col, value):
        self.fila = fila
        self.col = col
        self.value = value

    """Métodos getters & setters"""
    def set_fila(self, fila):
        self.fila = fila

    def set_col(self, col):
        self.col = col

    def set_value(self, value):
        self.value = value

    def get_fila(self):
        return self.fila

    def get_col(self):
        return self.col

    def get_value(self):
        return self.value
