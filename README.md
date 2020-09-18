#  Practical NLP 

This series of notebooks is aimed at helping fellow NLP enthusiasts think about applying new tools and techniques to practical tasks. My goal is to keep the code and work flow simple, and focus on an actual use case.

# PART 5: Fine Tune Transformer Model On Custom Dataset

[Notebook5.0](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/5.0_finetune_distilbert_colab_cch.ipynb) is an adaptation of my [new repo](https://github.com/chuachinhon/transformers_state_trolls_cch) on using transformer models to detect state trolls on Twitter. I reckon many may not be interested in the subject matter, so I only ported over the Colab notebook for fine tuning with custom dataset for folks who are specifically looking for examples like this.

This notebook took about 5.5 hours to run on a Colab Pro account on TPU and "high-RAM" settings. It could go slower or faster depending on your set-up. The datasets needed - train_raw.csv and validate.csv - are in the [data folder](https://github.com/chuachinhon/practical_nlp/tree/master/data) of this repo.


# PART 4: Batch Machine Translation with Hugging Face and MarianMT
![](https://miro.medium.com/max/1400/1*hYerl3LtK-hgDxqeYgmr5A.jpeg)
Machine translation doesn't generate as much excitement as other emerging areas in NLP, but recent advances have opened up interesting new possibilities in this space. Over three short notebooks, I'll demo a simple workflow for using Hugging Face's version of MarianMT to:
- [translate 3 English speeches of varying lengths to Chinese](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/4.0_english_to_chinese_translate.ipynb)
- [translate 5 English news stories on Covid-19 (under 500 words) to Chinese](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/4.1_english_to_chinese_news.ipynb)
- [translate 3 Chinese speeches to English](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/4.2_chinese_to_english_translate.ipynb)

Results from neural machine translation models are not (yet) as artful or precise as those by a skilled human translator. But they get 60% or more of the job done, in my view. Depending on your use case, that could be a huge time saver.

Fuller background and details in this Medium post [here](https://medium.com/@chinhonchua/lost-in-machine-translation-3b05615d68e7?sk=4006eab9717ef5381c50e923fe2b814d).


# PART 3: Beginner's Guide To Building A Singlish AI Chatbot 
![](https://miro.medium.com/max/2000/1*dStowlpqDyRipF3JIvVV0Q.jpeg)
AI text generation is one of the most exciting fields in NLP, but also a daunting one for beginners. These 4 notebooks aim to speed up the learning process for newcomers by combining and adapting various existing tutorials into  a practical end-to-end walkthrough with notebooks and sample data for a conversational chatbot that can be used in an interactive app.
 - [3.0](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/3.0_data_prep_cch.ipynb): Data preparation
 - [3.1](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/3.1_finetune_bot_cch.ipynb): Fine tuning a pretrained DialoGPT-medium model on Colab
 - [3.2](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/3.2_dash_chat_app_cch.ipynb): Testing the model's performance on an interactive Dash app
 - [3.3](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/3.3_aitextgen_cpu_cch.ipynb): CPU alternative to text generation 

Fuller background and details in this Medium post [here](https://medium.com/@chinhonchua/beginners-guide-to-building-a-singlish-ai-chatbot-7ecff8255ee?sk=ea4f20a44a73321fad8b592d3ede6243).

# PART 2: Text Summarisation Of Short and Long Speeches Using Hugging Face's Pipeline 
![](https://miro.medium.com/max/2000/1*KMA8dQRCoIh_nEJsgYUkQw.jpeg)

Text summarization is a far less common downstream NLP task compared to, say, classification or sentiment analysis. The resources and time needed to do it well are considerable. Hugging Face's transformers pipeline, however, has made the first part of the task much faster and efficient. More time can then be devoted to analysing the results, and/or building your own benchmarks for assessing the summaries. This [notebook](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/2.0_speech_summary_cch.ipynb) incorporates minor work-arounds to handle longer speeches, which is trickier to handle due to sequence length limits in the transformer models/pipeline.

Fuller background and details in this Medium post [here](https://towardsdatascience.com/practical-nlp-summarising-short-and-long-speeches-with-hugging-faces-pipeline-bc7df76bd366).


# PART 1: Sentiment Analysis Of Political Speeches Using Hugging Face's Pipeline

![](https://images.squarespace-cdn.com/content/v1/5d4b9c1c1d80190001a3d344/1592662833817-7Y70EZ5PEGYRCVI8ITBF/ke17ZwdGBToddI8pDm48kAnkJg-YzxtCygogjUK3bbh7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0haypLsn6iFkXbd5QrnyzAEumsUYJT3wYflNPYrPZQnj8QjtpZFrO1KmHo-026JVHw/pm_june7_annon.jpg?)

Sentiment analysis is a fairly common task in machine learning. Hugging Face's new pipeline feature, however, has made it incredibly easy to use a transformer-based model for this task. In this [notebook](https://github.com/chuachinhon/practical_nlp/blob/master/notebooks/1.0_speech_sentiment_cch.ipynb), I'll explore how the HF pipeline can be used together with Plotly and Google Sheets to produce a detailed analysis of one speech, as well as how the same technique can be adapted for longer-term analysis of political speeches on one topic, or those by a common group of speakers.

Fuller background in this post [here](https://www.analytix-labs.com/insights/cb-speeches).

---
