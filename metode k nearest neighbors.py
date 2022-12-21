Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from sklearn.neighbors import NearestCentroid
... 
... # Database: Gerbang logika AND
... # x = Data, Y = Target
... x = [[0,0], [0,1], [1,0], [1,1], [2,0], [2,1], [3,0], [3,1], [1,3], [2,2]]
... y = [0,0,0,1,0,0,1,0,0,1]
... 
... # Training and Classify
... clf = NearestCentroid()
... clf.fit(x,y)
... 
... # Prediksi
... print ("Logika AND Metode K. Nearest Neighbors (KNN)")
... print ("Logika = Prediksi")
... print ("0 0 = ", clf.predict([[0,0]]))
... print ("0 1 = ", clf.predict([[0,1]]))
... print ("1 0 = ", clf.predict([[1,0]]))
... print ("1 1 = ", clf.predict([[1,1]]))
... print ("2 0 = ", clf.predict([[2,0]]))
... print ("2 1 = ", clf.predict([[2,1]]))
... print ("3 0 = ", clf.predict([[3,0]]))
... print ("3 1 = ", clf.predict([[3,1]]))
... print ("1 3 = ", clf.predict([[1,3]]))
