import json
import plotly.graph_objects as go

bullying_types = ["Rumors", "Name-calling", "Physical", "Exclusion", "Cyberbullying"]
percentages = [13.0, 11.9, 6.0, 4.9, 21.6]
colors = ["#6fa8dc", "#f6b26b", "#e06666", "#93c47d", "#8e7cc3"]
x = list(range(len(bullying_types)))

def export_graph_data():
    data = []
    for i, (bt, pct, color) in enumerate(zip(bullying_types, percentages, colors)):
        data.append({
            "type": "scatter3d",
            "mode": "lines+markers",
            "x": [i, i],
            "y": [0, 0],
            "z": [0, pct],
            "marker": {"size": 8, "color": color},
            "line": {"color": color, "width": 15},
            "name": f"{bt}: {pct}%"
        })
    with open("graph_data.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    export_graph_data()

fig = go.Figure()
for i, (bt, pct, color) in enumerate(zip(bullying_types, percentages, colors)):
    fig.add_trace(go.Scatter3d(
        x=[x[i], x[i]],
        y=[0, 0],
        z=[0, pct],
        mode='lines+markers',
        marker=dict(size=8, color=color),
        line=dict(color=color, width=15),
        name=f'{bt}: {pct}%',
        hovertemplate=f'{bt}: {pct}%'
    ))

fig.update_layout(
    title="Reported Types of Bullying Among Students (3D Interactive)",
    scene=dict(
        xaxis=dict(title="Type of Bullying", tickvals=x, ticktext=bullying_types, backgroundcolor="black", color="white", gridcolor="gray"),
        yaxis=dict(title="", showticklabels=False, backgroundcolor="black", color="white", gridcolor="gray"),
        zaxis=dict(title="Percentage of Students (%)", range=[0, 25], backgroundcolor="black", color="white", gridcolor="gray"),
        camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
    ),
    margin=dict(l=0, r=0, b=0, t=40),
    showlegend=False,
    paper_bgcolor="black",
    plot_bgcolor="black",
    font=dict(color="white")
)

fig.show()
