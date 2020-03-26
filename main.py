from domain import Cerc, Cnab

# cerc = Cerc(r"C:\Users\lucas.abreu\Desktop\saida")
# cerc.listFiles()

cnab = Cnab(r"C:\Users\lucas.abreu\Desktop\Nova pasta\arquivo.ret")
cnab.read_cnab()
cnab.count_payment_line()
cnab.write_cnab(10, r"C:\Users\lucas.abreu\Desktop\Nova pasta\teste")