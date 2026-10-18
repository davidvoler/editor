import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:editor/features/modules/data/module.dart';
import 'package:editor/features/modules/widgets/exercise_dialog.dart';

void main() {
  test('maps wrong options and translation to the server columns', () {
    final exercise = Exercise.fromJson({
      'exercise_id': 1,
      'lesson_id': 11,
      'exercise_type': 'single_choice',
      'word': 'ciao',
      'question': '___, come stai?',
      'answer': 'Ciao',
      'options': {
        'incorrect': ['Grazie', 'Prego'],
      },
      'sentence_alt1': 'Hi, how are you?',
    });

    expect(exercise.incorrectOptions, ['Grazie', 'Prego']);
    expect(exercise.translation, 'Hi, how are you?');
    expect(exercise.toJson(), containsPair('word', 'ciao'));
    expect(exercise.toJson()['options'], {
      'incorrect': ['Grazie', 'Prego'],
    });
    expect(exercise.toJson()['sentence_alt1'], 'Hi, how are you?');
  });

  testWidgets('the form returns the edited exercise', (tester) async {
    tester.view.physicalSize = const Size(1440, 1000);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    Exercise? result;
    await tester.pumpWidget(
      MaterialApp(
        home: Builder(
          builder: (context) => TextButton(
            onPressed: () async => result = await showDialog<Exercise>(
              context: context,
              builder: (_) =>
                  const ExerciseDialog(exercise: Exercise(lessonId: 11)),
            ),
            child: const Text('open'),
          ),
        ),
      ),
    );
    await tester.tap(find.text('open'));
    await tester.pumpAndSettle();

    // Question and answer are required.
    await tester.tap(find.text('Add'));
    await tester.pumpAndSettle();
    expect(find.text('Required'), findsNWidgets(2));

    await tester.enterText(
      find.widgetWithText(TextFormField, 'Question'),
      '___, come stai?',
    );
    await tester.enterText(
      find.widgetWithText(TextFormField, 'Answer'),
      'Ciao',
    );
    await tester.enterText(
      find.widgetWithText(TextFormField, 'Wrong options'),
      'Grazie\n\nPrego ',
    );
    await tester.tap(find.text('Add'));
    await tester.pumpAndSettle();

    expect(result?.lessonId, 11);
    expect(result?.type, 'single_choice');
    expect(result?.answer, 'Ciao');
    expect(result?.incorrectOptions, ['Grazie', 'Prego']);
  });
}
