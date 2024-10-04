# usar o split() para dividir a data inserida, depois utilizar o replace() apenas na substring mes
data = input("digite respectivamente: dia, mês, ano.")
lista=[]
meses = ["janeiro", "fevereiro", "março","abril","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
def mesFormatado(data):
    
    tbpespaco = data.replace("/"," ")
    print(tbpespaco)
    listateste = tbpespaco.split()
    print(listateste)
    lista.append(listateste)
    mes = int(data[1])
    print(f"")
print(mesFormatado(data))

