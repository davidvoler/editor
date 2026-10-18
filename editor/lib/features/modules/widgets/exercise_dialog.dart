import 'package:flutter/material.dart';

import '../data/module.dart';

/// Adds or edits an exercise. Pops the edited exercise, or null when
/// cancelled.
class ExerciseDialog extends StatefulWidget {
  const ExerciseDialog({
    required this.exercise,
    this.words = const [],
    super.key,
  });

  /// The exercise to edit; one without an id is new.
  final Exercise exercise;

  /// The module's words, offered for the word field.
  final List<Word> words;

  @override
  State<ExerciseDialog> createState() => _ExerciseDialogState();
}

class _ExerciseDialogState extends State<ExerciseDialog> {
  final formKey = GlobalKey<FormState>();
  late String type = exerciseTypes.containsKey(widget.exercise.type)
      ? widget.exercise.type
      : exerciseTypes.keys.first;
  late final word = TextEditingController(text: widget.exercise.word);
  final wordFocus = FocusNode();
  late final question = TextEditingController(text: widget.exercise.question);
  late final answer = TextEditingController(text: widget.exercise.answer);
  late final incorrect = TextEditingController(
    text: widget.exercise.incorrectOptions.join('\n'),
  );
  late final translation = TextEditingController(
    text: widget.exercise.translation,
  );
  late final explanation = TextEditingController(
    text: widget.exercise.explanation,
  );

  @override
  void dispose() {
    for (final controller in [
      word,
      question,
      answer,
      incorrect,
      translation,
      explanation,
    ]) {
      controller.dispose();
    }
    wordFocus.dispose();
    super.dispose();
  }

  void submit() {
    if (!formKey.currentState!.validate()) return;
    final current = widget.exercise;
    Navigator.of(context).pop(
      Exercise(
        id: current.id,
        courseId: current.courseId,
        moduleId: current.moduleId,
        lessonId: current.lessonId,
        type: type,
        word: word.text.trim(),
        question: question.text.trim(),
        answer: answer.text.trim(),
        incorrectOptions: [
          for (final line in incorrect.text.split('\n'))
            if (line.trim().isNotEmpty) line.trim(),
        ],
        translation: translation.text.trim(),
        explanation: explanation.text.trim(),
      ),
    );
  }

  String? _required(String? value) =>
      value == null || value.trim().isEmpty ? 'Required' : null;

  @override
  Widget build(BuildContext context) {
    final isNew = widget.exercise.id == null;
    const gap = SizedBox(height: 14);
    return Dialog(
      backgroundColor: const Color(0xFFFFFCF8),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 560),
        child: Form(
          key: formKey,
          child: ListView(
            shrinkWrap: true,
            padding: const EdgeInsets.fromLTRB(32, 30, 32, 28),
            children: [
              Text(
                isNew ? 'Add an exercise' : 'Edit exercise',
                style: const TextStyle(
                  fontFamily: 'Georgia',
                  fontSize: 26,
                  fontWeight: FontWeight.w700,
                  color: Color(0xFF17252D),
                ),
              ),
              const SizedBox(height: 22),
              Row(
                children: [
                  Expanded(
                    child: DropdownButtonFormField<String>(
                      initialValue: type,
                      isExpanded: true,
                      decoration: const InputDecoration(labelText: 'Type'),
                      items: [
                        for (final entry in exerciseTypes.entries)
                          DropdownMenuItem(
                            value: entry.key,
                            child: Text(entry.value),
                          ),
                      ],
                      onChanged: (value) => setState(() => type = value!),
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(child: _buildWordField()),
                ],
              ),
              gap,
              TextFormField(
                controller: question,
                autofocus: isNew,
                maxLines: null,
                validator: _required,
                decoration: const InputDecoration(
                  labelText: 'Question',
                  hintText: 'Use ___ for the blank',
                ),
              ),
              gap,
              TextFormField(
                controller: answer,
                validator: _required,
                decoration: const InputDecoration(labelText: 'Answer'),
              ),
              gap,
              TextFormField(
                controller: incorrect,
                minLines: 2,
                maxLines: null,
                decoration: const InputDecoration(
                  labelText: 'Wrong options',
                  hintText: 'One per line',
                ),
              ),
              gap,
              TextFormField(
                controller: translation,
                maxLines: null,
                decoration: const InputDecoration(labelText: 'Translation'),
              ),
              gap,
              TextFormField(
                controller: explanation,
                maxLines: null,
                decoration: const InputDecoration(labelText: 'Explanation'),
              ),
              const SizedBox(height: 26),
              Row(
                children: [
                  const Spacer(),
                  TextButton(
                    onPressed: () => Navigator.of(context).pop(),
                    child: const Text('Cancel'),
                  ),
                  const SizedBox(width: 10),
                  FilledButton(
                    onPressed: submit,
                    child: Text(isNew ? 'Add' : 'Save'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  /// A text field that suggests the module's words as you type.
  Widget _buildWordField() => RawAutocomplete<String>(
    textEditingController: word,
    focusNode: wordFocus,
    optionsBuilder: (value) {
      final text = value.text.trim().toLowerCase();
      return [
        for (final w in widget.words)
          if (text.isEmpty || w.text.toLowerCase().contains(text)) w.text,
      ];
    },
    fieldViewBuilder: (context, controller, focusNode, onSubmitted) =>
        TextFormField(
          controller: controller,
          focusNode: focusNode,
          decoration: const InputDecoration(
            labelText: 'Word',
            hintText: 'The word it practises',
          ),
        ),
    optionsViewBuilder: (context, onSelected, options) => Align(
      alignment: Alignment.topLeft,
      child: Material(
        elevation: 4,
        borderRadius: BorderRadius.circular(10),
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxHeight: 240, maxWidth: 240),
          child: ListView(
            padding: EdgeInsets.zero,
            shrinkWrap: true,
            children: [
              for (final option in options)
                ListTile(
                  dense: true,
                  title: Text(option),
                  onTap: () => onSelected(option),
                ),
            ],
          ),
        ),
      ),
    ),
  );
}
