from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
irisdata = load_iris()

x = irisdata.data
y = irisdata.target
X_train,X_test,Y_train,Y_test = train_test_split(x,y)
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train,Y_train)
predictions = knn.predict(X_test)
print(X_test)
print(predictions)
print(Y_test) 