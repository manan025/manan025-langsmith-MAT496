# Foundation: Introduction to Agent Observability & Evaluations
Link: [https://academy.langchain.com/courses/intro-to-langsmith](https://academy.langchain.com/courses/intro-to-langsmith)

## Module 1
While I have tried to make several changes, the base model remains highly unstable as I have tried to focus more on Langsmith
rather than working on improving the overall output of the model itself.

### Lesson 1
Link: [Lesson1.ipynb](module1/lesson1.ipynb)\
Learnt how to make RAG models traceable for the requests to be visible on the langsmith platform. Also learnt how to add metadata to filter and add more information on the platform alongside the essential API call information.

Tweaks and learnings:
- Changed the RAG model to be instead a cold mail generator for research opportunities.
- Added function decorator to ensure all the requests to models are traceable on the langsmith platform.

### Lesson 2
Link: [Lesson2.ipynb](module1/lesson2.ipynb)\
Learnt how to classify runs, and use langchain with tools.

Tweaks and learnings:
- Reimplemented for Claude SDK (not compatible with OpenAI type API)
- Added metadata to make it relevant
- Added another tool to get dummy crime rate of a location

### Lesson 3
Link: [Lesson3.ipynb](module1/lesson3.ipynb)

Tweaks and learnings:
- Changed prompts to suit the overall theme
- Edited the code for claude
- Did the tasks accordingly as mentioned in the video
- Worked on the optional part mentioned in the notebook provided in resources

### Lesson 4
Link: [Lesson4.ipynb](module1/lesson4.ipynb)

Tweaks and learnings:
- Model used: Claude 3.5 Haiku 

Did not change the prompts as the objective was to see conversational threads on the langsmith platform

## Module 2

Link: [module2](module2)

### Lesson 1
Link: [Lesson1.ipynb](module2/lesson1.ipynb)

Tweaks and learnings:
- Tried out various options within the langsmith dataset and evaluation section to add and modify examples in dataset

### Lesson 2
Link: [Lesson2.ipynb](module2/lesson2.ipynb)

Tweaks and learnings:
- Basic understanding of how LLM-as-a-judge works
- Parsed the output from claude in a certain way because it does not support custom output type
- Explored langsmith platform to use the Auto Evaluate feature
- Used claude 3.5 Haiku to assess the RAG model programmatically and through web UI

### Lesson 3
Link: [Lesson3.ipynb](module2/lesson3.ipynb)

Tweaks and learnings:
- Understood the overall process of improving any model
- Compared state-of-the-art Claude Sonnet 4.5 and Claude 3.5 Haiku
- Used the existing example in langsmith course for simplicity
- Learnt about different ways to use langsmith's experiment option

### Lesson 4
Performed solely on the langsmith platform

Tweaks and learnings:
- Learnt options like charts and filters to explore the experiments runs
- Options in UI to ensure better readability and getting individual runs
- Compared experiments side by side

### Lesson 5
Link: [lesson5.ipynb](module2/lesson5.ipynb)

Tweaks and learnings:
- Judged two models side by side with dummy data
- The final output is given as a link and can be accessed on the langsmith UI
- Easier to compare multiple outputs

### Lesson 6
Link: [lesson6.ipynb](module2/lesson6.ipynb)

Tweaks and learnings:
- JSON parsing to ensure claude works with the rest of the code
- Implemented the code for claude
- Understood how f1 and other metrics work and found for the example dataset cloned from langsmith
- Used summary evaluator to ensure that the metric is found on running the evaluator on the entire dataset instead of individual

## Module 3

### Lesson 1
Link: [lesson1.ipynb](module3/lesson1.ipynb)

Tweaks and learnings:
- Learnt how to compare different models on langsmith playground
- Compared different models
- Used tool calling and output schema options
- Uploaded dataset programmatically and compared reference output against the model output

### Lesson 2
Link: [lesson2.ipynb](module3/lesson2.ipynb)

Tweaks and learnings:
- Used prompt hub
- Added variables to prompts programmatically
- Learnt how to commit prompts on langchain
- Programmatically uploaded prompts to langchain
- Converted code for Claude

### Lesson 3
Link: [lesson3.ipynb](module3/lesson3.ipynb)

Tweaks and learnings:
- Uploading and evaluating on prompts from database at once
- Evaluation of responses obtained from model against reference outputs
- Programmatically accessed prompt and changed variables within the prompt to get desired output
