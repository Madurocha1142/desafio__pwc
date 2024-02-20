# vamos importar uma lib do python para lidar com regex, que é o re
import re

# vamos manter a função que recebe o endereço
def processar_endereco(endereco):

    padrao = re.compile(r'(\D+)(\d+.*)')

    # No match vamos guardar se a nossa string segue esse padrão, nesse caso uma variável booleana
    match = padrao.match(endereco)
    
    # Caso seja uma string que segue esse modelo
    if match:
        
        rua = match.group(1).strip()
        # Removemos a vírgula no final do nome da rua, se houver
        rua = rua.rstrip(',')
        
        numero = match.group(2).strip()
        # Retorna a rua e o numero separadamente
        return rua, numero
    # Aqui é caso a condição não dê certo, ou seja, não tenha match
    else:
        return None, None

def main():
    # Recebe a rua e o número
    endereco = input("Digite o endereço: ")
    # Armazena a rua e o numero com os valores retornados da função
    rua, numero = processar_endereco(endereco)
    
    # Se existir um endereço, retorna
    if rua and numero:
        print(f"Rua: {rua}\nNúmero: {numero}")
    # Se não, endereço inválido
    else:
        print("Endereço inválido.")

main()