import google.generativeai as genai
import sqlite3
import json

genai.configure(api_key="AIzaSyAPc4wK9B1iwA7o-alIZtOi_jQrzJ-az7E")

model = genai.GenerativeModel('gemini-1.5-pro',generation_config={"response_mime_type": "application/json"})

prompt = "Bana fraud detection hikayesi yazman lazım: \
            1. Hikaye Türkçe yazılmalı\
                3. Kişi hakkında çok fazla detay vermeli\
                    4. Kişi hakkında finansal detaylar da vermeli\
                        5. Hikayeyi fraud, not fraud diye label la\
                            6. Hikaye kendini asla tekrar etmemeli. \
                                7. Hikaye ve bilgiler birleşik olmalı, \
                                    8. Hikaye text label ının altında olmalı \
                                        9. Sonuç label isimli label ın altında olmalı, \
                                            10. Sadece 2 label olmalı text ve label \
                                                11. Bütün detaylar hikayenin içinde yazılsın\
                                                    12. Sadece dediklerimi yap fazladan label ekleme \
                                                      Using this JSON schema:\
                                                        data = {'text': str,'label':str}\
                                                            Return a `list[Recipe]`"

def clear_punc(text:str):
    import string

    for punc in string.punctuation:

        text = text.replace(punc,"")
    return text

if __name__ == "__main__":
    connection = sqlite3.connect("/home/musasina/Desktop/projects/ZiraatBankFraudAI/gemini_dataset/collected_data.db")
    cursor = connection.cursor()
    count = 0
    while count < 3000:
        try:
            response = model.generate_content(prompt)
            response_as_dict = json.loads(str(response.text.strip()))
            cursor.execute(f"INSERT INTO data(text, label) VALUES('{clear_punc(response_as_dict['text'])}', '{clear_punc(response_as_dict['label'])}');")
            connection.commit()
            count += 1
            print(f"{count} text created")
        except BaseException as e:
            continue
    connection.close()