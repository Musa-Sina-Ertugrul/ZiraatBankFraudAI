import google.generativeai as genai
import sqlite3
import json
import pandas as pd
import numpy as np
from copy import deepcopy
genai.configure(api_key="AIzaSyAPc4wK9B1iwA7o-alIZtOi_jQrzJ-az7E")

model = genai.GenerativeModel('gemini-1.5-flash',generation_config={"response_mime_type": "application/json"})

prompt = "Bana not fraud detection hikayesi yazman lazım: \
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
            job_year = abs(np.random.randint(18,age)-18)
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
                                31. Hikaye uzun olmalı
                                32. Hikayede alengirli olaylar olması lazım
                                """
            alterated_config = deepcopy(prompt)
            alterated_config += extra_prompt
            response = model.generate_content(alterated_config)
            response_as_dict = json.loads(str(response.text.strip()))
            print(response_as_dict)
            cursor.execute(f"INSERT INTO data(text, label) VALUES('{clear_punc(response_as_dict['text'])}', '{clear_punc(response_as_dict['label'])}');")
            connection.commit()
            count += 1
            print(f"{count} text created")
        except BaseException:
            continue
    connection.close()