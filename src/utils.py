import re
import pandas as pd
import numpy as np

import xgboost as xgb
from sklearn.metrics import (
    roc_curve,
    roc_auc_score,
    precision_recall_curve,
    average_precision_score,
)

import matplotlib.pyplot as plt
import seaborn as sns


def import_datasets() -> tuple[pd.DataFrame, pd.DataFrame]:
    """Método para importar os datasets de treino e de teste

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: df_train, df_test
    """
    df_train = pd.read_csv("datasets/train.csv")
    df_test = pd.read_csv("datasets/test.csv")

    print("df_train[linhas, colunas] = {}".format(df_train.shape))
    print(
        "Tammanho df_train = {:.2f} MB".format(df_train.memory_usage().sum() / 1024**2)
    )
    print("df_test[linhas, colunas] = {}".format(df_test.shape))
    print("Tamanho df_test = {:.2f} MB".format(df_test.memory_usage().sum() / 1024**2))

    return df_train, df_test


def limpar_textos(row: str) -> str:
    """Função para limpar os textos, evitando ruidos desnecessários

    Args:
        row (str): String com o conteúdo da coluna

    Returns:
        str: Retorna o texto limpo
    """

    row = str(row).lower()  # evitando duplicação. Ex: 'Casa' | 'casa'
    row = re.sub(r"http\S+", " url ", row)  # url não são necessárias p/ classificar
    row = re.sub(r"@\w+", " user ", row)  # nem menções para usuários
    row = re.sub(r"[^a-z0-9\s#]", " ", row)  # removendo pontuações

    return row


def plotar_matriz_confusao(cm: np.ndarray, implementacao: str) -> None:
    """Função para plotar uma matriz de confusão"""
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Não desastre", "Desastre"],
        yticklabels=["Não desastre", "Desastre"],
    )
    plt.xlabel("Predição")
    plt.ylabel("Real")
    plt.title(f"Matriz de Confusão - {implementacao}")
    plt.show()


def plot_roc(model, X, y, model_name):
    # Detecta se é XGBoost (DMatrix ou booster)
    if isinstance(X, xgb.DMatrix):
        probs = model.predict(X)
    elif hasattr(model, "predict_proba"):
        # Se tiver predict_proba, usa a coluna da classe positiva
        probs = model.predict_proba(X)[:, 1]

    fpr, tpr, thresholds = roc_curve(y, probs)
    auc = roc_auc_score(y, probs)

    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, label=f"AUC = {auc:.3f}")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"Curva ROC - {model_name}")
    plt.legend()
    plt.show()


def plot_precision_recall(model, X, y, model_name):
    # Detecta se é XGBoost (DMatrix ou booster)
    if isinstance(X, xgb.DMatrix):
        probs = model.predict(X)
    elif hasattr(model, "predict_proba"):
        # Se tiver predict_proba, usa a coluna da classe positiva
        probs = model.predict_proba(X)[:, 1]

    precision, recall, thresholds = precision_recall_curve(y, probs)
    ap = average_precision_score(y, probs)

    plt.figure(figsize=(6, 5))
    plt.plot(recall, precision, label=f"AP = {ap:.3f}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(f"Curva Precisão-Revocação - {model_name}")
    plt.legend()
    plt.show()
