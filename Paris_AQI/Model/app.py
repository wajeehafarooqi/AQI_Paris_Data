from flask import Flask,render_template,url_for
import pandas as pd 
import pickle


app = Flask(__name__)
# load the model from disk
loaded_model=pickle.load(open("C://Users/wajee/OneDrive/Bureau/projects/Paris_AQI/Model/Random_forest.pkl", 'rb'))


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv('C://Users/wajee/OneDrive/Bureau/projects/Paris_AQI/Data/Data/Extract-Data/ex_2017.csv')
    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    return render_template('result.html',prediction = my_prediction)


if __name__ == '__main__':
	app.run(debug=True)
