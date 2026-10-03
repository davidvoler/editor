from fastapi import params

from utils.db import get_query_results, run_query
from models.course import Course
import json


async def get_courses() -> list[Course]:
    query = """
    SELECT * FROM courses
    """
    result = await get_query_results(query, {})
    if result:
        return [Course(**row) for row in result]
    return []

async def get_course(course_id: int) -> Course:
    query = """
    SELECT * FROM courses
    WHERE course_id = :course_id
    """
    params = {"course_id": course_id}
    result = await get_query_results(query, params)
    if result:
        return Course(**result[0])
    return Course()

async def update_course(course: Course) -> Course:
    query = """
    UPDATE courses
    SET lang = :lang,
        to_lang = :to_lang,
        user_id = :user_id,
        school = :school,
        title = :title,
        description = :description,
        course_options = :course_options,
        status = :status
    WHERE course_id = :course_id
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
        "status": course.status,
        "course_id": course.course_id
    }
    result = await get_query_results(query, params)
    if result:
        return Course(**result[0])
    return Course()

async def create_course(course: Course) -> Course:
    """Creates a new course in the database"""
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

async def delete_course(course_id: int) -> None:
    query = """
    UPDATE courses
    SET deleted = true
    WHERE course_id = :course_id
    """
    await run_query(query, {"course_id": course_id})
    