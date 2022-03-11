from dash import Dash,html,dcc,Input,Output
import pickle
import numpy as np


# Uploading our Logistic Regression Model
model_name = 'model.sav'

model = pickle.load(open(model_name, 'rb'))

app = Dash(__name__)

app.layout = html.Div([
        
    html.Table([
        html.Tr([html.Td(html.H2('Select Passenger Class')),
                 html.Td(dcc.RadioItems(options=[1,2,3],value=1,id='input-pclass'),style={'width':'60%'}),
                 html.Td([html.H1('Result',style={'color':'indianred'}),html.H1(id='output-prediction',style={'color':'navy'})],rowSpan=4)
                ]),
        html.Tr([html.Td(html.H2('Select Gender')),
                 html.Td(dcc.RadioItems(options=[
                        {'label':'Male','value':0},
                        {'label':'Female','value':1},
                    ],
                    value = 0,
                    id='input-sex')),
                ]),
        html.Tr([html.Td(html.H2('Select Age')),
                 html.Td(dcc.Slider(0,100,step=5,value=20,
                        marks = {str(age): str(age) for age in range(0,105,5)},
                        id = 'input-age')),
                ]),
        html.Tr([html.Td(html.H2('Select Sibsp')),
                 html.Td(dcc.Slider(0,8,step = 1, value = 0,
                        marks = {str(n): str(n) for n in range(9)},
                        id = 'input-sibsp'),),
                ]),
        html.Tr([html.Td(html.H2('Select Parch')),
                 html.Td(dcc.Slider(0,8,step = 1, value = 0,
                        marks = {str(n): str(n) for n in range(9)},
                        id = 'input-parch'),),
                ]),
        html.Tr([html.Td(html.H2('Select Fare')),
                 html.Td(dcc.Slider(0,500,step = 50, value = 50,
                        marks = {str(fare): str(fare) for fare in range(0,501,50)},
                        id = 'input-fare'),),
                ]),
        html.Tr([html.Td(html.H2('Select Embarked')),
                 html.Td(dcc.RadioItems(options=[
                            {'label':'S','value':1},
                            {'label':'C','value':2},
                            {'label':'Q','value':3},
                            ],
                        value=1,
                        id='input-embarked'),),
                ]),
        html.Tr([html.Td(html.H2('Select Cabin')),
                 html.Td(dcc.RadioItems(options=[
                            {'label':'Yes','value':1},
                            {'label':'No','value':0},
                            ],
                        value=1,
                        id = 'input-cabin'),),
                ]),
            ]),    
    # dcc.Dropdown(),      # for floor
    # dcc.Dropdown(),      # for title
    # html.Div(id='output-prediction')
])


@app.callback(Output('output-prediction','children'),
              Input('input-pclass','value'),              
              Input('input-sex','value'),              
              Input('input-age','value'),              
              Input('input-sibsp','value'),              
              Input('input-parch','value'),              
              Input('input-fare','value'),              
              Input('input-embarked','value'),              
              Input('input-cabin','value'),              
              )

def fn(pclass,sex,age,sibsp,parch,fare,embarked,cabin,floor=1,title=1):
    if model.predict(np.array([pclass,sex,age,sibsp,parch,fare,embarked,cabin,floor,title]).reshape(1,-1)):
        return 'Survived'
    return 'Deceased'


if __name__ == '__main__':
    app.run_server(debug=True)