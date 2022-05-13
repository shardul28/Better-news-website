from flask import Flask, render_template,request
import pandas as pd
app = Flask(__name__)
import json
@app.route('/',methods=['POST','GET'])
def entry_point():
    from getting_data import news0,title0,subjectivity_score0,polarity_score0,bias0,predicted0,topic0,tags0,news1,title1,subjectivity_score1,polarity_score1,bias1,predicted1,topic1,tags1,news2,title2,subjectivity_score2,polarity_score2,bias2,predicted2,topic2,tags2,news3,title3,subjectivity_score3,polarity_score3,bias3,predicted3,topic3,tags3,news4,title4,subjectivity_score4,polarity_score4,bias4,predicted4,topic4,tags4,news5,title5,subjectivity_score5,polarity_score5,bias5,predicted5,topic5,tags5


    return render_template('index.html',news0=news0,title0=title0,subjectivity_score0=subjectivity_score0,polarity_score0=polarity_score0,bias0=bias0,predicted0=predicted0,topic0=topic0,tags0=tags0,news1=news1,title1=title1,subjectivity_score1=subjectivity_score1,polarity_score1=polarity_score1,bias1=bias1,predicted1=predicted1,topic1=topic1,tags1=tags1,news2=news2,title2=title2,subjectivity_score2=subjectivity_score2,polarity_score2=polarity_score2,bias2=bias2,predicted2=predicted2,topic2=topic2,tags2=tags2,news3=news3,title3=title3,subjectivity_score3=subjectivity_score3,polarity_score3=polarity_score3,bias3=bias3,predicted3=predicted3,topic3=topic3,tags3=tags3,news4=news4,title4=title4,subjectivity_score4=subjectivity_score4,polarity_score4=polarity_score4,bias4=bias4,predicted4=predicted4,topic4=topic4,tags4=tags4,news5=news5,title5=title5,subjectivity_score5=subjectivity_score5,polarity_score5=polarity_score5,bias5=bias5,predicted5=predicted5,topic5=topic5,tags5=tags5)
if __name__ == '__main__':
    app.run(debug=True)
