from gen.generic import Generic


class Car:
    id: int
    marca: str
    modelo: str
    cor: str
    ano_fabricacao: int
    ano_modelo: int
    combustivel: str
    potencia: int
    portas: int
    lugares: int
    fipe_codigo: str
    data_criacao: int
    data_alteracao: int

    def __init__(self, marca: str, modelo: str):
        self.id = 0
        self.marca = marca
        self.modelo = modelo
        self.cor = ''
        self.ano_fabricacao = 0
        self.ano_modelo = 0
        self.combustivel = ''
        self.potencia = 0
        self.portas = 0
        self.lugares = 0
        self.fipe_codigo = ''
        self.data_criacao = Generic.get_current_date()
        self.data_alteracao = 0

    def __str__(self):
        return f'id {self.id} : marca {self.marca} : modelo {self.modelo}'

    def load_from_tuple(self, line: tuple):
        self.id = line[0]
        self.marca = line[1]
        self.modelo = line[2]
        self.cor = line[3]
        self.ano_fabricacao = line[4]
        self.ano_modelo = line[5]
        self.combustivel = line[6]
        self.potencia = line[7]
        self.portas = line[8]
        self.lugares = line[9]
        self.fipe_codigo = line[10]
        self.data_criacao = line[11]
        self.data_alteracao = line[12]

    # def set(self, id: int = None):
    #     if id is not None:
    #         self.id = id
