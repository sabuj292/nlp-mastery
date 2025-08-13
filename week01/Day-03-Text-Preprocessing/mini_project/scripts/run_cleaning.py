# scripts/run_cleaning.py
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



import argparse, os, pandas as pd
from src.cleaning import clean_text_basic, clean_text_advanced

def main():
    ap = argparse.ArgumentParser(description="Clean a CSV that has a 'text' column.")
    ap.add_argument("--input_csv", required=True, help="Path to input CSV (must contain a 'text' column)")
    ap.add_argument("--out_csv", default="outputs/cleaned.csv", help="Where to save the cleaned CSV")
    ap.add_argument("--mode", choices=["basic", "advanced"], default="advanced", help="Which cleaner to use")
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out_csv), exist_ok=True)

    df = pd.read_csv(args.input_csv)
    if "text" not in df.columns:
        raise ValueError("Input CSV must contain a 'text' column.")

    cleaner = clean_text_advanced if args.mode == "advanced" else clean_text_basic
    df["clean_text"] = df["text"].astype(str).apply(cleaner)
    df.to_csv(args.out_csv, index=False, encoding="utf-8")
    print(f"Saved {args.out_csv} with {len(df)} rows.")

if __name__ == "__main__":
    main()
