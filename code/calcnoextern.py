#Igual o arquivo calc.py, mas sem dependências externas
# Criar uma calculadora de derivadas parciais em python
# 1 - Interface de usuário simples
# 2 - Entrada de função multivariável
# 3 - Cálculo de derivadas parciais
# 4 - Exibição dos resultados

def calcular_derivada_parcial(funcao: str, variavel: str):
    # Normaliza potência escrita com ^ para ** (ex: x^2 -> x**2)
    funcao = funcao.replace('^', '**')

    # Verifica se a variável está na função
    if variavel not in funcao:
        raise ValueError(f"A variável '{variavel}' não está presente na função.")

    # Implementação simples de derivada parcial para polinômios
    termos = funcao.replace('-', '+-').split('+')
    derivada_termos = []

    for termo in termos:
        termo = termo.strip()
        if variavel in termo:
            partes = termo.split(variavel)
            coeficiente = partes[0]
            expoente = 1

            if len(partes) > 1 and partes[1].startswith('**'):
                expoente_partes = partes[1].split('**')
                if len(expoente_partes) > 1:
                    try:
                        expoente = int(expoente_partes[1])
                    except ValueError:
                        raise ValueError(f"Expoente inválido em '{termo}'.")

            if expoente == 1:
                derivada_termos.append(coeficiente if coeficiente not in ('', '+', '-') else coeficiente + '1')
            else:
                novo_coeficiente = f"{coeficiente}*{expoente}" if coeficiente not in ('', '+', '-') else f"{expoente}"
                novo_expoente = expoente - 1
                if novo_expoente == 1:
                    derivada_termos.append(novo_coeficiente + variavel)
                elif novo_expoente > 1:
                    derivada_termos.append(novo_coeficiente + variavel + f"**{novo_expoente}")

    if not derivada_termos:
        return "0"

    return ' + '.join(derivada_termos).replace('+-', '- ')

# Interface de usuário simples
def inicializar_calculadora():
    print("Calculadora de Derivadas Parciais (sem dependências externas)")
    funcao = input("Digite uma função multivariável (ex: x**2 + y**2 ou x^2 + y^2): ").strip()
    variavel = input("Digite a variável em relação à qual deseja derivar (ex: x ou y): ").strip()

    if not funcao or not variavel:
        print("Função ou variável não informada. Saindo.")
        return

    try:
        resultado = calcular_derivada_parcial(funcao, variavel)
        print("Calculando a derivada parcial de", funcao, "em relação a", variavel)
        print("Resultado:", resultado)
    except Exception as e:
        print("Erro:", e)