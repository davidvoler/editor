import 'package:flutter/material.dart';

import '../data/course.dart';

class CreateCourseDialog extends StatefulWidget {
  const CreateCourseDialog({super.key});

  @override
  State<CreateCourseDialog> createState() => _CreateCourseDialogState();
}

class _CreateCourseDialogState extends State<CreateCourseDialog> {
  final titleController = TextEditingController();
  String learningLanguage = 'Spanish';
  String studentLanguage = 'English';
  String level = 'A1';

  @override
  void dispose() {
    titleController.dispose();
    super.dispose();
  }

  void submit() {
    final title = titleController.text.trim();
    if (title.isEmpty) return;
    Navigator.of(context).pop(
      Course(
        title: title,
        learningLanguage: learningLanguage,
        studentLanguage: studentLanguage,
        level: level,
        monogram: learningLanguage.substring(0, 2).toUpperCase(),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Dialog(
      backgroundColor: const Color(0xFFFFFCF8),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 560),
        child: Padding(
          padding: const EdgeInsets.fromLTRB(32, 30, 32, 28),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  const Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'Create a course',
                          style: TextStyle(
                            fontFamily: 'Georgia',
                            fontSize: 26,
                            fontWeight: FontWeight.w700,
                            color: Color(0xFF17252D),
                          ),
                        ),
                        SizedBox(height: 7),
                        Text(
                          'Set the foundation before you start authoring.',
                          style: TextStyle(
                            color: Color(0xFF748087),
                            fontSize: 13,
                          ),
                        ),
                      ],
                    ),
                  ),
                  IconButton(
                    onPressed: () => Navigator.of(context).pop(),
                    icon: const Icon(Icons.close_rounded),
                  ),
                ],
              ),
              const SizedBox(height: 28),
              TextField(
                controller: titleController,
                autofocus: true,
                decoration: const InputDecoration(
                  labelText: 'Course title',
                  hintText: 'For example, Everyday Spanish',
                  prefixIcon: Icon(Icons.title_rounded),
                ),
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: CourseDropdown(
                      label: 'Learning language',
                      value: learningLanguage,
                      values: const [
                        'Spanish',
                        'German',
                        'French',
                        'Japanese',
                        'English',
                      ],
                      onChanged: (value) =>
                          setState(() => learningLanguage = value!),
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: CourseDropdown(
                      label: 'Student language',
                      value: studentLanguage,
                      values: const ['English', 'Spanish', 'German', 'French'],
                      onChanged: (value) =>
                          setState(() => studentLanguage = value!),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              CourseDropdown(
                label: 'Level',
                value: level,
                values: const ['A1', 'A2', 'B1', 'B2', 'C1'],
                onChanged: (value) => setState(() => level = value!),
              ),
              const SizedBox(height: 28),
              Row(
                children: [
                  const Spacer(),
                  TextButton(
                    onPressed: () => Navigator.of(context).pop(),
                    child: const Text('Cancel'),
                  ),
                  const SizedBox(width: 10),
                  FilledButton.icon(
                    onPressed: submit,
                    icon: const Icon(Icons.arrow_forward_rounded, size: 18),
                    label: const Text('Continue'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class CourseDropdown extends StatelessWidget {
  const CourseDropdown({
    required this.label,
    required this.value,
    required this.values,
    required this.onChanged,
    super.key,
  });

  final String label;
  final String value;
  final List<String> values;
  final ValueChanged<String?> onChanged;

  @override
  Widget build(BuildContext context) => DropdownButtonFormField<String>(
    initialValue: value,
    decoration: InputDecoration(labelText: label),
    items: values
        .map((item) => DropdownMenuItem(value: item, child: Text(item)))
        .toList(),
    onChanged: onChanged,
  );
}
