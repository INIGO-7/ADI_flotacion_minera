from typing import Dict, List, Tuple

import pandas as pd
import numpy as np
import plotly.express as px

def custom_boxplot(
    df: pd.DataFrame,
    variable_x: str, 
    variable_y: str,
    title: str,
    subtitle: str = "",
    range: List[int] | None = None,
):
    
    fig = px.box(df, x=variable_x, y=variable_y, template="plotly_white")
    fig.update_layout(
        title={
            "text": title + f"<br><sup>{subtitle}</sup>",
            "xanchor": "center",
            "yanchor": "top",
            "y": 0.955,
            "x": 0.5
        }
    )
    fig.update_yaxes(range=range)
    fig.show()