from utils.db import get_query_results
from models.course import Course
import json

async def create_course(course: Course) -> Course:
   
    # Implement the logic to create a course in the database
    query = """
    INSERT INTO courses (lang, to_lang, user_id, school, title, description, course_options, status)
    VALUES (:lang, :to_lang, :user_id, :school, :title, :description, :course_options, :status)
    RETURNING *
    """
    params = {
        "lang": course.lang,
        "to_lang": course.to_lang,
        "user_id": course.user_id,
        "school": course.school,
        "title": course.title,
        "description": course.description or '',
        "course_options": json.dumps(course.course_options or {}),
        "status": course.status
    }
    result = await  get_query_results(query, params)
    if result:
        return Course(**result[0])
    return Course()