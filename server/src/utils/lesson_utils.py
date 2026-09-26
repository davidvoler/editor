from models.lesson import Lesson, LessonFull
from models.exercise import Exercise
from utils.db import get_query_results

async def create_lesson(lesson: Lesson) -> Lesson:
    sql = """
    INSERT INTO course.lesson (module_id, title, content, deleted, weight)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING lesson_id, module_id, title, content, deleted, weight
    """
    values = (lesson.module_id, lesson.title, lesson.content, lesson.deleted, lesson.weight)
    row = await get_query_results(sql, values)
    return Lesson(**row)

async def get_lesson_exercises(lesson_id: int) -> list[Exercise]:
    sql = """
    SELECT exercise_id, lesson_id, title, content, deleted, weight
    FROM course.exercise
    WHERE lesson_id = %s
    """
    values = (lesson_id,)
    rows = await get_query_results(sql, values)
    return [Exercise(**row) for row in rows]


async def get_lesson_full(lesson_id: int) -> LessonFull:
    sql = """
    SELECT lesson_id, module_id, title, content, deleted, weight
    FROM course.lesson
    WHERE lesson_id = %s
    """
    values = (lesson_id,)
    row = await get_query_results(sql, values)
    lesson = Lesson(**row)
    # Here you would typically retrieve related resources from the database
    exercise = await get_lesson_exercises(lesson_id)
    return LessonFull(lesson=lesson, exercises=exercise, resources=resources)


async def get_lesson(lesson_id: int) -> Lesson:
    sql = """
    SELECT lesson_id, module_id, title, content, deleted, weight
    FROM course.lesson
    WHERE lesson_id = %s
    """
    values = (lesson_id,)
    row = await get_query_results(sql, values)
    return Lesson(**row)

async def get_module_lessons(module_id: int) -> list[Lesson]:
    sql = """
    SELECT lesson_id, module_id, title, content, deleted, weight
    FROM course.lesson
    WHERE module_id = %s
    """
    values = (module_id,)
    rows = await get_query_results(sql, values)
    return [Lesson(**row) for row in rows]


async def get_module_lesson_full(module_id: int) -> list[LessonFull]:
    sql = """
    SELECT lesson_id, module_id, title, content, deleted, weight
    FROM course.lesson
    WHERE module_id = %s
    """
    values = (module_id,)
    rows = await get_query_results(sql, values)
    lessons_full = []
    for row in rows:
        lesson = Lesson(**row)
        exercise = await get_lesson_exercises(lesson.lesson_id)
        lessons_full.append(LessonFull(lesson=lesson, exercises=exercise))
    return lessons_full

async def update_lesson(lesson: Lesson) -> Lesson:
    sql = """
    UPDATE course.lesson
    SET module_id = %s, title = %s, content = %s, deleted = %s, weight = %s
    WHERE lesson_id = %s
    RETURNING lesson_id, module_id, title, content, deleted, weight
    """
    values = (lesson.module_id, lesson.title, lesson.content, lesson.deleted, lesson.weight, lesson.lesson_id)
    row = await get_query_results(sql, values)
    return Lesson(**row)

async def delete_lesson(lesson: Lesson) -> None:
    sql = """
    DELETE FROM course.lesson
    WHERE lesson_id = %s
    """
    values = (lesson.lesson_id,)
    await get_query_results(sql, values)