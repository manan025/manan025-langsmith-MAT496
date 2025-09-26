# Foundation: Introduction to Agent Observability & Evaluations
Link: [https://academy.langchain.com/courses/intro-to-langsmith](https://academy.langchain.com/courses/intro-to-langsmith)

## Module 1

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
