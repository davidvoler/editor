from models.lesson import Lesson

async def create_lesson(lesson: Lesson) -> Lesson:
    # Here you would typically save the lesson to a database
    # For now, we'll just return the lesson as is
    return lesson

