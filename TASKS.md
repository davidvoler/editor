# TASKS

## Overview

- Try to have a fully working app when a feature pack is complete


## Feature Pack 1 - Architecture

### Design the architecture 
- [v] prompts, prompts router etc  
- [v] Resultsstructure  
### Recreate the database structure 
- [v] Recreate all table and databases for course  
- [v] Create tables for prompts and prompt history
### Tasks, API and full process 
- [v] verify that the process works for an example action
##  Feature Pack 2 - Course editor pane 
- [v] words pane - load words from current modulw/course 
- [v] lesson page with exercises
    > Q: Separate page or a tab in the course pane? Decision: a "Lesson" tab next to Modules/Words, showing the context's lesson (else the module's first lesson).
- [v] words for this module mark used 
    > Q: How is a word "used"? Decision: new column course.exercise.word; saving/deleting an exercise recalculates course.words.used for its module (used = some exercise in the module practises the word).
- [v] manual editing of exercise
    > Q: Which fields does the form edit? Decision: type, word, question, answer, wrong options (options = {"incorrect": [...]}, like the AI SingleChoice shape), translation (sentence_alt1), explanation.
- [v] manual add exercise
##  Feature Pack 3 - Prompt context
- [] The prompt options should know the current course/module context
    - [] No words - suggest words
    - [] No exercise - suggest create exercise for words 
    - [] too many exercise for the current lesson - create the next lesson
    - [] too many lessons per module - suggest creating the next module, move words from current module to the next one    
## Feature Pack 3 - Video
- [] When the prompt contains a video url
    - [] start a video module 
    - [] suggest braking the video into 10 parts each 3 minutes length,  20 parts each 2 minutes length
    - [] extract words 
    - [] extract parts 
- [] generate exercises 
- [] select words and translations 
## Feature Pack 3 - Words in module course 
- [] Words appeared in sentences should be collected - suggest them as new words to learn
- []  


