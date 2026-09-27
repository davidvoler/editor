from utils.db import get_query_results
from models.word import Word


async def course_words(course_id:int, module_id:int|None = None) -> list[Word]: 
    query = "SELECT * FROM words WHERE course_id = :course_id"
    params = {"course_id": course_id}
    if module_id is not None:
        query += " AND module_id = :module_id"
        params["module_id"] = module_id
    results = await get_query_results(query, params)
    return [Word(**row) for row in results]