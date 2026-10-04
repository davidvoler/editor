from utils.db import get_query_results
from models.word import Word


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