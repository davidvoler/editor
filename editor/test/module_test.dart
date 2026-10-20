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

  test('parses a module sentence from the server', () {
    final sentence = Sentence.fromJson({
      'sentence_id': 11,
      'lesson_id': 38,
      'sentence': 'Il sole è caldo.',
      'translation': 'The sun is hot.',
      'used': true,
    });

    expect(sentence.id, 11);
    expect(sentence.lessonId, 38);
    expect(sentence.text, 'Il sole è caldo.');
    expect(sentence.translation, 'The sun is hot.');
    expect(sentence.used, isTrue);
  });
}
