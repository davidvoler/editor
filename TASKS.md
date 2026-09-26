# TASKS

## New Chat framework
- [v]  Get the framework to work client and server 
- History of chat should work
- The debug should be readable and can be used
- Some easy testing
- Maybe a mechanism to improve the cycle of prompts improvements - with AI 
## Improve results 
- Improve on the prompts
- Verify the prompt router  
## Editing & Adding exercises
- Edit Exercise 
- Add by exercise type 
### Question on how to proceed 

Q. let claude copy code from old repo
A. No, Design the new architecture

Q. I embarked on the cleanup project - Should I give it up and go back to the working version and improve it there?
A. Old code is not manageable - continue with the cleanup 

Q. When would it be time to pay for more expensive Claude subscription and continue with the code
A. When I have a good working architecture on the server side and I want to speed up the development cycles

Q. Should I keep auth for later
A. Yes

Q. Should we separate the data to multiple schemas 
- content - sentences and words 
- prompts - prompts request responses
- users - already in a specific schema 
A. Maybe - but it would be easy to do it at any time 
Q. Should a prompt options should be of type PromptsRequest 
 - this way the is almost no login on the server side
 - we should let the clint know somehow that it is an options 
  - but maybe we can prepare the entire request for the server
 - Words for example - the client should know where to load the words for the course/module 
- We do need for the client to do some composition when create a prompt request. Let's look at it and this what would be the best way

- course id
- module id 
- lesson id
- words 
- user prompt text

List of words - we could read it in the server side 
words - if we collect it on the server side it saves us extra read form the client and than send to server



### Ideas 
- let the user after chat rate
    - how well the AI understood what she wanted
    - The quality of the content

