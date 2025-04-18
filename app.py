import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True 

model = pickle.load(open('models/savemodel.sav', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def input_form():
    prediction = None
    if request.method == 'POST':
        Bwd_Pkt_Len_Std = float(request.form['Bwd_Pkt_Len_Std'])
        PSH_Flag_Cnt = float(request.form['PSH_Flag_Cnt'])
        Fwd_Seg_Size_Min = float(request.form['Fwd_Seg_Size_Min'])
        Bwd_Pkt_Len_Min = float(request.form['Bwd_Pkt_Len_Min'])
        ACK_Flag_Cnt = float(request.form['ACK_Flag_Cnt'])
        Fwd_IAT_Std = float(request.form['Fwd_IAT_Std'])
        Init_Fwd_Win_Byts = float(request.form['Init_Fwd_Win_Byts'])
        Flow_IAT_Max = float(request.form['Flow_IAT_Max'])
        Bwd_Pkts = float(request.form['Bwd_Pkts/s'])
        Bwd_IAT_Tot = float(request.form['Bwd_IAT_Tot'])
        URG_Flag_Cnt = float(request.form['URG_Flag_Cnt'])
        Pkt_Len_Min = float(request.form['Pkt_Len_Min'])

        result = model.predict([[Bwd_Pkt_Len_Std, PSH_Flag_Cnt, Fwd_Seg_Size_Min, Bwd_Pkt_Len_Min,
                                 ACK_Flag_Cnt, Fwd_IAT_Std, Init_Fwd_Win_Byts, Flow_IAT_Max,
                                 Bwd_Pkts, Bwd_IAT_Tot, URG_Flag_Cnt, Pkt_Len_Min]])

        prediction = "ANOMALY DETECTED!!!" if result[0] != 0 else "NO ANOMALY DETECTED!!!"

    return render_template('form.html', prediction=prediction)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
