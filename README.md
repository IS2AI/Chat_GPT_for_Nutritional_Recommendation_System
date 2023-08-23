# Chat_GPT_for_Nutritional_Recommendation_System

This repository contains the code, 50 different patient profiles and respective Chat-GPT responses on providing nutritional recommendations and sample diet plans. Patient profiles contain easy, medium and complex cases and various diseases. The project aims to evaluate the application of large language models for nutritional recommendation systems.


Responses were evaluated based on the personalization, consistency with evidence-based recommendations/ guidelines, and practicality. 

Cases were developed and evaluated in English, Russian, and Kazakh. To overcome the problem of model performance for underrepresented languages like Kazakh and Russian, an additional step of translating the cases to the English language before passing them to Chat-GPT has been done.

## Questions

The outputs for the following queries have been extracted: 

1. Provide dietary recommendations for this patient profile.
   
2. Give a specific diet plan for the day based on the patient profile using Central Asian food. 

## Data 

All sets of patient profiles and responses are located in the folder "Cases_and_Reponses".

cases_results.zip - contain the data in English language

cases_results_1.zip - contain the data in Russian language

cases_results_1_tr.zip - contain the data in Russian language with the translation before passing to the Chat-GPT

cases_results_2.zip - contain the data in Kazakh language

cases_results_2_tr.zip - contain the data in Kazakh language with the translation before passing to the Chat-GPT

Use gpt_response_extraction.py to extract the output using the Chat-GPT api.

## File structure

Each file contains the patient profiles, followed by the query and Chat-GPT output.

