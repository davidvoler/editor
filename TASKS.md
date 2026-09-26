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

Q. Try to let the Claude do the new code on his own - when we can read  the old code
- Do it with Claude from start 
- Do it with Claude by copying the old code
- Continue some manual work
a. So far when I let code write the server side on its own
- the results are finally working
- the code quality id bad
- the code becomes un accessible for me - only claude understands it
A. Do it from Start - clean and simple code
- I do let Claude write code on server side - But I am watching the changes. I am letting it write minimal code and sometime I have to redo it. I am kipping the server code owned by myself

Q. I embarked on the cleanup project - Should I give it up and go back to the working version and improve it there?
a. Clean code seems like a good idea
b. The new code is much more readable - and looks like it can easily grow 
c. avoiding large files on the server side


Q. When would it be time to pay for more expensive Claude subscription and continue with the code
A. When I have a good working architecture on the server side and I want to speed up the development cycles


Q. Should I keep auth for later
a. it would allow an easy development process 
b. We can add it from the old code later 
A. Yes


Q. Should we separate the data to multiple schemas 
- content - sentences and words 
- prompts - prompts request responses
- users - already in a specific schema 

