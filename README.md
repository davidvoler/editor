# Editor

This project is an editor for language course 
I have decided replace a single server for student, school management and editor



### Editor/UI
I am re-designing the editor UI 
- Simpler 
- More AI driven - so far we did it in baby steps now we can do create a module - and it will do each steps
- Maybe we do 



### Questions

I want the ui for creating a course or a module look more like claude code or any agent 
- You can type free text 
- Your text is that translated to actions 
    - create exercises of different types
    - choose words for lesson
    - create explanations 
    - break them into lessons 
    - create a module based on a video
The AI should return options 
- suggests words for model - say you have 3 lists and you choose one of them, or create your own list
- suggest explanations for each lesson

### Prompt router - self planned 

- PromptRouter
    - Try to understand user  
    - if you do not succeed 
        - pose question
    - if data is missing 
        - pose show options 

- CoursePrompts
    - figure out the mandatory fields from the prompt
    - offer more options to the user - basic list + show more 
    - create a course 

- Module Prompts 
    - just like course - ask the user for some options 

- ExercisePrompt
    - We have multiple exercises types we want to understand what type of exercise to create
    - We have the module data and know what was created so far and what is needed

- Lesson prompt?
    - do we need a prompts for that stage - is lesson not only a bunch of exercises
    - can we group exercises into lesson later

- VideoPrompt 
    - Show some options 
    - break into sections
    - break sections into parts of speech 
    - generate quizzes

- Utitlities
    - save prompts request for debug
    - handle errors 


#### Architectural design ####
- Easily improve prompts 
    - extended
    - test
    - improve 
- Prompts should have 
    - params for the prompts  
        - word
        - free text
    - system params oc course/module level
        - language 
        - to language 
        - max number of words in sentence
        - free text extending the system prompt


##### UI/UX #####
A simple chat window with not need to have create course/create module button 
We are always in a context of a course/module whoever we change from button interface to chat interface

Pages 
- Chat page - When we are in course context we see the course/module in a tab 
    - the good elements about using chat to create the course are 
        - it is impressive - fully modern AI design
        - it is great for setting specific course related parameters
- Course list page 
- Prompt Monitor

Q. Where do we show the tasks that are not yet completed 
    a. in chat window (and we can continue to the next prompt)
    b. in the context 
        - if we are creating a new module - we show it in the module tab
        - if we create exercises for words - show it in the lesson/exercises

The chat window should have the following structure 
- 2 panes 
    - chat pane
    - course/module pane 
    - review pane 

###### Ideas ######
- add suggestion to a module/course 
    - too many exercises in a lesson
    

##### Backend #####
A user can write anything in the chat 
Prompt Router - what do the user wants from the chat 

                                       _________________
                                       | Prompt Router |
                                       -----------------
                                              |
     _________________    _______________   _______________    ________________    ________________
    | Exercise Router |  | Module Router |  | Lesson Router | | Course Router  |  | Video Router  |  
     -----------------    ---------------   ---------------    ----------------    ----------------                        

     _________________    _______________    _______________    ________________
    | Choice Exercise |  |Explanation  |   | Identify.    |   |Course Router  |
     -----------------    ---------------    ---------------    ----------------   


How to figure out what did the user mean? 
- keywords
- let AI decide
- Show options 

Context
- Course context
- Module context
- Options selected context with original prompt

Logging 
It would be great to save the prompt data into a database
- review the process
- get context for next time with start - go exactly where you left
- improve prompts 


#### Client Server Communication ####
[Client]
- load context (per course, empty if no context)
- Send prompt
    - Prompt Text
    - Context
[Server]
- Identify type of prompt
- returns Prompt Response
    - task id if a long running task - we will poll on completed tasks and mark them as done, running, failed
    - results if the prompt can be answered without waiting
    - options - if we are not sure what the user wanted - if the current context 
    - description to display prompt window
    - result type 
[Client]
    Result type?
        - new course 
            - create the course elements in the course pane 
        - new module 
            - Create the module in the module pane
        - Task ID 
            - show progress spinner
            - poll for task results 
            - reload module when task completes
        - Options 
            - show the options in a clickable manner
            - offer the normal chat to suggest something else





endpoint
POST /prompt
GET /prompt/status  - list of task ids for the current module/course
GET /course/prompt_context - where we have left last time in the course
GET /module/prompt_context 
GET /course
GET /module_full includes all lesson and exercises 


simplified version 

GET /course -  course data
GET /context (course_id, module_id) - last saved context 
GET /module_full - context, module, module element
GET /tasks/status



Questions:
Q. when can the user send the next prompt?
    1. when last prompts has a response - async 
    2. when pending tasks are completed - sync - do not run a new task before older tasks are completed







### Gemini suggestion for Implementing Multi stage course creation  

### Prompt Router

                          ┌──────────────────────────┐
                          │   User Message + State   │
                          └────────────┬─────────────┘
                                       │
                                       ▼
                          ┌──────────────────────────┐
                          │   PydanticAI Router      │
                          └────────────┬─────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │ 
        ▼                              ▼                              ▼
┌──────────────┐               ┌──────────────┐               ┌──────────────┐
│ Exercise     │               │ Course.      │               │ Module       │
│ Router.      │               │ Router.      │               │ Router.      │
└───────┬──────┘               └───────┬──────┘               └───────┬──────┘
        │                              │                              │
        └──────────────────────────────┼──────────────────────────────┘
                                       ▼
                          ┌──────────────────────────┐
                          │ Return Response.         │ [Data], [TaskID],[Options]
                          └──────────────────────────┘
                                      |
                                      ▼
                          ┌──────────────────────────┐    ┌──────────────────────────┐
                          │ Run Tasks.               │ -> │ Notify task complete     │
                          └──────────────────────────┘    └──────────────────────────┘
                                      |
                                      ▼
                          ┌──────────────────────────┐
                          │ Save to DB               │
                          └──────────────────────────┘


                          