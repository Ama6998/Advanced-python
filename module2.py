import pandas as pd

def clean_columns(df):
    df.columns = (
        df.columns
        .str.replace('_', '')
        .str.lower()
        .str.strip()
    )
    return df

def missing_summary(df):
    total = df.isna().sum()
    pct = (total / len(df) * 100).round(2)

    out = pd.DataFrame({
        "missing_cnt": total,
        "missing_pct": pct
    }).sort_values(["missing_cnt", "missing_pct"], ascending=False)

    return out

def preview(df, n=5):
    return df.head(n)
