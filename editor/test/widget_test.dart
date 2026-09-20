import 'package:flutter/material.dart';
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter_test/flutter_test.dart';

import 'package:editor/main.dart';

void main() {
  testWidgets('shows the courses page', (WidgetTester tester) async {
    await tester.pumpWidget(const CourseEditorApp());

    expect(find.text('Your courses'), findsOneWidget);
    expect(find.text('Everyday Spanish'), findsOneWidget);
    expect(find.text('Add course'), findsOneWidget);
  });

  testWidgets('opens course setup and enters authoring', (
    WidgetTester tester,
  ) async {
    tester.view.physicalSize = const Size(1440, 1000);
    tester.view.devicePixelRatio = 1;
    await tester.pumpWidget(const CourseEditorApp());

    await tester.tap(find.text('Add course'));
    await tester.pumpAndSettle();
    expect(find.text('Create a course'), findsOneWidget);
    expect(find.text('Learning language'), findsOneWidget);
    expect(find.text('Student language'), findsOneWidget);
    expect(find.text('Course title'), findsOneWidget);

    await tester.enterText(find.byType(TextField), 'Italian for Travel');
    await tester.tap(find.text('Continue'));
    await tester.pumpAndSettle();

    expect(find.text('Italian for Travel'), findsNWidgets(2));
    expect(find.text('Your course is ready to take shape'), findsOneWidget);

    await tester.tap(find.text('Add first module'));
    await tester.pumpAndSettle();

    expect(find.text('MODULE OUTLINE'), findsOneWidget);
    expect(find.text('Start with your first lesson'), findsOneWidget);
    expect(find.text('Add lesson'), findsOneWidget);

    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
  });
}
