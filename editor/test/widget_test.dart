// This is a basic Flutter widget test.
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
}
