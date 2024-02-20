import re

def processar_endereco(endereco):
    padrao = re.compile(r'(?:(\d+),?\s)?(.+)')
    match = padrao.match(endereco)
    
    if match:
        numero = match.group(1).strip() if match.group(1) else None
        rua = match.group(2).strip()
        return rua, numero
    else:
        return None, None

def executar_testes():
    test_cases = [
        "4, Rue de la République",
        "100 Broadway Av",
        "Calle Sagasta, 26",
        "Calle 44 No 1991"
    ]

    for endereco in test_cases:
        rua, numero = processar_endereco(endereco)
        print(f"{endereco} -> Rua: {rua}, Número: {numero}")

# Chamando a função de teste diretamente
executar_testes()