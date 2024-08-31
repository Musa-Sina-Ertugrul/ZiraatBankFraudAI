from flask import Flask, request,render_template,flash
import string
import torch
import pickle
import torch.nn.functional as F
from transformers import AutoModel,AutoModelForSequenceClassification,AutoModelForCausalLM,AutoTokenizer
from models import ModelFraud,ModelSent
import sklearn
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "./ui/uploaded"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

with open('./ui/models/cc_fraud_model.pkl','rb') as f:
    cc_fraud_model = pickle.load(f)

tokenizer_sent = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
tokenizer_sent.padding_side = "left"
tokenizer_sent.pad_token = tokenizer_sent.eos_token
tokenizer_sent.add_special_tokens({'pad_token': '[PAD]'})

tokenizer_fraud = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
tokenizer_fraud.padding_side = "left"
tokenizer_fraud.pad_token = tokenizer_fraud.eos_token
tokenizer_fraud.add_special_tokens({'pad_token': '[PAD]'})

model_fraud = ModelFraud().to("cuda")
model_sent = ModelSent().to("cuda")
model_sent.load_state_dict(torch.load("./ui/models/model_sent.pth")["model_state_dict"])
model_fraud.load_state_dict(torch.load("./ui/models/model_fraud.pth")["model_state_dict"])

cc_fraud_result_table = {0:"Sahtecilik yok",1:"Sahtecilik olabilir"}
fraud_result_table = {0:"Sahtecilik olabilir",1:"Sahtecilik yok"}
sent_result_table = {0:"Negatif",1:"Notr",2:"Pozitif"}

def preprocess_fraud(examples):
    model_inputs = tokenizer_fraud(examples, max_length=256,padding="max_length",truncation=True,return_tensors="pt")
    return model_inputs["input_ids"]

def preprocess_sent(examples):
    model_inputs = tokenizer_sent(examples, max_length=128,padding="max_length",truncation=True,return_tensors="pt")
    return model_inputs["input_ids"]

letters = set(list(string.ascii_letters + "ışİŞüğÜĞçöÇÖ 0123456789"))

def remove_wrong_letters(text:str):
    text_as_list = list(text)
    result_text_list = text_as_list.copy()
    for letter in text_as_list:
        if letter not in letters:
            result_text_list.remove(letter)
    
    return ("".join(result_text_list)).casefold()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fraud/')
def fraud_analysis():
    return render_template("fraud_analysis.html")

@app.route('/cc_fraud/')
def cc_fraud_analysis():
    return render_template("cc_fraud_analysis.html")

@app.route('/upload_sentiment/', methods=['POST'])
def upload_sentiment():
    text = request.form['main_text_input']
    cleared_text = remove_wrong_letters(text)
    preprocessed_text = preprocess_sent(cleared_text).to("cuda")
    result = torch.argmax(model_sent(preprocessed_text),dim=1).cpu().item()
    flash(sent_result_table[result])
    return render_template("index.html")

@app.route('/upload_fraud/', methods=['POST'])
def upload_fraud():
    text = request.form['main_text_input']
    cleared_text = remove_wrong_letters(text)
    preprocessed_text = preprocess_fraud(cleared_text).to("cuda")
    result = torch.argmax(model_fraud(preprocessed_text),dim=1).cpu().item()
    flash(fraud_result_table[result])
    return render_template("fraud_analysis.html")

@app.route('/upload_cc_fraud/', methods=['POST'])
def upload_cc_fraud():
    step_count = float(request.form['main_input_step'])
    trans_type = float(request.form['main_input_type'])
    amount = float(request.form['main_input_amount'])
    old_orig = float(request.form['main_input_old_orig'])
    new_orig = float(request.form['main_input_new_orig'])
    old_dest = float(request.form['main_input_old_dest'])
    new_dest = float(request.form['main_input_new_dest'])
    model_input = [[step_count,trans_type,amount,old_orig,new_orig,old_dest,new_dest]]
    result = cc_fraud_model.predict(model_input)
    flash(cc_fraud_result_table[int(result[0])])
    return render_template("cc_fraud_analysis.html")

if __name__ == "__main__":
    app.run(debug=True)