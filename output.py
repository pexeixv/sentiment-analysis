 pex@Asus >  py main.py
[nltk_data] Downloading package wordnet to
[nltk_data]     C:\Users\pex\AppData\Roaming\nltk_data...
[nltk_data]   Package wordnet is already up-to-date!
[nltk_data] Downloading package omw-1.4 to
[nltk_data]     C:\Users\pex\AppData\Roaming\nltk_data...
[nltk_data]   Package omw-1.4 is already up-to-date!

Train data stats: 

10 random sample:
                                                   text  category
2712  Salman khan Teri maa ki chuth aur Teri bahan k...  negative
3136  sukun mila . . bade dino baad udbilao aur lunc...  positive
6785  i think afridi want kohli to be more aggressiv...   neutral
6751  Ek baar maine jo commitment kar di uske baad a...   neutral
4135             guddu playing bhagat singh . . . . lol   neutral
3272  rt @insan1674044: "#msgyouthicon @gurmeetramra...  positive
4542  Salman Bhai aap cinta mat karo apki movie ham ...  positive
7209  mene socha tha ki aap humesa such bolte he aur...  negative
4150  Aap ko letter b likhy hain shayd ap tk puhnch ...   neutral
3435  msgyouthicon its a best efrt to show better p...  positive


First 10 rows:
                                                text  category
0                                Han wo bhi baat hai   neutral
1  its not unionbudget2015 its buredinkabudget ...  negative
2  public movie review :- shamitabh shamitabh a...   neutral
3                                                 ok   neutral
4  salmaan khan tumhare naam k pichey khan accha ...  negative
5  bhaijaan thagaye hoghaey itne saare comments d...   neutral
6  mummy jabb apne kisi dost ko nick name se bula...   neutral
7                     bas kar rulayega kya . . . . .   neutral
8  Bajrangi Bhai hamse bhi guftgu kar liya karo.....  positive
9  Uhhh what ever happened to the \ " this page i...   neutral


Total columns:
Index(['text', 'category'], dtype='object')


Shape:
(10080, 2)


Overall data:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10080 entries, 0 to 10079
Data columns (total 2 columns):      
 \#   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   text      10079 non-null  object
 1   category  10080 non-null  object
dtypes: object(2)
memory usage: 157.6+ KB
None


Data type;
text        object
category    object
dtype: object     


Total number null rows:
1


Total target value:
['neutral' 'negative' 'positive']


Test data stats:

10 random sample:
                                                   text  category
87    sabse mast hai launcher paji udbilaao ka la li...  positive
323                           Muje apse shadi karni hai  positive
1228              Salman bhai ab to ap shadi kr lain...   neutral
821                 dhoni ka helicopter shot;-) ;-) ;-)  positive
1140                  Bhai sab ko pagal samjha h kha ho  negative
196   @sumona24 who will decide priority u, film fra...   neutral
320          EID mubarak aur hit (film)mubarak advance.  positive
1216                          Ye mera recreation time h   neutral
608   sabhi bandra aao mere ghar par sabse milunga main   neutral
1192  @someUSER @someUSER close early on thanksgivin...  positive


First 10 rows:
                                                text  category
0            Kuch nhi launde .. Bas thodi bahut holi   neutral
1  intermission fc took a big step towards the ti...  positive
2  @msgthefilm @gurmeetramrahim msgyouthicon we ...   neutral
3  ha ha ha ha ha ha ha . . . . . :d ye mast tha ...  positive
4          yaar woh toh bahut importantg courseg hai   neutral
5  @someUSER 1win from the superbowl ! game tomor...  positive
6                                    apko ana padega   neutral
7  beta agr aisi hi achi life chahta hai to ladki...  negative
8  @someUSER @someUSER surface the florida mall ...  positive
9                               Hloo salu bhai......   neutral


Total columns:
Index(['text', 'category'], dtype='object')


Shape:
(1261, 2)


Overall data:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1261 entries, 0 to 1260
Data columns (total 2 columns):
 \#   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   text      1261 non-null   object
 1   category  1261 non-null   object
dtypes: object(2)
memory usage: 19.8+ KB
None


Data type;
text        object
category    object
dtype: object


Total number null rows:
0


Total target value:
['neutral' 'positive' 'negative']


No. of feature_words:  19762



Logical Regression Model:


Classification report:
              precision    recall  f1-score   support

    negative       0.52      0.39      0.44       290
     neutral       0.57      0.68      0.62       586
    positive       0.55      0.49      0.52       385

    accuracy                           0.56      1261
   macro avg       0.55      0.52      0.53      1261
weighted avg       0.55      0.56      0.55      1261



Confusion Matrix:
[[113 137  40]
 [ 76 397 113]
 [ 29 166 190]]


Prediction Accuracy:
0.5551149881046789