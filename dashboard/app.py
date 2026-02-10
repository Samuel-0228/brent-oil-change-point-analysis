import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
gfrom pathlib import Path

app = dash.Dash(__name__)

# Resolve paths relative to the repository root (two levels up from this file)
BASE_DIR = Path(__file__).resolve().parent.parent
df_path = BASE_DIR / "data" / "processed" / "brent_2012_2022.csv"
events_path = BASE_DIR / "data" / "external" / "events.csv"

df = pd.read_csv(df_path, parse_dates=["Date"])
events = pd.read_csv(events_path, parse_dates=["Date"])

fig = go.Figure()
fig.add_trace(go.Scatter(x=df["Date"], y=df["price"],
              mode="lines", name="Brent Price"))

for _, row in events.iterrows():
    fig.add_vline(x=row["Date"], line_dash="dot", line_color="red")
    fig.add_annotation(x=row["Date"], y=df["price"].max()*0.9,
                       text=row["Event_Description"][:20], showarrow=True)

fig.update_layout(title="Brent Oil Prices & Key Events",
                  xaxis_title="Date", yaxis_title="USD/barrel")

app.layout = html.Div([
    html.H1("Brent Oil Change Point Dashboard"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
