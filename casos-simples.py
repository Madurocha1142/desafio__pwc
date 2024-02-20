import re

def processar_endereco(endereco):
    padrao = re.compile(r'([^\d]+)\s?([\d\s\w,]+)')
    match = padrao.match(endereco)
    
    if match:
        rua = match.group(1).strip()
        numero = match.group(2).strip()
        return rua, numero
    else:
        return None, None

def executar_testes():
    test_cases = [
        "Miritiba 339",
        "Babaçu 500",
        "Cambuí 804B"
    ]

    for endereco in test_cases:
        rua, numero = processar_endereco(endereco)
        print(f"{endereco} -> Rua: {rua}, Número: {numero}")

# Chamando a função de teste diretamente
executar_testes()