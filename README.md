# Generative AI Orchestration
This repository is part of a live streaming series. In this specific part of the series we are orchestrating Generative AI applications using Google Cloud Workflows. 

**We continue working on this during the next livestreams**

📺 Get Ready to Code and Laugh Live! Join me every Friday* from 10 - 11:30 AM CET / 8 - 10:30 UTC for the Coding GenAI Applications Live Stream!

## Previous live streams
If you want to follow along you can watch the recordings. 

1. https://youtube.com/live/gAxQst87vA4

## Usage

### Deploy the workflow
```
gcloud workflows deploy recipe --source=recipe.yaml
```

### Run the workflow
```
gcloud workflows run recipe --data='{"recipePrompt":"generate a vegan BBQ recipe"}'
```