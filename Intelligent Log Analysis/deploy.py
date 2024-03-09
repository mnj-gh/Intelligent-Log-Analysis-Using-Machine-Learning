from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load your trained machine learning model
model = joblib.load('savemodel.sav')

@app.route('/', methods=['GET', 'POST'])
def index():
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
        # Make prediction using your model
        result = model.predict([[Bwd_Pkt_Len_Std, PSH_Flag_Cnt, Fwd_Seg_Size_Min, Bwd_Pkt_Len_Min, ACK_Flag_Cnt, Fwd_IAT_Std, Init_Fwd_Win_Byts, Flow_IAT_Max, Bwd_Pkts, Bwd_IAT_Tot, URG_Flag_Cnt, Pkt_Len_Min]])
        prediction = "ANOMALY DETECTED!!!" if result[0] != 0 else "NO ANOMALY DETECTED!!!"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)