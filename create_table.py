import sqlite3

connection = sqlite3.connect("/home/musasina/Desktop/projects/ZiraatBankFraudAI/gemini_dataset/collected_data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE data(text,label)")