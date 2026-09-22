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
    - S

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
- course list page 

##### Backend #####
A user can write anything in the chat 
Prompt Router - what do the user wants from the chat 

                                       _________________
                                       | Prompt Router |
                                       -----------------
                                              |
     _________________    _______________   _______________    ________________
    | Exercise Router |  | Module Router |  | Lesson Router | | Course Router  |
     -----------------    ---------------   ---------------    ----------------                          

     _________________    _______________   _______________    ________________
    | Choice Exercise  |  |Explanation |   | Identify.    |   |Course Router  |
     -----------------    ---------------   ---------------    ----------------   


How to figure out what did the user mean? 
- simply by 


### Gemini suggestion for Implementing Multi stage course creation  
1. Architectural Strategy: The Agentic State Machine
To move to a free-text process without breaking your data flow, treat the chat interface as a stateful conversation where the AI acts as a Course Designer Assistant.

Maintain State: Keep track of where the author is in the module creation process (e.g., STATE: AWAITING_MODULE_TOPIC, STATE: SELECTING_VOCABULARY, STATE: GENERATING_LESSON_1).

Hidden Function Calling (Tools): When the user types freely (e.g., "Let's make an A2 Japanese lesson about ordering food"), your chat model should parse the intent and call your existing backend generation prompts under the hood.

Structured Previews: Return the results of those backend prompts as interactive UI cards or clean markdown previews in the chat, followed by a prompt asking for approval or edits.

2. Designing the Step-by-Step Free-Text Flow
Here is how you can map your required steps into a natural conversation flow:

Step 1: Initialization & Vocabulary Suggestion
User Input (Free text): "I want to create an A2 module about ordering food at a restaurant."

AI Action: The LLM recognizes the goal and triggers your vocabulary/sentence generation prompt behind the scenes.

AI Response:

Great! For an A2 module on restaurant ordering, here are 3 suggested word and sentence sets to start with:

Set A (Polite Requests): 注文する (chuumon suru - to order), ... [Preview]

Set B (Menu items & Diet): アレルギー (arerugii - allergy), ... [Preview]

Set C (Paying the bill): お会計 (o-kaikei - bill), ... [Preview]

Would you like to use one of these sets, mix and match, or provide your own words?

Step 2: Lesson Generation & Iteration
User Input: "Let's go with Set A, but add the word 'menu'."

AI Action: The LLM updates the working vocabulary list, saves a draft module state, and triggers your lesson/sentence/quiz generation endpoint for Lesson 1.

AI Response: Displays the generated sentences, quizzes, and explanation exercises for Lesson 1.

Here is Lesson 1 based on your selection. (Preview of sentences, multiple-choice quizzes, and explanation exercise).

How does this look? You can approve it to move to Lesson 2, or tell me what to change (e.g., "Make the quizzes a bit harder").

3. Implementation Blueprint for Your Backend
To make this seamless, adjust your backend architecture:

Intent Parser Layer: A lightweight system prompt that reviews the user's free text and determines if they are:

Giving feedback/edits to current content.

Approving content to move to the next step.

Asking a completely new question.

Deterministic Fallback: If the user's free text is ambiguous (e.g., "Hmm, make it better"), the AI should ask a clarifying question rather than guessing which endpoint to fire.

Would you like to explore how to design the system prompt for the orchestrator layer to handle these state transitions?


### Prompt Router

                          ┌──────────────────────────┐
                          │   User Message + State   │
                          └────────────┬─────────────┘
                                       │
                                       ▼
                          ┌──────────────────────────┐
                          │   PydanticAI Router      │
                          │ (Classification Engine)  │
                          └────────────┬─────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │ [Action = Vocab]             │ [Action = Quizzes]           │ [Action = Ambiguous]
        ▼                              ▼                              ▼
┌──────────────┐               ┌──────────────┐               ┌──────────────┐
│ Vocab Agent  │               │ Quiz Agent   │               │ Direct Chat  │
│ (Your Prompt)│               │ (Your Prompt)│               │ + Options    │
└───────┬──────┘               └───────┬──────┘               └───────┬──────┘
        │                              │                              │
        └──────────────────────────────┼──────────────────────────────┘
                                       ▼
                          ┌──────────────────────────┐
                          │ Output to Client + DB    │
                          └──────────────────────────┘

                          