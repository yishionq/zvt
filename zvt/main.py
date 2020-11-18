import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from zvt import init_plugins
from zvt.ui import zvt_app
from zvt.ui.apps import trader_app


def serve_layout():
    layout = html.Div(
        children=[
            dcc.Interval(
                id='interval-component',
                interval=60 * 60 * 1000,  # in milliseconds
                n_intervals=0
            ),
            # Top banner
            html.Div(
                className="zvt-banner row",
                children=[
                    html.H2(className="h2-title", children="ZVT"),
                    html.H2(className="h2-title-mobile", children="ZVT"),
                ],
            ),
            html.Div(
                children=[  # tabs
                    dcc.Tabs(
                        id="tabs-with-classes",
                        value='tab-factor',
                        className='custom-tabs',
                        children=[
                            dcc.Tab(
                                label='factor',
                                value='tab-factor',
                                className='custom-tab',
                                selected_className='custom-tab--selected'
                            ),
                            dcc.Tab(
                                label='trader',
                                value='tab-trader',
                                className='custom-tab',
                                selected_className='custom-tab--selected'
                            )
                        ]),

                    html.Div(id='tabs-content-classes', className="row app-body")]),
        ]
    )

    return layout


@zvt_app.callback(Output('tabs-content-classes', 'children'),
                  [Input('tabs-with-classes', 'value')])
def render_content(tab):
    if tab == 'tab-factor':
        return trader_app.my_layout()
    elif tab == 'tab-trader':
        return html.Div([
            html.H3('Tab content 2')
        ])


zvt_app.layout = serve_layout


def main():
    init_plugins()
    zvt_app.run_server()


if __name__ == '__main__':
    main()
