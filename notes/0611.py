#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns


# In[3]:


var = ['a', 'a', 'b', 'b', 'b', 'c']
var


# In[4]:


sns.countplot(x = var)


# In[5]:


df = sns.load_dataset('titanic')
df


# In[7]:


sns.countplot(data = df, x = 'sex')


# In[8]:


sns.countplot(data = df, x = 'sex', hue = 'alive')


# In[11]:


sns.countplot(data = df, y = 'class', hue = 'sex')


# In[12]:


pip install pydataset


# In[13]:


import pydataset


# In[14]:


pydataset.data()


# In[15]:


df = pydataset.data('mtcars')
df


# In[16]:


score = [80, 60, 70, 50 , 90]
print(score)
sum_score = sum(score)
print(sum_score)


# In[18]:


pip install pandas


# In[19]:


import pandas as pd


# In[23]:


df = pd.DataFrame({"name" : ["김지훈", "이유진", "박동현", "김민지"],
                  "english": [90, 80, 60, 70],
                  "math" : [50, 60, 100, 20]})
df


# In[24]:


df['english']


# In[25]:


sum(df['english'])


# In[26]:


sum(df['english']) / 4


# In[36]:


df2 = pd.DataFrame({'product' : ['사과', '딸기', '수박'],
                   'price' : [1800, 1500, 3000],
                   'count' : [24, 38, 13]})
df2


# In[39]:


print(sum(df2['price']))
print(sum(df2['price']) / 3)


# In[40]:


df_exam = pd.read_excel('excel_exam.xlsx')
df_exam


# In[45]:


# 수학 점수 평균 구하기
print(sum(df_exam['math']) / 20)
print(sum(df_exam['math']) / len(df_exam))


# In[46]:


# 영어 점수 평균 구하기
print(sum(df_exam['english']) / 20)
print(sum(df_exam['english']) / len(df_exam))


# In[50]:


# 과학 점수 평균 구하기
print(sum(df_exam['science']) / 20)
print(sum(df_exam['science']) / len(df_exam))


# In[53]:


df_exam_novar = pd.read_excel('excel_exam_novar.xlsx')
df_exam_novar


# In[55]:


df_exam_novar = pd.read_excel('excel_exam_novar.xlsx', header = None)
df_exam_novar


# In[57]:


df_csv = pd.read_csv('exam.csv')
df_csv


# In[59]:


# 데이터프레임을 csv 파일로 저장하기
df_midterm = pd.DataFrame({'english' : [90, 80, 60, 70],
                          'math' : [50, 60, 100, 20],
                          'nclass' : [1, 1, 2, 2]})
df_midterm
df_midterm.to_csv("output_newdata.csv")


# In[60]:


import pandas as pd


# In[61]:


exam = pd.read_csv('exam.csv')


# In[62]:


exam.head()


# In[63]:


exam.head(8)


# In[64]:


exam.tail()


# In[65]:


exam.tail(10)


# In[66]:


exam.shape


# In[67]:


exam.info()
# <class 'pandas.core.frame.DataFrame'> : 해당 데이터가 pandas로 만든 데이터프레임이다.
# RangeIndex: 20 entries, 0 to 19 : 20개의 행으로 이루어져있으며, 행 번호는 0 ~ 19이다.
# Data columns (total 5 columns) : exam의 변수는 5개로 구성되어 있다.


# In[70]:


exam.describe(include = 'all')


# In[71]:


mpg = pd.read_csv('mpg.csv')
mpg


# In[72]:


mpg.head()


# In[73]:


mpg.tail()


# In[74]:


mpg.info()


# In[75]:


mpg.shape


# In[76]:


mpg.describe()


# In[77]:


mpg.describe(include = 'all')
# count = 빈도: 값의 개수
# unique = 고유값 빈도 : 중복을 제거한 범주의 개수
# top = 최빈값 : 개수가 가장 많은 값
# freq = 최빈값 빈도 : 개수가 가장 많은 값의 개수


# In[78]:


# 변수명 바꾸기
df_raw = pd.DataFrame({'var1' : [1, 2, 1],
                      'var2' : [2, 3, 2]})
df_raw


# In[79]:


# 데이터프레임 복사본 만들기
df_new = df_raw.copy()
df_new
# 복사본 만들기는 변수명.copy() 하면 된다


# In[80]:


df_new = df_new.rename(columns = {'var2' : 'v2'})
df_new


# In[82]:


df_raw


# In[84]:


mpg_new = mpg.copy()
mpg_new


# In[85]:


mpg_new = mpg_new.rename(columns = {"cty" : "city",
                          "hwy" : "highway"})
mpg_new


# In[86]:


# 파생변수 만들기: 기존의 변수를 변형해 만든 변수
df = pd.DataFrame({'var1' : [4, 3, 8],
                  'var2' : [2, 6, 1]})
df


# In[87]:


df['var_sum'] = df['var1'] + df['var2']
df


# In[90]:


df['var_mean'] = df['var_sum'] / 2
df


# In[93]:


mpg_new['total'] = (mpg_new['city'] + mpg_new['highway']) / 2
mpg_new


# In[94]:


sum(mpg_new['total']) / len(mpg_new)


# In[95]:


mpg_new['total'].mean()


# In[96]:


# 조건문을 활용해 파생변수 만들기
# 전체 자동차 중에서 연비 기준을 충족해 '고연비 합격 판정'을 받은 자동차가 몇 대?
# 연비가 기준값을 넘으면 합격, 넘지 못하면 불합격
mpg_new['total'].describe()


# In[100]:


