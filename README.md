# Projeto de manipulação de arquivos posicionais

* ## **CERC - CERC-A001T006-02**

    * Métodos: 
        1. listFiles()
        2. search_line_type(type_reg: str)
        3. search_cod_reg(type_reg: str)
        4. search_line_by_ec(cpf_cnpj: str)

* ## **CNAB 240 - Itaú**
    
    * Métodos: 
        1. write_cnab(file_qty: int, path: str)
        2. count_payment_line()

## Detalhes:

### CERC

**listFiles()**: Lista todos os arquivos do diretório do tipo A001T006. 
    
**search_line_type(type_reg: str)**: Seleciona todas as linha do tipo selecionado.

**search_cod_reg(type_reg: str)**: Seleciona o identificador uníco do registro por tipo.

**search_line_by_ec(cpf_cnpj: str)**: Seleciona linha por cpf/cnpj do EC


### CNAB

**write_cnab(file_qty: int, path: str)**: Defino a quantidade de aquivos que serão reescritos e o path, onde os arquivos serão escritos.

**count_payment_line()**: Quantidade total de pagamento no arquivo.

### Exemplo
>
    Cerc
        cerc = Cerc(r"C:\Users\lucas.abreu\Desktop\saida") # diretório dos arquivos de saída
        cerc.listFiles()
        cerc.search_line_type("3") # 1- regitro, 2- manutenção e 3- baixa
        cerc.search_line_type("3")
        search_line_by_ec("00006559970086")


> 
    CNAB
        cnab = Cnab(r"C:\Users\lucas.abreu\Desktop\Nova pasta\arquivo.ret") # diretório do arquivo de retorno
        cnab.count_payment_line()
        cnab.write_cnab(10, r"C:\Users\lucas.abreu\Desktop\Nova pasta\teste") # Número de arquivos e path destino

        # retorno:
    
        # O Arquivo possui 0 linha(s) de pagamento.
        # Arquivo original: 1245 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v0.ret gerado com 125 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v1.ret gerado com 125 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v2.ret gerado com 125 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v3.ret gerado com 125 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v4.ret gerado com 125 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v5.ret gerado com 124 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v6.ret gerado com 124 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v7.ret gerado com 124 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v8.ret gerado com 124 pagamento(s)
        # Arquivo: C:\Users\lucas.abreu\Desktop\Nova pasta\teste\v9.ret gerado com 124 pagamento(s)
        # Arquivos gerados com sucesso!
