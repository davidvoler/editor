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
- [v] The prompt options should know the current course/module context
    > Q: Where are options computed and when are they shown? Decision: the server computes them from the course's last saved context (GET /prompt/default_options, utils/context_options.py); the chat shows them at start and after every reply that has no options of its own. Unrecognised typed messages also get them.
    > Q: Thresholds? Decision: 10 exercises per lesson, 5 lessons per module, 5 words per exercise request (constants in utils/context_options.py).
    > Q: Offer one option or all that apply? Decision: the most specific step only (next module > next lesson > create exercises), plus "Suggest (more) words" when there are no unused words.
    - [v] No words - suggest words
    - [v] No exercise - suggest create exercise for words 
        > Q: How are exercises created? Decision: one AI call writes one exercise for each of up to 5 unused words, saved in the current lesson, which marks the words used.
        > Q: What is a single-choice exercise (the default)? Decision: a sentence that uses the word; the student picks the word's translation from 4 options (answer + 3 wrong translations). Fill in the blank (sentence with ___, the word is the answer) is generated only when prompt_type is fill_in_the_blank.
    - [v] too many exercise for the current lesson - create the next lesson
        > Q: What happens after creating it? Decision: "Lesson N+1" is added and becomes the current context, so new exercises go there.
    - [v] too many lessons per module - suggest creating the next module, move words from current module to the next one    
        > Q: Which words move? Decision: only words no exercise uses yet; used words stay with their module. The new "Module N+1" gets "Lesson 1" and becomes the current context.
## Feature Pack 3 - Video
- [v] When the prompt contains a video url
    > Q: How is a video link recognised? Decision: any YouTube URL in a typed chat message routes to the video router (main_router), whatever else the message says.
    > Q: Which subtitles? Decision: the course's learning language only; if missing, the reply lists the languages the video has.
    - [v] start a video module 
        > Q: Module title and storage? Decision: titled after the video (YouTube oEmbed), subtitles stored in course.video.raw_subtitles; the module becomes the current context with no lesson until it is split.
    - [v] suggest braking the video into 10 parts each 3 minutes length,  20 parts each 2 minutes length
        > Q: Fixed 10/20 parts? Decision: offer 3-minute and 2-minute parts, with the part count computed from the video's length. Each part becomes a lesson ("Part 1 (0:00-3:02)") whose description holds the part's subtitles; parts end on subtitle boundaries.
    - [v] extract words 
        > Q: Whole video or per part? Decision: one AI call per part ("Extract words and sentences from Part N"), up to 15 words with translations, saved to the module; the part's lesson.words records them and marks the part done.
    - [v] extract parts 
        > Q: What are "parts" here? Decision: cleaned-up sentences with translations (up to 10 per part), saved to course.sentences with the part's lesson_id, in the same AI call as the words.
- [v] generate exercises 
    > Q: New flow for video? Decision: reuse "Create exercises for N unused words"; extracting a part makes it the current lesson, so its exercises go into that part. Video modules never get "next lesson"/"next module" options.
- [v] select words and translations 
    > Q: How? Decision: tap a word in the Words tab to edit its translation or remove it (PUT /words/word, soft delete). Removed words are not suggested again.
    > Note: extracting a part took ~3.5 min on muse-glimmer, so the chat now waits up to 10 minutes for a reply.


## Feature Pack 4 - Ui improve improvements
- [] words panes - allow adding words manually - translation is optional
- [] Lessons pane - 
    - [v] adding exercises manually
        > Q: One form or one per type? Decision: one dialog whose fields follow the type. Single/multiple choice: sentence, 4 options by default with a checkbox for each correct one (single choice allows exactly one), add/remove options, translation, explanation. True/false: statement + True/False. Explanation: one multi-line text. Fill in the blank: question with ___ and the same option rows with exactly one correct option (the word for the blank), translation, explanation.
        > Q: How are several correct options stored? Decision: options = {"correct": [...], "incorrect": [...]}, answer = the first correct option. Exercises without options.correct (the AI's) read their answer as the one correct option. True/false stores answer "true"/"false".
    - [] Edit Exercise - you can correct any part of the exercise manually 
    - [v] Add options 
    - [v] delete options 
    - [] correct sentences and correct translation





## Feature Pack 20 - Words in module course 
- [] Words appeared in sentences should be collected - suggest them as new words to learn
- []  


