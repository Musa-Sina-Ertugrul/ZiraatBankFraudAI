from groq import Groq
import json
import sqlite3
from tqdm.auto import tqdm
import numpy as np
import pandas as pd
from copy import deepcopy
import groq

config = {"model":"llama-3.1-8b-instant",
    "messages":[
        {
            "role": "user",
            "content": """JSON olarak Bana fraud detection hikayesi yazman lazım: \
            1. Hikaye Türkçe yazılmalı\
            2. Hikaye uzun olmalı\
            3. Kişi hakkında çok fazla detay vermeli\
            4. Kişi hakkında finansal detaylar da vermeli\
            5. Hikayeyi fraud, not fraud diye label la\
            6. Hikaye kendini asla tekrar etmemeli. \
            7. Hikaye ve bilgiler birleşik olmalı, \
            8. Hikaye text label ının altında olmalı \
            9. Sonuç label isimli label ın altında olmalı, \
            10. Sadece 2 label olmalı text ve label \
            11. Bütün detaylar hikayenin içinde yazılsın\
            12. Sadece dediklerimi yap fazladan label ekleme\
            13. Kişilerin yaş bilgisi olmamalıdır.\ 
            14. Hikaye alışılmadık olmalı.
            15. Hikayeyi yazarken yaratıcılığını kullan.
            16. Hikayede olay örgüsü olmalı."""
        }
    ],
    "temperature":0,
    "max_tokens":512,
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
    extra_prompt = ""
    names = pd.read_csv("/home/musasina/Desktop/projects/ZiraatBankFraudAI/datasets/names.csv").convert_dtypes(convert_string=True)["names"].to_list()
    cities = pd.read_csv("/home/musasina/Desktop/projects/ZiraatBankFraudAI/datasets/cities.csv").convert_dtypes(convert_string=True)["names"].to_list()
    companies = pd.read_csv("/home/musasina/Desktop/projects/ZiraatBankFraudAI/datasets/companies.csv").convert_dtypes(convert_string=True)["names"].to_list()
    surnames = pd.read_csv("/home/musasina/Desktop/projects/ZiraatBankFraudAI/datasets/surnames.csv").convert_dtypes(convert_string=True)["names"].to_list()
    jobs = pd.read_csv("/home/musasina/Desktop/projects/ZiraatBankFraudAI/datasets/job_list.csv").convert_dtypes(convert_string=True)["names"].to_list()
    jobs = list(set(jobs))
    while True:
        try:
            choiced_name = np.random.choice(names)
            choiced_city = np.random.choice(cities)
            choiced_company = np.random.choice(companies)
            choiced_surname = np.random.choice(surnames)
            choiced_job = np.random.choice(jobs)
            age = np.random.randint(18,76)
            job_year = abs(np.random.randint(18,age+1)-18)
            extra_prompt = f"""17. Kişi ismi {choiced_name} olmalı 
                                18. Kişi soyadı {choiced_surname}
                                19. Kişinin yaşadığı şehir {choiced_city} olmalı
                                20. Kişinin çalıştığı şirket {choiced_company} olmalı
                                21. Kişinin yaşı {age} olmalı
                                22. Kişinin işi {choiced_job} olmalı
                                23. Kişinin özellikleri yaşına uygun olmalı
                                24. Kişinin özellikleri yaşadığı şehre uygun olmalı
                                25. Kişinin özellikleri çalıştığı şirkete uygun olmalı
                                26. Kişinin özellikleri yaptığı işe uygun olmalı
                                27. Hikayede tutarlılık olmalı
                                29. Kişinin çalıştığı yıl {job_year} olmalı
                                30. Hikaye sade yazılmış olmalı nesnel olmalı
                                31. Hikayede kişinin fraud yapıp yapmadığı belli olmamalı
                                """
            alterated_config = deepcopy(config)
            alterated_config["messages"][0]["content"] += extra_prompt
            response = create_response(**alterated_config)
            response_as_dict = json.loads(str(response.choices[0].message.content.strip()))
            print(response_as_dict)
            try:
                cursor.execute(f"INSERT INTO data(text, label) VALUES('{clear_punc(response_as_dict['text'])}', '{clear_punc(response_as_dict['label'])}');")
                connection.commit()
                count += 1
                print(f"{count} text created")
                continue
            except KeyError:
                pass
            except TypeError:
                pass
            try:
                cursor.execute(f"INSERT INTO data(text, label) VALUES('{clear_punc(response_as_dict['hikaye']['text'])}', '{clear_punc(response_as_dict['hikaye']['label'])}');")
                connection.commit()
                count += 1
                print(f"{count} text created")
                continue
            except KeyError:
                pass
            except TypeError:
                pass
            try:
                cursor.execute(f"INSERT INTO data(text, label) VALUES('{clear_punc(response_as_dict['hikaye'])}', '{clear_punc(response_as_dict['label'])}');")
                connection.commit()
                count += 1
                print(f"{count} text created")
                continue
            except BaseException:
                continue 
        except groq.BadRequestError:
            continue
    connection.close()


