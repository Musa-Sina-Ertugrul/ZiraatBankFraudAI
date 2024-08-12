from groq import Groq
import json
import sqlite3
from tqdm.auto import tqdm
config = {"model":"llama-3.1-8b-instant",
    "messages":[
        {
            "role": "user",
            "content": "JSON olarak Bana fraud detection hikayesi yazman lazım: \
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
                                                    12. Sadece dediklerimi yap fazladan label ekleme"
        }
    ],
    "temperature":0.35,
    "max_tokens":1024,
    "top_p":1,
    "response_format":{"type": "json_object"},}
client = Groq(api_key="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")
create_response = client.chat.completions.create

def clear_punc(text:str):
    import string

    for punc in string.punctuation:

        text = text.replace(punc,"")
    return text

if __name__ == "__main__":

    connection = sqlite3.connect("/home/musasina/Desktop/projects/ZiraatBankFraudAI/groq_dataset/collected_data.db")
    cursor = connection.cursor()
    count = 0
    while count < 3000:
        try:
            response = create_response(**config)
            response_as_dict = json.loads(str(response.choices[0].message.content.strip()))
            cursor.execute(f"INSERT INTO data(text, label) VALUES('{clear_punc(response_as_dict['hikaye']['text'])}', '{clear_punc(response_as_dict['hikaye']['label'])}');")
            connection.commit()
            count += 1
            print(f"{count} text created")
        except BaseException:
            continue
    connection.close()


