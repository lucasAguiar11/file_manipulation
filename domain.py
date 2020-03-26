import glob
import numpy


class Cerc:
    def __init__(self, path: str):
        self.path = path
        self.arquivos = []

    def __read_directory(self):
        self.arquivos = glob.glob(rf"{self.path}/*.dom")

    @staticmethod
    def __read_file(arquivo_path: str, type: str):
        with open(arquivo_path, "r") as arquivo:
            for line in arquivo:
                print(line.strip()) if line[1:2] == type else None

    @staticmethod
    def __read_file_reg_code(arquivo_path: str, type_reg: str):
        register_code = set()
        with open(arquivo_path, "r") as arquivo:
            for line in arquivo:
                line_strip = line.strip()
                register_code.add(line_strip[91:108]) if line_strip[1:2] == type_reg else None
            for code in register_code:
                print(code)

    @staticmethod
    def __read_file_cpf_cnpj(arquivo_path, cpf_cnpj):
        with open(arquivo_path, "r") as arquivo:
            for line in arquivo:
                line_strip = line.strip()
                print(line_strip) if line_strip[3:17] == cpf_cnpj else None

    def listFiles(self):
        self.__read_directory()
        for file in self.arquivos:
            print(file)

    def search_line_type(self, type_reg):
        self.__read_directory()
        for arquivo_path in self.arquivos:
            self.__read_file(arquivo_path, type_reg)

    def search_cod_reg(self, type_reg):
        self.__read_directory()
        for arquivo_path in self.arquivos:
            self.__read_file_reg_code(arquivo_path, type_reg)

    def search_line_by_ec(self, cpf_cnpj):
        self.__read_directory()
        for arquivo_path in self.arquivos:
            self.__read_file_cpf_cnpj(arquivo_path, cpf_cnpj)


class Cnab:
    def __init__(self, path: str):
        self.path = path
        self.header = []
        self.trailer = []
        self.detail = []

    def read_cnab(self):
        _header = set()
        _trailer = set()
        _detail = []
        with open(self.path, "r") as file:
            for line in file:
                line = line.rstrip("\n\r")
                typefile = line[7:8]

                _header.add(line) if typefile == "0" or typefile == "1" and len(_header) < 2 else None
                _trailer.add(line) if typefile == "9" else None
                _trailer.add(line) if typefile == "5" and len(_trailer) < 1 else None
                _detail.append(line) if typefile == "3" else None

        self.header = _header
        self.trailer = _trailer
        self.detail = _detail

    def count_payment_line(self):
        print(f"O Arquivo possui {len(self.detail)} linha(s) de pagamento.")

    def write_cnab(self, file_qty: int, path: str):

        lots = numpy.array_split(numpy.array(self.detail), file_qty)
        print(f"Arquivo original: {len(self.detail)} pagamento(s)")
        i = 0
        for lot in lots:

            if len(lot) <= 0:
                continue

            filename = r"{}\v{}.ret".format(path, i)
            open(filename, 'w').close()

            for h in self.header:
                with open(filename, "a") as file:
                    file.write(h)
                    file.write("\n")

            for lines in lot:
                with open(filename, "a") as file:
                    file.write(lines)
                    file.write("\n")

            for t in self.trailer:
                with open(filename, "a") as file:
                    file.write(t)
                    file.write("\n")

            print(f"Arquivo: {filename} gerado com {len(lot)} pagamento(s)")
            i += 1

        print("Arquivos gerados com sucesso!")

