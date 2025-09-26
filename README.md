# Foundation: Introduction to Agent Observability & Evaluations
Link: [https://academy.langchain.com/courses/intro-to-langsmith](https://academy.langchain.com/courses/intro-to-langsmith)

## Module 1
While I have tried to make several changes, the base model remains highly unstable as I have tried to focus more on Langsmith
rather than working on improving the overall output of the model itself.

### Lesson 1
Link: [Lesson1.ipynb](module1/lesson1.ipynb)\
Learnt how to make RAG models traceable for the requests to be visible on the langsmith platform. Also learnt how to add metadata to filter and add more information on the platform alongside the essential API call information.

Tweaks:
- Changed the RAG model to be instead a cold mail generator for research opportunities.
- Added function decorator to ensure all the requests to models are traceable on the langsmith platform.

### Lesson 2
Link: [Lesson2.ipynb](module1/lesson2.ipynb)\
Learnt how to classify runs, and use langchain with tools.

Tweaks:
- Reimplemented for Claude SDK (not compatible with OpenAI type API)
- Added metadata to make it relevant
- Added another tool to get dummy crime rate of a location

### Lesson 3
Link: [Lesson3.ipynb](module1/lesson3.ipynb)

Tweaks:
- Changed prompts to suit the overall theme
- Edited the code for claude
- Did the tasks accordingly as mentioned in the video
- Worked on the optional part mentioned in the notebook provided in resources

### Lesson 4
Link: [Lesson4.ipynb](module1/lesson4.ipynb)

Tweaks:
- Model used: Claude 3.5 Haiku 
Did not change the prompts as the objective was to see conversational threads on the langsmith platform