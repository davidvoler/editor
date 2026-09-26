from fastapi import HTTPException, Depends, APIRouter
from models.course import Course
from utils.db import get_query_results
from utils.permission import get_school_user
router = APIRouter()


@router.get("/courses",response_model=list[Course])
async def list_courses(lang: str | None = None, to_lang: str | None = None, school_user=Depends(get_school_user)):
    query = """SELECT * FROM course.course 
    WHERE (%s::varchar IS NULL OR lang = %s)
    AND (%s::varchar IS NULL OR to_lang = %s)
    AND deleted = false 
    AND user_id = %s
    AND school = %s
    ORDER BY updated_at DESC""" 
    results = await get_query_results(query, (lang, lang, to_lang, to_lang, school_user.user_id, school_user.school))
    res = [Course(**row) for row in results]
    return res

@router.get("/course",response_model=Course)
async def get_course(course_id: int, school_user=Depends(get_school_user)):
    query = """SELECT * FROM course.course 
        WHERE deleted = false 
        AND user_id = %s
        AND school = %s
        AND course_id = %s
        """ 
    results = await get_query_results(query, (school_user.user_id, school_user.school, course_id))
    if not results:
        raise HTTPException(status_code=404, detail="Course not found")
    return Course(**results[0])

@router.post("/course")
async def create_course(course: Course, school_user=Depends(get_school_user)):
    sql = """
        INSERT INTO course.course (lang, to_lang, user_id, school, level)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING * 
        """
    results = await get_query_results(sql, 
                                      (course.lang, course.to_lang, school_user.user_id, school_user.school, course.level))
    if not results:
        raise HTTPException(status_code=400, detail="Failed to create course")
    res = [Course(**row) for row in results]
    return res[0]

@router.put("/course")
async def update_course( course: Course, school_user=Depends(get_school_user)) -> Course :
    """Updates a course"""
    sql = """
        UPDATE course.course
        SET lang = %s,
            to_lang = %s,
            level = %s
            title = %s,
            deleted = %s,
        WHERE course_id = %s
        AND user_id = %s
        AND school = %s
        RETURNING *
    """
    results = await get_query_results(sql, 
                                      (course.lang, course.to_lang, course.level, course.title, course.deleted, course.course_id, school_user.user_id, school_user.school))
    if not results:
        raise HTTPException(status_code=400, detail="Failed to update course")
    res = [Course(**row) for row in results]
    return res[0]

@router.delete("/course")
async def delete_course(course: Course, school_user=Depends(get_school_user))->dict:
    """Deletes a course"""
    sql = """
        DELETE FROM course.course
        WHERE course_id = %s
        AND user_id = %s
        AND school = %s
        RETURNING *
    """
    results = await get_query_results(sql, (course.course_id, school_user.user_id, school_user.school))
    if not results:
        raise HTTPException(status_code=400, detail="Failed to delete course")
    return {"status": "success"}