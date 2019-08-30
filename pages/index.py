import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
             2014 survey which measures the occurrence and prevalence of mental health disorders in the Tech workplace. 

            People who had a family history of mental health disorders were more likely to be affected at work, if they felt that it would be difficult for them to take leave days. 

            Women in the tech industries are much more likely to be affected at work by mental health disorders they younger they are. Where contrarily, men, are much more likely to be affected the older they are. 

            Men and women who are not in the tech industry show an inverse pattern. Older women and younger aged men are more affected.      
            
            Being self-employed increases the chance of mental health disorders and with those disorders interfering with work. 

            For male employees, being employed in the tech industry does not have an impact on a mental health disorder interfering with work. 

            Women employees seem slightly more mentally healthy if they are employed in the tech industry 
            
            Mental health disorders are an impediment on performance and productivity. Everyone is affected differently and those with a family history of mental health disorders are more prone and vulnerable to mental health disorders and their impact on their work. 

            As it is shown that employees who were under stricter leave policies at their workplace were more likely to suffer from a mental health disorders, a solution may be for companies to have better, more flexible, leave policies in place which would help lead to a reduction in mental health disorders having an impact on an employees work performance and productivity. 

            When going over the true predictions versus the predictions, It shows that the confusion matrix told us that our model did not accurately predict the correct values. The number of true values that were true and true values that were false are nearly identical. False values that were true versus false values that were false were also nearly identical.  












            """
        ),
        dcc.Link(dbc.Button('Button to Nowhere', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
       html.Div(
            [
             html.Img(
                            src=app.get_asset_url("../assets/download.png"),
                            id="plotly-image",
                            style={
                                "height": "auto",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
               html.Img(
                            src=app.get_asset_url("../assets/download2.png"),
                            id="plotly-image",
                            style={
                                "height": "auto",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
               html.Img(
                            src=app.get_asset_url("../assets/download3.png"),
                            id="plotly-image",
                            style={
                                "height": "auto",
                                "width": "auto",
                                "margin-bottom": "25px",
                            },
                        ),
               
             
            ]
       )
    ]

)

layout = dbc.Row([column1, column2])
