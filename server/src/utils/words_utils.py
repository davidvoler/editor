from utils.db import get_query_results, run_query
from models.word import (Word, WordTranslationList, WordTranslation)


async def course_words(course_id:int, module_id:int|None = None) -> list[Word]: 
    # One row per word; a word repeated in the table counts as used when any copy is,
    # and keeps the translation it was first saved with.
    query = """
    SELECT word AS text, bool_or(COALESCE(used, false)) AS used,
        COALESCE((array_agg(translation ORDER BY word_id))[1], '') AS translation
    FROM course.words
    WHERE course_id = %(course_id)s AND deleted IS NOT TRUE
    """
    params = {"course_id": course_id}
    if module_id is not None:
        query += " AND module_id = %(module_id)s"
        params["module_id"] = module_id
    query += " GROUP BY word ORDER BY min(weight), min(word_id)"
    results = await get_query_results(query, params)
    return [Word(**row) for row in results]

async def save_words(lang:str, to_lang:str, course_id:int, module_id:int|None = 0, words: list[WordTranslation] = []):
    
    known_words = {word.text for word in await course_words(course_id)}
    # insert only new words 
    query = """
    INSERT INTO course.words (course_id, module_id,lang, to_lang, word, translation)
    VALUES (%s,%s,%s,%s,%s,%s)
    """
    for word_translation in words:
        if word_translation.word in known_words:
            continue
        known_words.add(word_translation.word)
        params = (course_id, module_id,
                  lang, to_lang,
                  word_translation.word,
                  word_translation.translation)
        await run_query(query, params)

