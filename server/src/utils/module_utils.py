from models.module import Module, ModuleFull
from utils.db import get_query_results
from utils.lesson_utils import get_module_lesson_full


async def create_module(module: Module) -> Module:
    sql = """
    INSERT INTO course.module (course_id, title, description, deleted, weight)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING module_id, course_id, title, description, deleted, weight
    """
    values = (module.course_id, module.title, module.description, module.deleted, module.weight)
    row = await get_query_results(sql, values)
    return Module(**row)

async def get_module(module_id: int) -> Module:
    sql = """
    SELECT module_id, course_id, title, description, deleted, weight
    FROM course.module
    WHERE module_id = %s
    """
    values = (module_id,)
    row = await get_query_results(sql, values)
    return Module(**row)

async def get_module_full(module_id: int) -> ModuleFull:
    module = await get_module(module_id)
    lessons = await get_module_lesson_full(module_id)
    return ModuleFull(module=module, lessons=lessons)


async def get_course_modules(course_id: int) -> list[Module]:
    sql = """
    SELECT module_id, course_id, title, description, deleted, weight
    FROM course.module
    WHERE course_id = %s
    """
    values = (course_id,)
    rows = await get_query_results(sql, values)
    return [Module(**row) for row in rows]

async def update_module(module: Module) -> Module:
    sql = """
    UPDATE course.module
    SET title = %s, description = %s, deleted = %s, weight = %s
    WHERE module_id = %s
    RETURNING module_id, course_id, title, description, deleted, weight
    """
    values = (module.title, module.description, module.deleted, module.weight, module.module_id)
    row = await get_query_results(sql, values)
    return Module(**row)


async def delete_module(module: Module) -> None:
    sql = """
    DELETE FROM course.module
    WHERE module_id = %s
"""
    values = (module.module_id,)
    await get_query_results(sql, values)    