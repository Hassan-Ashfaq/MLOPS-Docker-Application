import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template, request

app = Flask(__name__)

def Train():
    data = pd.read_csv('Salary_Data.csv')
    model = LinearRegression()
    model.fit(
        data['YearsExperience'].values.reshape(-1, 1), 
        data['Salary'].values.reshape(-1, 1)
    )
    print('Model Trained :-)')
    return model

model = Train()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        year = float(request.form['Y101'])
        out = int(model.predict(np.array(year).reshape(1, -1)))
        return render_template('predict.html', out=out)
    else:
        return render_template("file.html")

if __name__ == '__main__':
    app.run(
        debug=True, host='0.0.0.0', 
        use_reloader=False
    )
