import 'package:flutter_test/flutter_test.dart';

import 'package:editor/features/modules/data/module.dart';

void main() {
  test('parses a module lesson with its exercises from the server', () {
    final lesson = Lesson.fromJson({
      'lesson': {'lesson_id': 7, 'module_id': 3, 'title': 'Greetings'},
      'exercises': [
        {
          'exercise_id': 1,
          'exercise_type': 'single_choice',
          'question': 'Hola?',
        },
      ],
    });

    expect(lesson.id, 7);
    expect(lesson.title, 'Greetings');
    expect(lesson.exercises.single.type, 'single_choice');
    expect(lesson.exercises.single.question, 'Hola?');
  });
}
