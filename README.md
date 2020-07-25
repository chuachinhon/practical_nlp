#  Practical NLP 

This series of notebooks is aimed at helping fellow NLP enthusiasts think about applying new tools and techniques to practical tasks. My goal is to keep the code and work flow simple, and focus on an actual use case.

# PART 2: Text Summarisation Of Short and Long Speeches Using Hugging Face's Pipeline 
![](https://cdn-images-1.medium.com/max/2400/1*KMA8dQRCoIh_nEJsgYUkQw.jpeg)

Text summarization is a far less common downstream NLP task compared to, say, classification or sentiment analysis. The resources and time needed to do it well are considerable. Hugging Face's transformers pipeline, however, has made the first part of the task much faster and efficient. More time can then be devoted to analysing the results, and/or building your own benchmarks for assessing the summaries. This notebook incorporates minor work-arounds to handle longer speeches, which is trickier to handle due to sequence length limits in the transformer models/pipeline.


# PART 1: Sentiment Analysis Of Political Speeches Using Hugging Face's Pipeline

![](https://images.squarespace-cdn.com/content/v1/5d4b9c1c1d80190001a3d344/1592662833817-7Y70EZ5PEGYRCVI8ITBF/ke17ZwdGBToddI8pDm48kAnkJg-YzxtCygogjUK3bbh7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z4YTzHvnKhyp6Da-NYroOW3ZGjoBKy3azqku80C789l0haypLsn6iFkXbd5QrnyzAEumsUYJT3wYflNPYrPZQnj8QjtpZFrO1KmHo-026JVHw/pm_june7_annon.jpg?)

Sentiment analysis is a fairly common task in machine learning. Hugging Face's new pipeline feature, however, has made it incredibly easy to use a transformer-based model for this task. In this notebook, I'll explore how the HF pipeline can be used together with Plotly and Google Sheets to produce a detailed analysis of one speech, as well as how the same technique can be adapted for longer-term analysis of political speeches on one topic, or those by a common group of speakers.

Fuller background in this post [here](https://www.analytix-labs.com/insights/cb-speeches).

---
