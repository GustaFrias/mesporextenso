def mesFormatado(data):
    data = (data.replace("/", " ").split())
    mes = int(data[1])
    meses = ["janeiro", "fevereiro","maio","março","abril","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
    print(f"{data[0]} {meses[mes -1 ]} {data[2]}")
    

mesFormatado("02/06/1995")
