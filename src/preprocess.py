import pandas as pd
import numpy as np


def process(path, target="UTS (MPa)"):
    df = pd.read_csv(path, encoding="latin1")
    df.columns = df.columns.str.strip()

    if "S (Max)" in df.columns and "S(Max)" not in df.columns:
        df = df.rename(columns={"S (Max)": "S(Max)"})

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .replace({"-": np.nan, "": np.nan, "nan": np.nan, "NaN": np.nan})
            )

    numeric_cols = [
        "UTS (MPa)",
        "UTS (Ksi)",
        "YS (MPa)",
        "YS (ksi)",
        "Elongation (%)",
        "Reduction (%)",
        "Hardness (HB)",
        "C (Min)",
        "C (Max)",
        "Mn (Min)",
        "Mn (Max)",
        "P (Min)",
        "P (Max)",
        "S (Min)",
        "S(Max)",
        "Si (Min)",
        "Si (Max)",
        "Ni (Min)",
        "Ni (Max)",
        "Cr (Min)",
        "Cr (Max)",
        "Mo (Min)",
        "Mo (Max)",
        "Ti (Min)",
        "Ti (Max)",
        "N",
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=[target]).copy()

    feature_cols = [
        "SAE Grade",
        "Conditions",
        "C (Min)",
        "C (Max)",
        "Mn (Min)",
        "Mn (Max)",
        "P (Min)",
        "P (Max)",
        "S (Min)",
        "S(Max)",
        "Si (Min)",
        "Si (Max)",
        "Ni (Min)",
        "Ni (Max)",
        "Cr (Min)",
        "Cr (Max)",
        "Mo (Min)",
        "Mo (Max)",
        "Ti (Min)",
        "Ti (Max)",
        "N",
    ]

    feature_cols = [col for col in feature_cols if col in df.columns]

    X = df[feature_cols].copy()
    y = df[target].copy()

    # tamamen boş kolonları direkt sil
    X = X.dropna(axis=1, how="all")

    numeric_feature_cols = X.select_dtypes(include=["number"]).columns
    categorical_feature_cols = X.select_dtypes(exclude=["number"]).columns

    for col in numeric_feature_cols:
        if X[col].notna().sum() == 0:
            X = X.drop(columns=[col])
        else:
            X[col] = X[col].fillna(X[col].median())

    for col in categorical_feature_cols:
        if X[col].notna().sum() == 0:
            X = X.drop(columns=[col])
        else:
            X[col] = X[col].fillna(X[col].mode().iloc[0])

    X = pd.get_dummies(X, columns=list(X.select_dtypes(exclude=["number"]).columns), drop_first=True)

    # son güvenlik ağı
    X = X.fillna(0)

    return X, y