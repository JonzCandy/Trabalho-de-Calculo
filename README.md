# Equipe

- João Miguel Cândido Anastácio Costa
- Raphael Matos

## Como executar os scripts

Pré-requisitos gerais:

- Python 3.8+ instalado
- `pip` para instalar pacotes opcionais

Observação sobre PowerShell (Windows): execute os comandos abaixo no `powershell.exe`.

### `code/calc.py` (usa SymPy)

- O que faz: recebe uma expressão simbólica (ex: `x**2 + y**2`) e calcula a derivada parcial em relação à variável informada, usando SymPy.

- Instalação (se necessário):

```powershell
pip install sympy
```

- Execução:

```powershell
python .\code\calc.py
```

- Dica: escreva potência com `**` ou use `^` (algumas versões do script convertem `^` para `**`). Exemplo de entrada: `x**2 + 3*x*y`, variável `x` → saída `2*x + 3*y`.

### `code/calcnoextern.py` (sem dependências externas)

- O que faz: versão simples que calcula derivadas parciais apenas para polinômios escritos como string (sem usar bibliotecas externas).

- Execução:

```powershell
python .\code\calcnoextern.py
```

- Limitações: suporta principalmente termos polinomiais do tipo `a*x**n` ou `a*x^n`. Não lida corretamente com funções trigonométricas, exponenciais, parênteses complexos ou expressões muito gerais.

### `code/calgradient.py` (regressão linear por Gradient Descent)

- O que faz: ajusta uma reta `y = w*x + b` usando descida do gradiente, mostra o custo (MSE) por iteração e plota a reta final sobre os dados.

- Instalação (se necessário):

```powershell
pip install numpy matplotlib
```

- Execução:

```powershell
python .\code\calgradient.py
```

## Relação entre os scripts e derivadas parciais / backpropagation

- `calc.py` e `calcnoextern.py` calculam derivadas parciais de uma função — conceito central para entender o gradiente.

- `calgradient.py` mostra na prática como usamos derivadas parciais da função de perda (MSE) em relação aos parâmetros (`w`, `b`) para atualizar esses parâmetros via Gradient Descent (w_novo = w_antigo − η * ∂L/∂w).

- Em redes neurais, backpropagation usa a mesma ideia: calcular ∂L/∂w para todos os pesos (usando a regra da cadeia) e aplicar um otimizador (p.ex. Gradient Descent, SGD, Adam) para reduzir a perda.

## Exemplos rápidos de uso

- Exemplo `calgradient.py`: os hiperparâmetros padrão estão no `main()`; rode o script e observe os logs e gráficos.

- Exemplo `calc.py`: inserir `x**2 + y**2` e escolher variável `x` retorna `2*x`.

- Exemplo `calcnoextern.py`: inserir `3*x**3 + 2*x**2 + x` e escolher variável `x` retorna `9*x**2 + 4*x + 1`.
