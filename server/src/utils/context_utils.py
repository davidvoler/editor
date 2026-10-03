from models.context import PromptsContext
from utils.db import get_query_results
from utils.module_utils import create_course
from utils.lesson_utils import create_lesson
from utils.words_utils import course_words

async def save_context(context: PromptsContext) -> PromptsContext:
    sql = """
    INSERT INTO prompts_context (course_id, module_id, lesson_id)
    VALUES (%s, %s, %s)
    returning *
    """
    params = (context.course_id, context.module_id, context.lesson_id)
    results = await get_query_results(sql, params)
    return PromptsContext(**results[0])

async def get_or_create_context(course_id: int, module_id: int = 0) -> PromptsContext:
    if module_id == 0:
        whr = "course_id = %s AND module_id = %s"
    else:
        whr = "course_id = %s"
    sql = f"""SELECT * FROM prompts_context WHERE {whr} 
    order by context_id desc
    limit 1     
    """
    params = (course_id, module_id) if module_id > 0 else (course_id,)
    results = await get_query_results(sql, params)
    if results:
        row = results[0]
        pc = PromptsContext(**row)
        if pc.module_id > 0 and pc.lesson_id >0:
            pc.words = await course_words(course_id=pc.course_id, module_id=pc.module_id)
            return pc
    else:
        pc = PromptsContext(course_id=course_id, module_id=module_id)
    if pc.module_id == 0:
        module = await create_course(course_id=pc.course_id)
        pc.module_id = module.module_id
    if pc.lesson_id == 0:
        lesson = await create_lesson(course_id=pc.course_id, module_id=pc.module_id)
        pc.lesson_id = lesson.lesson_id
    pc.words = await course_words(course_id=pc.course_id, module_id=pc.module_id)
    return await save_context(pc)


