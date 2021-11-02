#!/usr/bin/env python
# coding: utf-8

def getprice(new):
	import pandas as pd
	file_path='melb_data.csv'
	file_data=pd.read_csv(file_path)


	file_data.columns

	y=file_data.Price
	y.head()

	file_features=['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

	X=file_data[file_features]
	X.head()

	X.describe()

	from sklearn.tree import DecisionTreeRegressor

	melbourne_model = DecisionTreeRegressor(random_state=1)
	melbourne_model.fit(X, y)


	return melbourne_model.predict(new)[0]






