from flask import Flask,request,render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    
    
    else:
        data=CustomData(
            Duration = int(request.form.get('Duration')),
            Count = int(request.form.get('Count')),
            DestinationBytes = int(request.form.get('DestinationBytes')),
            DiffSrvRate = float(request.form.get('DiffSrvRate')),
            DstHostCount = int(request.form.get('DstHostCount')),
            DstHostDiffSrvRate = float(request.form.get('DstHostDiffSrvRate')),
            DstHostRerrorRate = float(request.form.get('DstHostRerrorRate')),
            DstHostSameSrcPortRate = float(request.form.get('DstHostSameSrcPortRate')),
            DstHostSameSrvRate = float(request.form.get('DstHostSameSrvRate')),
            DstHostSerrorRate = float(request.form.get('DstHostSerrorRate')),
            DstHostSrvCount = int(request.form.get('DstHostSrvCount')),
            DstHostSrvDiffHostRate = float(request.form.get('DstHostSrvDiffHostRate')),
            DstHostSrvRerrorRate = float(request.form.get('DstHostSrvRerrorRate')),
            DstHostSrvSerrorRate = float(request.form.get('DstHostSrvSerrorRate')),
            Flag = request.form.get('Flag'),
            Hot = int(request.form.get('Hot')),
            IsGuestLogin = int(request.form.get('IsGuestLogin')),
            IsHostLogin = int(request.form.get('IsHostLogin')),
            Land = int(request.form.get('Land')),
            LoggedIn = int(request.form.get('LoggedIn')),
            NumAccessFiles = int(request.form.get('NumAccessFiles')),
            NumCompromised = int(request.form.get('NumCompromised')),
            NumFailedLogins = int(request.form.get('NumFailedLogins')),
            NumFileCreations = int(request.form.get('NumFileCreations')),
            NumOutboundCmds = int(request.form.get('NumOutboundCmds')),
            NumRoot = int(request.form.get('NumRoot')),
            NumShells = int(request.form.get('NumShells')),
            ProtocolType = request.form.get('ProtocolType'),
            RerrorRate = float(request.form.get('RerrorRate')),
            RootShell = int(request.form.get('RootShell')),
            SameSrvRate = float(request.form.get('SameSrvRate')),
            SerrorRate = float(request.form.get('SerrorRate')),
            Service = request.form.get('Service'),
            SourceBytes = int(request.form.get('SourceBytes')),
            SrvCount = int(request.form.get('SrvCount')),
            SrvDiffHostRate = float(request.form.get('SrvDiffHostRate')),
            SrvRerrorRate = float(request.form.get('SrvRerrorRate')),
            SrvSerrorRate = float(request.form.get('SrvSerrorRate')),
            SuAttempted = int(request.form.get('SuAttempted')),
            Urgent = int(request.form.get('Urgent')),
            WrongFragment = int(request.form.get('WrongFragment'))


        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)






if __name__=="__main__":
    app.run(host='0.0.0.0',port = 5000 ,debug=True)

