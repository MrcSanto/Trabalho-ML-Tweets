# Classificação de Tweets sobre Desastres: Comparação de Abordagens em PLN

Este projeto tem como objetivo treinar e comparar modelos de Processamento de Linguagem Natural (PLN) para classificar tweets relacionados a desastres naturais. Foram testadas diferentes abordagens de vetorização e algoritmos de classificação para avaliar métricas como precisão, recall, F1-score e ROC AUC.

## Gerenciador de pacotes utilizado
O projeto em questão utiliza o gerenciador de pacotes UV.

O UV é uma ferramenta moderna para gerenciamento de pacotes e ambientes virtuais Python, desenvolvida pela Astral. É significativamente mais rápido que o pip tradicional e oferece recursos avançados de gerenciamento de dependências.

Estou utilizando ele, pois posso especificar qual versão do python posso utilizar, no pip eu não consigo fazer isso.

Fora que a velocidade de download dos pacotes é astronomicamente melhor!

### Instalando o UV

- Linux

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

- Windows
  ```bash
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

### Instalando as dependências

```bash
uv sync
```

Após isso, já pode rodar o notebook e visualizar os resultados.


## Documentação

Caso seja preciso consultar a documentação, segue o link: [docs.astral](https://docs.astral.sh/uv/)
 