# Projeto de Cálculo do IMC

Aplicação desenvolvida por **Daniel Camilo da Silva** como atividade prática da disciplina de **Linguagem de Programação** no curso **Tecnólogo em DevOps** do **Centro Universitário Anhanguera Pitágoras Ampli**.

## Sobre o Projeto

Este projeto tem como objetivo calcular o **Índice de Massa Corpórea (IMC)**, classificar os resultados de acordo com tabelas padrão, e promover o aprendizado em lógica de programação utilizando Python.

## Classificação do IMC
A aplicação utiliza a seguinte tabela de classificação baseada no IMC:

| IMC                | Classificação          |
|--------------------|------------------------|
| Menor que 18.5    | Magreza                |
| 18.5 a 24.9       | Normal                 |
| 25.0 a 29.9       | Sobrepeso             |
| 30.0 a 34.9       | Obesidade Grau I      |
| 35.0 a 39.9       | Obesidade Grau II     |
| 40.0 ou mais      | Obesidade Grau III    |

## Funcionalidades

- Solicita ao usuário:
  - Peso (em kg)
  - Altura (em metros)
- Calcula o IMC com base na fórmula:
  ```text
  IMC = peso / (altura ** 2)
