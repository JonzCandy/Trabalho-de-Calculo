# Criar uma calculadora de derivadas parciais em python
# 1 - Interface de usuário simples
# 2 - Entrada de função multivariável
# 3 - Cálculo de derivadas parciais
# 4 - Exibição dos resultados

# Calculadora de derivadas parciais (simples) usando SymPy
import sympy as sp

def calcular_derivada_parcial(funcao: str, variavel: str):
    # Normaliza potência escrita com ^ para ** (ex: x^2 -> x**2)
    funcao = funcao.replace('^', '**')

    # Cria símbolo para a variável solicitada (ex: 'x' ou 'y' ou 'z')
    var_sym = sp.symbols(variavel)

    # Passa o símbolo nas locals para sympify — evita ambiguidade
    try:
        expr = sp.sympify(funcao, locals={variavel: var_sym})
    except Exception as e:
        raise ValueError(f"Erro ao interpretar a função: {e}")

    try:
        derivada = sp.diff(expr, var_sym)
    except Exception as e:
        raise ValueError(f"Erro ao derivar em relação a '{variavel}': {e}")

    return derivada

# Interface de usuário simples
def inicializar_calculadora():
    print("Calculadora de Derivadas Parciais")
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

if __name__ == "__main__":
    inicializar_calculadora()