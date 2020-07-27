import dash
import dash_table as dt
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

from transformers import pipeline

nlp_summarizer = pipeline('summarization')

# Define app
app = dash.Dash(__name__, external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

# Define Layout
app.layout = html.Div([
    html.H1('Summarisation With Hugging Face Pipeline'),
    dcc.Textarea(
        id='input_text',
        value='',
        style={'font-size': '100%', 'width': '100%', 'height': 500},
    ),
    html.Button('Summarise', id='submit_val', n_clicks=0),
    dcc.Markdown(
        id='sum_text',
        style={'font-size': '130%', 'border-style': 'solid', 'padding': '1px', 'border-width': '3px'})
])

@app.callback(
    Output('sum_text', 'children'),
    [Input('submit_val', 'n_clicks')],
    [State('input_text', "value")]
)
def summarize_text(n_clicks, input_text):
    if n_clicks != 0:
        stext = nlp_summarizer(input_text)[0]['summary_text']
        return stext

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
