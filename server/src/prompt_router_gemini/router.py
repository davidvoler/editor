async def handle_user_chat(
    user_message: str, 
    context: ConversationContext,
    db_session
) -> dict:
    
    # Step 1: Infer intent using current state context
    deps = AgentDeps(context=context)
    route_result = await router_agent.run(user_message, deps=deps)
    action: CourseAction = route_result.output

    # Step 2: Route execution based on intent
    if action.intent == "GENERATE_VOCAB":
        # Resolve parameters from route or fallback state
        lang = action.target_language or context.target_language or "Spanish"
        count = action.word_count or 5
        topic = action.topic_or_context or "General Conversation"

        prompt = f"Generate {count} {lang} vocabulary words for the topic: '{topic}'."
        vocab_result = await vocab_agent.run(prompt)
        
        # Save to database
        # await save_vocab_to_db(db_session, context.active_module_id, vocab_result.output)

        # Update state context
        context.current_step = WorkStep.VOCAB_GENERATION
        # await update_session_state(db_session, context)

        return {
            "type": "vocab_created",
            "message": f"I've added {len(vocab_result.output.items)} words for '{topic}' to your module.",
            "data": vocab_result.output.model_dump()
        }

    elif action.intent == "GENERATE_EXERCISES":
        # Pull words from active module in DB if target word not specified
        # target_words = await get_module_words(db_session, context.active_module_id)
        
        prompt = f"Create {action.word_count or 3} exercises using current module vocabulary."
        quiz_result = await quiz_agent.run(prompt)

        # Save to database
        # await save_quizzes_to_db(db_session, context.active_module_id, quiz_result.output)

        context.current_step = WorkStep.EXERCISE_BUILDING

        return {
            "type": "exercises_created",
            "message": "I've generated new single-choice exercises for this lesson.",
            "data": quiz_result.output.model_dump()
        }

    else:
        return {
            "type": "chat_response",
            "message": "I can help you build courses, generate vocabulary, or create quizzes. What would you like to do next?"
        }