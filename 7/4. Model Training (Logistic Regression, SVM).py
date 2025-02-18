from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()
model.fit(X_train_resampled, y_train_resampled)
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")


from sklearn.svm import SVC

svm_model = SVC(kernel='linear')
svm_model.fit(X_train_resampled, y_train_resampled)
y_pred_svm = svm_model.predict(X_test)

print(f"SVM Accuracy: {accuracy_score(y_test, y_pred_svm):.2f}")
