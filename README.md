# 🧮 Calculadora com Tkinter (Python)

Este é um projeto simples de calculadora desenvolvido em Python utilizando a biblioteca Tkinter para interface gráfica.

## 🚀 Funcionalidades

- Interface gráfica com botões interativos
- Entrada de números e operadores matemáticos
- Atualização dinâmica do display
- Cálculo de expressões matemáticas
- Botão de limpar (`C`) para resetar a operação

## 🧠 Como funciona

A lógica da calculadora é baseada em dois elementos principais:

- `num_entry_value`: armazena a expressão matemática como string
- `StringVar()`: faz a ligação entre o valor da expressão e o display

Quando um botão é clicado:
1. O valor é adicionado à string (`num_entry_value`)
2. O display é atualizado automaticamente com `StringVar`

Ao clicar em `=`:
- A expressão é avaliada usando `eval()`
- O resultado substitui a expressão atual
- O display é atualizado com o resultado

## ⚠️ Observações

- O uso de `eval()` facilita a implementação, mas não é recomendado para aplicações reais por questões de segurança.
- O projeto ainda pode ser melhorado com:
  - tratamento de erros mais robusto
  - organização em classes (orientação a objetos)
  - suporte a mais operações

## 🛠️ Tecnologias utilizadas

- Python
- Tkinter
