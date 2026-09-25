from models.exercise import Exercise

async def create_exercise(exercise: Exercise) -> Exercise:
    # Here you would typically save the exercise to a database
    # For now, we'll just return the exercise as is
    return exercise