mpg_new['total'].plot.hist()


# In[101]:


import numpy as np


# In[103]:


mpg_new['test'] = np.where(mpg_new['total'] >= 20,'pass', 'fail')
mpg_new


# In[106]:


mpg_new['test'].value_counts()


# In[107]:


# 막대 그래프로 빈도 표현하기
count_test= mpg_new['test'].value_counts()


# In[108]:


count_test.plot.bar()


# In[111]:


# 축 이름 회전하기
count_test.plot.bar(rot = 30)


# In[114]:


# 중첩 조건문 활용하기
mpg_new['grade'] = np.where(mpg_new['total'] >= 30, 'A', np.where(mpg_new['total'] >= 20, 'B', 'C'))
mpg_new.head(20)


# In[119]:


count_grade = mpg_new['grade'].value_counts()
count_grade


# In[121]:


count_grade.plot.bar(rot = 0)


# In[124]:


# 등급 빈도표 알파벳순 정렬
count_grade = mpg_new['grade'].value_counts().sort_index()
count_grade


# In[126]:


count_grade.plot.bar(rot = 0)


# In[137]:


mpg_new['size'] = np.where((mpg_new['category'] == 'compact')|
                           (mpg_new['category'] == 'subcompact')|
                           (mpg_new['category'] == '2seater'), 'small', 'large')
mpg_new


# In[138]:


mpg_new['size'] = np.where(mpg_new['category'].isin(['compact', 'subcompact','2seater']), 'small', 'large')
mpg_new


# In[3]:


import pandas as pd
midwest = pd.read_csv('midwest.csv')
midwest


# In[4]:


midwest.head()


# In[5]:


midwest.tail()


# In[6]:


midwest.shape


# In[7]:


midwest.info()


# In[8]:


midwest.describe()


# In[11]:


midwest.describe(include = 'all')


# In[13]:


midwest_new = midwest.copy()
midwest_new


# In[18]:


midwest_new = midwest.rename(columns = {'poptotal' : 'total',
                                     'popasian' : 'asian'})
midwest_new


# In[22]:


midwest_new['asian_ratio'] = (midwest_new['asian'] / midwest_new['total']) * 100
midwest_new


# In[23]:


ratio_hist = midwest_new['asian_ratio']
ratio_hist.plot.hist()


# In[27]:


import numpy as np


# In[29]:


midwest_new['avg_asian'] = np.where(midwest_new['asian_ratio'] > midwest_new['asian_ratio'].mean(), 'large', 'small')
midwest_new.head(15)


# In[45]:


midwest_new['avg_asian'].value_counts()


# In[49]:


midwest_new['avg_asian'].value_counts().plot.bar(rot = 0)


# In[2]:


# 자유자재로 데이터 가공하기
# 1. 데이터 전처리 : 원하는 형태로 데이터 가공하기
# 2. 조건에 맞는 데이터만 추출하기
import pandas as pd
exam = pd.read_csv('exam.csv')
exam


# In[3]:


exam.query('nclass == 1')


# In[4]:


exam.query('nclass == 2')


# In[5]:


exam.query('nclass != 1')


# In[6]:


# 수학 점수가 50점을 초과한 경우
exam.query('math > 50')


# In[7]:


# 수학 점수가 50점 미만인 경우
exam.query('math < 50')


# In[8]:


# 영어 점수가 50점 이상인 경우
exam.query('english >= 50')


# In[9]:


# 영어 점수가 80점 이하인 경우
exam.query('english <= 80')


# In[10]:


# 여러 조건을 충족하는 행 추출하기
exam.query('nclass == 1 & math >= 50')


# In[11]:


# 2반이면서 영어 점수가 80점 이상인 경우
exam.query('nclass == 2 & english >= 80')


# In[13]:


# 여러 조건 중 하나 이상을 충족하는 행 추출하기
# 수학 점수가 90점 이상이거나 영어 점수가 90점 이상인 경우
exam.query('math >= 90 | english >= 90')


# In[15]:


# 영어 점수가 90점 미만이거나 과학 점수가 50점 미만인 경우
exam.query('english < 90 | science < 50')


# In[16]:


# 목록에 해당하는 행 추출하기
# 1, 3, 5반에 해당하면 추출
exam.query('nclass == 1 | nclass == 3 | nclass == 5')


# In[17]:


# in을 사용하기
exam.query('nclass in [1, 3, 5]')


# In[25]:


# 추출한 행으로 데이터 만들기
# nclass가 1인 행을 추출해 nclass1에 할당
nclass1 = exam.query('nclass == 1')

# nclass가 2인 행을 추출해 nclass2에 할당
nclass2 = exam.query('nclass == 2')


# In[26]:


# 1반 수학 점수 평균 구하기
nclass1['math'].mean()


# In[42]:


# 2반 수학 점수 평균 구하기
nclass2['math'].mean()


# In[47]:


import pandas as pd
# 문자 변수를 이용해 조건에 맞는 행 추출하기
df= pd.DataFrame({'sex' : ['F', 'M', 'F', 'M'],
             'country' : ['Korea', 'China', 'Japan', 'USA']})
df


# In[48]:


# 전체 조건에 작은따옴표, 추출할 문자에 큰따옴표 사용
df.query('sex == "F" & country == "Korea"')


# In[50]:


# 전체 조건에 큰따옴표로 썼다면 추출 문자는 작은 따옴표를 사용
df.query("sex == 'M' & country == 'China'")


# In[51]:


# 외부 변수를 이용해 추출하기
var = 3
exam.query('nclass == @var')


# In[ ]:




