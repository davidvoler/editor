from utils.db import get_query_results, run_query
from models.word import (Word, WordTranslationList, WordTranslation)


async def course_words(course_id:int, module_id:int|None = None) -> list[Word]: 
    # A word counts as used once it is assigned to a lesson.
    query = """
    SELECT word AS text, COALESCE(lesson_id, 0) > 0 AS used
    FROM course_words
    WHERE course_id = %(course_id)s AND deleted IS NOT TRUE
    """
    params = {"course_id": course_id}
    if module_id is not None:
        query += " AND module_id = %(module_id)s"
        params["module_id"] = module_id
    results = await get_query_results(query, params)
    return [Word(**row) for row in results]

async def save_words(lang:str, to_lang:str, course_id:int, module_id:int|None = 0, words: list[WordTranslation] = []):
    
    words_in_course = await course_words(course_id)
    words_dict = {word.word: word.translation for word in words_in_course}
    # insert only new words 
    query = """
    INSERT INTO course.words (course_id, module_id,lang, to_lang, word, translation)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    for word_translation in words:
        if word_translation.word in words_dict:
            continue
        params = (course_id, module_id,
                  lang, to_lang,
                  word_translation.word,
                  word_translation.translation)
        await run_query(query, params)

