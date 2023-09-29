import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from sklearn.linear_model import LinearRegression
import pandas as pd


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("House Price Predictor")
        self.setGeometry(100, 100, 500, 300)
        self.setFixedSize(500, 300)

        self.label1 = QLabel(self)
        self.label1.setText("Number of bedrooms:")
        self.label1.move(50, 50)

        self.bedrooms = QLineEdit(self)
        self.bedrooms.move(200, 50)

        self.label2 = QLabel(self)
        self.label2.setText("Number of bathrooms:")
        self.label2.move(50, 80)

        self.bathrooms = QLineEdit(self)
        self.bathrooms.move(200, 80)

        self.label3 = QLabel(self)
        self.label3.setText("Square footage:")
        self.label3.move(50, 110)

        self.square_footage = QLineEdit(self)
        self.square_footage.move(200, 110)

        self.label4 = QLabel(self)
        self.label4.setText("Year built:")
        self.label4.move(50, 140)

        self.year_built = QLineEdit(self)
        self.year_built.move(200, 140)

        self.label5 = QLabel(self)
        self.label5.setText("Zipcode:")
        self.label5.move(50, 170)

        self.zipcode = QLineEdit(self)
        self.zipcode.move(200, 170)

        self.predict_button = QPushButton("Predict", self)
        self.predict_button.move(200, 220)
        self.predict_button.clicked.connect(self.predict)

    def predict(self):
        try:
            model = LinearRegression()
            data = pd.read_csv("house_data.csv")
            X = data[["bedrooms", "bathrooms", "sqft_living", "yr_built", "zipcode"]]
            y = data["price"]
            model.fit(X, y)

            bedrooms = float(self.bedrooms.text())
            bathrooms = float(self.bathrooms.text())
            sqft_living = float(self.square_footage.text())
            yr_built = float(self.year_built.text())
            zipcode = float(self.zipcode.text())

            price = model.predict([[bedrooms, bathrooms, sqft_living, yr_built, zipcode]])

            QMessageBox.information(self, "Prediction", "The predicted price is $%.2f" % price)

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

