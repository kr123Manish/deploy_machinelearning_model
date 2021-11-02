from flask import Flask, render_template,request
import model as m

app=Flask(__name__)

@app.route('/',methods=["GET","POST"])
def predict():
    final_ans=''
    if request.method=="POST":
        r=request.form["rooms"]
        tb=request.form["totalBathrooms"]
        tl=request.form["totalLandsize"]
        la=request.form["lattitude"]
        lo=request.form["longtitude"]
        new=[[r,tb,tl,la,lo]]
        # new=[[2,1.0,202.0,-37.7996,144.9984]]
        ans = m.getprice(new)
        final_ans=ans
        # print("ans")
    return render_template('index.html',predicted_ans=final_ans)

if __name__ =='__main__':
    app.run(debug=True)
