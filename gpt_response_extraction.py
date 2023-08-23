import os
import openai
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='kazakh', target='en')

cases = os.listdir('cases')
ready_cases = os.listdir('cases_results_2_tr')
ready_cases = [x[:-8] for x in ready_cases]
cases.sort()



for each_case in cases:
    #each_case = str(each_case)+'_1.txt'
    if each_case[-5]=='2':
        if each_case[:-4] not in ready_cases:
            #each_case = str(each_case) + '_0.txt'
            print(each_case)
            path = os.path.join('cases', each_case)
            with open(path) as f:
                contents = f.readlines()
                # print('\n'.join(contents))

            result = ''
            if each_case[-5]=='0':
                
                result = "Provide dietary recommendation for this patient profile. " + contents[0]
            if each_case[-5]=='1':
                original = "Предоставьте рекомендации по питанию для данного пациента. " + contents[0]
                result = translator.translate(original)
            if each_case[-5]=='2':
                original = "Oсы науқас/пациент профилі үшін тамақтану бойынша кеңес беріңіз. " + contents[0]
                result = translator.translate(original)
            #print(result)
            # Set openai.api_key to the OPENAI environment variable
            openai.api_key = "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"

            messages = [
                # system message first, it helps set the behavior of the assistant
                {"role": "system", "content": "You are a helpful assistant."},
            ]


            chat_completion = openai.ChatCompletion.create(
                    model="gpt-4", messages=[{"role": "user", "content": result}],max_tokens=800)
            response1 = chat_completion.choices[0].message.content
            print("ChatGPT:", response1)
            follow_up=''
            if each_case[-5]=='0':
                follow_up = result + " " + str(response1) + " " + "Give a specific diet plan for the day based on the patient profile using Central Asian food."
            if each_case[-5]=='1':
                follow_up = result + " " + str(response1) + " " + "Give a specific diet plan for the day based on the patient profile using Central Asian food."

                #follow_up = result + " " + str(response1) + " " + "Предложите конкретный план питания на день, основанный на профиле пациента с использованием центральноазиатской пищи."
                
            if each_case[-5]=='2':
                follow_up = result + " " + str(response1) + " " + "Give a specific diet plan for the day based on the patient profile using Central Asian food."

                # follow_up = result + " " + str(response1) + " " + "Пациент профиліне негізделген түрде Орта Азия тағамдарын қолдана отырып бір күндік тамақтанудың нақты жоспарын ұсыныңыз."
            
      
            messages.append({"role": "user", "content": follow_up},)
            chat_completion = openai.ChatCompletion.create(
                model="gpt-4", messages=messages, max_tokens=800)
            messages.append({"role": "assistant", "content": chat_completion.choices[0].message.content})

            response = chat_completion.choices[0].message.content
            #print("ChatGPT:", response)
            translator_back = GoogleTranslator(source='en', target='kazakh')
            first_part = translator_back.translate(response1)
            save_text = translator_back.translate(response)
            save_text = original + first_part + "Предложите конкретный план питания на день, основанный на профиле пациента с использованием центральноазиатской пищи." + save_text
            file = open("cases_results_2_tr/{}_gpt.txt".format(each_case[:-4]), "a")
            a = file.write(save_text)
            file.close()


