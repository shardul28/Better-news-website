import random
import pandas as pd
df=pd.read_csv('df.csv')
#print(df.count())
pd.options.display.max_colwidth = -1
randomlist = random.sample(range(1, 170), 2)+random.sample(range(172, 271), 2)+random.sample(range(273, 1258), 2)

def getbias(bias):
    if bias==0:
        return '\static\leftbias.jpg'
    if bias==1:
        return '\static/rightbias.jpg'
    if bias==3:
        return '\static\centerbias.jpg'
print(randomlist)
# for i in range(0,6):
#     print(f"news{i}=df.loc[randomlist[{i}]]['content']")
#     print(f"title{i}=df.loc[randomlist[{i}]]['title']")
#     print(f"subjectivity_score{i}=df.loc[randomlist[{i}]]['subjectivity_score']")
#     print(f"polarity_score{i}=df.loc[randomlist[{i}]]['polarity_score']")
#     print(f"bias{i}=getbias(df.loc[randomlist[{i}]]['bias'])")
#     print(f"predicted{i}=getbias(df.loc[randomlist[{i}]]['predicted'])\n")
##########################################################################
news0=df.loc[randomlist[0]]['content']
title0=df.loc[randomlist[0]]['title']
subjectivity_score0=df.loc[randomlist[0]]['subjectivity_score']
polarity_score0=df.loc[randomlist[0]]['polarity_score']
bias0=getbias(df.loc[randomlist[0]]['bias'])
predicted0=getbias(df.loc[randomlist[0]]['predicted'])

news1=df.loc[randomlist[1]]['content']
title1=df.loc[randomlist[1]]['title']
subjectivity_score1=df.loc[randomlist[1]]['subjectivity_score']
polarity_score1=df.loc[randomlist[1]]['polarity_score']
bias1=getbias(df.loc[randomlist[1]]['bias'])
predicted1=getbias(df.loc[randomlist[1]]['predicted'])

news2=df.loc[randomlist[2]]['content']
title2=df.loc[randomlist[2]]['title']
subjectivity_score2=df.loc[randomlist[2]]['subjectivity_score']
polarity_score2=df.loc[randomlist[2]]['polarity_score']
bias2=getbias(df.loc[randomlist[2]]['bias'])
predicted2=getbias(df.loc[randomlist[2]]['predicted'])

news3=df.loc[randomlist[3]]['content']
title3=df.loc[randomlist[3]]['title']
subjectivity_score3=df.loc[randomlist[3]]['subjectivity_score']
polarity_score3=df.loc[randomlist[3]]['polarity_score']
bias3=getbias(df.loc[randomlist[3]]['bias'])
predicted3=getbias(df.loc[randomlist[3]]['predicted'])

news4=df.loc[randomlist[4]]['content']
title4=df.loc[randomlist[4]]['title']
subjectivity_score4=df.loc[randomlist[4]]['subjectivity_score']
polarity_score4=df.loc[randomlist[4]]['polarity_score']
bias4=getbias(df.loc[randomlist[4]]['bias'])
predicted4=getbias(df.loc[randomlist[4]]['predicted'])

news5=df.loc[randomlist[5]]['content']
title5=df.loc[randomlist[5]]['title']
subjectivity_score5=df.loc[randomlist[5]]['subjectivity_score']
polarity_score5=df.loc[randomlist[5]]['polarity_score']
bias5=getbias(df.loc[randomlist[5]]['bias'])
predicted5=getbias(df.loc[randomlist[5]]['predicted'])
# print(title0,'\n',news0)
#for i in range(0,6):
    # print(f"news{i}=news{i},title{i}=title{i},subjectivity_score{i}=subjectivity_score{i},polarity_score{i}=polarity_score{i},bias{i}=bias{i},predicted{i}=predicted{i},",end='')
for i in range(0,6):
     print(f"news{i},title{i},subjectivity_score{i},polarity_score{i},bias{i},predicted{i},",end='')