"""Mock table access for local analytics demos."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_trades(path: str | Path = "data/sample/trades.csv") -> pd.DataFrame:
    return pd.read_csv(path)
