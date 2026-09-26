from models.exercise import Exercise
from utils.db import get_query_results

async def create_exercise(exercise: Exercise) -> Exercise:
    sql = """
    INSERT INTO course.exercise (lesson_id, title, content, deleted, weight)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING exercise_id, lesson_id, title, content, deleted, weight
    """
    values = (exercise.lesson_id, exercise.title, exercise.content, exercise.deleted, exercise.weight)
    row = await get_query_results(sql, values)
    return Exercise(**row)

async def get_exercise(exercise_id: int) -> Exercise:
    sql = """
    SELECT exercise_id, lesson_id, title, content, deleted, weight
    FROM course.exercise
    WHERE exercise_id = %s
    """
    values = (exercise_id,)
    row = await get_query_results(sql, values)
    return Exercise(**row)

async def get_lesson_exercises(lesson_id: int) -> list[Exercise]:
    sql = """
    SELECT exercise_id, lesson_id, title, content, deleted, weight
    FROM course.exercise
    WHERE lesson_id = %s
    """
    values = (lesson_id,)
    rows = await get_query_results(sql, values)
    return [Exercise(**row) for row in rows]

async def update_exercise(exercise: Exercise) -> Exercise:
    sql = """
    UPDATE course.exercise
    SET lesson_id = %s, title = %s, content = %s, deleted = %s, weight = %s
    WHERE exercise_id = %s
    RETURNING exercise_id, lesson_id, title, content, deleted, weight
    """
    values = (exercise.lesson_id, exercise.title, exercise.content, exercise.deleted, exercise.weight, exercise.exercise_id)
    row = await get_query_results(sql, values)
    return Exercise(**row)

async def delete_exercise(exercise: Exercise) -> None:
    sql = """
    DELETE FROM course.exercise
    WHERE exercise_id = %s
    """
    values = (exercise.exercise_id,)
    await get_query_results(sql, values)


