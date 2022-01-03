import pandas as pd

from stats import stats
from preprocessing import preprocessing
from model import model

train = pd.read_csv("train.txt", sep = "\t")
test = pd.read_csv("test.txt", sep = "\t")

print("\nTrain data stats: ")
stats.get_stats(train)
print("\n\nTest data stats: ")
stats.get_stats(test)

train = preprocessing.remove_null(train)
test = preprocessing.remove_null(test)

train_clean = preprocessing.data_prep(train)
test_clean = preprocessing.data_prep(test)

x_train = train_clean['text'].values
y_train = train_clean['category'].values

x_test = test_clean['text'].values
y_test = test_clean['category'].values

model.vector_fit(x_train)

x_train_v = model.vector_transform(x_train)
x_test_v = model.vector_transform(x_test)

print("\n\n\nLogical Regression Model:")
LRmodel = model.train_lr(x_train_v, y_train)
model.model_Evaluate(LRmodel, x_test_v, y_test)