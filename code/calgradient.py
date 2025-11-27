#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de gradiente (regressão linear simples) usando gradient descent.

Funcionalidades:
- calcula mean squared error (MSE)
- encontra peso (slope) e bias (intercept) por descida do gradiente
- plota custo vs iterações e reta de regressão final

Uso:
  python code/calgradient.py

Autor: adaptado para o Trabalho-de-Calculo
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List


def mean_squared_error(y_true: np.ndarray, y_predicted: np.ndarray) -> float:
    """Calcula MSE entre vetores"""
    return float(np.mean((y_true - y_predicted) ** 2))


def gradient_descent(x: np.ndarray,
                     y: np.ndarray,
                     iterations: int = 1000,
                     learning_rate: float = 0.0001,
                     stopping_threshold: float = 1e-6,
                     verbose: bool = False) -> Tuple[float, float, List[float], List[float]]:
    """
    Executa gradient descent para ajustar uma regressão linear y = w*x + b.

    Retorna (peso, bias, lista_costs, lista_weights)
    """
    # Inicializa parâmetros
    current_weight = 0.0
    current_bias = 0.0
    n = float(len(x))

    costs: List[float] = []
    weights: List[float] = []
    previous_cost: float | None = None

    for i in range(1, iterations + 1):
        # Predição atual
        y_predicted = current_weight * x + current_bias

        # Cálculo do custo
        current_cost = mean_squared_error(y, y_predicted)

        # Guarda histórico
        costs.append(current_cost)
        weights.append(current_weight)

        # Critério de parada
        if previous_cost is not None and abs(previous_cost - current_cost) <= stopping_threshold:
            if verbose:
                print(f"Parou na iteração {i} por critério de parada. Mudança do custo: {abs(previous_cost - current_cost)}")
            break
        previous_cost = current_cost

        # Derivadas (gradientes)
        weight_derivative = (-2.0 / n) * np.sum(x * (y - y_predicted))
        bias_derivative = (-2.0 / n) * np.sum(y - y_predicted)

        # Atualiza parâmetros
        current_weight = current_weight - (learning_rate * weight_derivative)
        current_bias = current_bias - (learning_rate * bias_derivative)

        # Logs ocasionais
        if verbose and (i % 100 == 0 or i == 1):
            print(f"Iter {i}: cost={current_cost:.6f}, weight={current_weight:.6f}, bias={current_bias:.6f}")

    return current_weight, current_bias, costs, weights


def main() -> None:
    # Dados (vetores fornecidos no enunciado)
    X = np.array([
        32.5, 53.4, 61.5, 47.4, 59.8,
        55.1, 52.2, 39.2, 48.1, 52.5,
        45.4, 54.3, 44.1, 58.1, 56.7,
        48.9, 44.6, 60.2, 45.6, 38.8
    ], dtype=float)

    Y = np.array([
        31.7, 68.7, 62.5, 71.5, 87.2,
        78.2, 79.6, 59.1, 75.3, 71.3,
        55.1, 82.4, 62.0, 75.3, 81.4,
        60.7, 82.8, 97.3, 48.8, 56.8
    ], dtype=float)

    # Hiperparâmetros
    iterations = 2000
    learning_rate = 0.0001
    stopping_threshold = 1e-6

    w, b, costs, weights = gradient_descent(X, Y, iterations=iterations, learning_rate=learning_rate, stopping_threshold=stopping_threshold, verbose=True)

    print(f"\nEstimated Weight: {w:.6f}\nEstimated Bias: {b:.6f}")

    # Predições finais
    Y_pred = w * X + b

    # Plot: custo vs iterações
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(costs) + 1), costs, label='Cost')
    plt.title('Cost (MSE) por iteração')
    plt.xlabel('Iteração')
    plt.ylabel('Custo (MSE)')
    plt.grid(True)
    plt.legend()
    plt.show()

    # Plot: dados e reta de regressão
    plt.figure(figsize=(8, 6))
    plt.scatter(X, Y, marker='o', color='red', label='Dados')
    xs = np.linspace(np.min(X) - 1, np.max(X) + 1, 100)
    plt.plot(xs, w * xs + b, color='blue', label='Regressão')
    plt.title('Regressão Linear por Gradient Descent')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()