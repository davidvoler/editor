import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../../core/widgets/navigation_rail_panel.dart';
import '../../chat/data/prompt_router_responder.dart';
import '../../chat/widgets/chat_panel.dart';
import '../../modules/data/module.dart';
import '../../modules/pages/module_editing_page.dart';
import '../data/course.dart';

class CourseAuthoringPage extends ConsumerWidget {
  const CourseAuthoringPage({required this.course, super.key});

  final Course course;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      body: Row(
        children: [
          const NavigationRailPanel(),
          Expanded(
            child: Column(
              children: [
                _buildHeader(context),
                Expanded(
                  child: Row(
                    children: [
                      Expanded(
                        child: ChatPanel(
                          responder: ref.watch(responderFactoryProvider)(
                            course,
                          ),
                        ),
                      ),
                      const VerticalDivider(width: 1, color: Color(0xFFE4E0D9)),
                      Expanded(child: CourseDataPane(course: course)),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildHeader(BuildContext context) {
    return Container(
      height: 78,
      padding: const EdgeInsets.symmetric(horizontal: 42),
      decoration: const BoxDecoration(
        color: Colors.white,
        border: Border(bottom: BorderSide(color: Color(0xFFE4E0D9))),
      ),
      child: Row(
        children: [
          IconButton(
            tooltip: 'Back to courses',
            onPressed: () => Navigator.of(context).pop(),
            icon: const Icon(Icons.arrow_back_rounded),
          ),
          const SizedBox(width: 16),
          const Text(
            'Courses',
            style: TextStyle(color: Color(0xFF8A979A), fontSize: 13),
          ),
          const Padding(
            padding: EdgeInsets.symmetric(horizontal: 12),
            child: Icon(
              Icons.chevron_right_rounded,
              size: 18,
              color: Color(0xFFB2B9B8),
            ),
          ),
          Text(
            course.title,
            style: const TextStyle(
              color: Color(0xFF17252D),
              fontSize: 13,
              fontWeight: FontWeight.w700,
            ),
          ),
          const Spacer(),
          OutlinedButton.icon(
            onPressed: () {},
            icon: const Icon(Icons.visibility_outlined, size: 17),
            label: const Text('Preview'),
          ),
        ],
      ),
    );
  }
}

class CourseDataPane extends ConsumerStatefulWidget {
  const CourseDataPane({required this.course, super.key});

  final Course course;

  @override
  ConsumerState<CourseDataPane> createState() => _CourseDataPaneState();
}

class _CourseDataPaneState extends ConsumerState<CourseDataPane> {
  /// The module whose lessons are shown. Defaults to the first module.
  int? currentModuleId;

  Course get course => widget.course;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(42),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            course.title,
            style: const TextStyle(
              fontFamily: 'Georgia',
              fontSize: 36,
              fontWeight: FontWeight.w700,
              color: Color(0xFF17252D),
            ),
          ),
          const SizedBox(height: 8),
          Text(
            '${course.learningLanguage} for ${course.studentLanguage}  ·  ${course.level}',
            style: const TextStyle(color: Color(0xFF748087), fontSize: 14),
          ),
          const SizedBox(height: 24),
          Wrap(
            spacing: 12,
            runSpacing: 12,
            children: [
              _CourseFact(label: 'Learning', value: course.learningLanguage),
              _CourseFact(
                label: 'Students speak',
                value: course.studentLanguage,
              ),
              _CourseFact(label: 'Level', value: course.level),
              _CourseFact(label: 'Lessons', value: '${course.lessons}'),
            ],
          ),
          const SizedBox(height: 28),
          const Text(
            'MODULES',
            style: TextStyle(
              color: Color(0xFF9AA4A6),
              fontSize: 10,
              fontWeight: FontWeight.w700,
              letterSpacing: 1,
            ),
          ),
          const SizedBox(height: 12),
          Expanded(child: _buildModules()),
        ],
      ),
    );
  }

  Widget _buildModules() {
    final id = course.id;
    if (id == null) return _EmptyModules(course: course);
    return ref
        .watch(modulesProvider(id))
        .when(
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (error, _) => Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text('Could not load the modules.\n$error'),
                const SizedBox(height: 16),
                OutlinedButton(
                  onPressed: () => ref.invalidate(modulesProvider(id)),
                  child: const Text('Retry'),
                ),
              ],
            ),
          ),
          data: (modules) {
            if (modules.isEmpty) return _EmptyModules(course: course);
            final current = modules.any((m) => m.id == currentModuleId)
                ? currentModuleId
                : modules.first.id;
            return ListView.separated(
              itemCount: modules.length,
              separatorBuilder: (_, _) => const SizedBox(height: 10),
              itemBuilder: (context, index) {
                final module = modules[index];
                return _ModuleCard(
                  module: module,
                  isCurrent: module.id == current,
                  onTap: () => setState(() => currentModuleId = module.id),
                );
              },
            );
          },
        );
  }
}

class _ModuleCard extends ConsumerWidget {
  const _ModuleCard({
    required this.module,
    required this.isCurrent,
    required this.onTap,
  });

  final Module module;
  final bool isCurrent;
  final VoidCallback onTap;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Material(
      color: Colors.white,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: BorderSide(
          color: isCurrent ? const Color(0xFF2B7771) : const Color(0xFFE4E0D9),
        ),
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          ListTile(
            onTap: onTap,
            leading: Icon(
              isCurrent ? Icons.folder_open_rounded : Icons.folder_outlined,
              color: const Color(0xFF2B7771),
            ),
            title: Text(
              module.title.isEmpty ? 'Untitled module' : module.title,
              style: const TextStyle(
                fontWeight: FontWeight.w700,
                color: Color(0xFF17252D),
              ),
            ),
            subtitle: module.description.isEmpty
                ? null
                : Text(
                    module.description,
                    style: const TextStyle(color: Color(0xFF748087)),
                  ),
          ),
          if (isCurrent) _buildLessons(ref),
        ],
      ),
    );
  }

  Widget _buildLessons(WidgetRef ref) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 0, 16, 14),
      child: ref
          .watch(lessonsProvider(module.id))
          .when(
            loading: () => const LinearProgressIndicator(),
            error: (error, _) => Text('Could not load the lessons.\n$error'),
            data: (lessons) => lessons.isEmpty
                ? const Text(
                    'No lessons yet.',
                    style: TextStyle(color: Color(0xFF748087), fontSize: 13),
                  )
                : Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      for (final lesson in lessons) _LessonRow(lesson: lesson),
                    ],
                  ),
          ),
    );
  }
}

class _LessonRow extends StatelessWidget {
  const _LessonRow({required this.lesson});

  final Lesson lesson;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(top: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              const Icon(
                Icons.menu_book_outlined,
                size: 17,
                color: Color(0xFFB86F46),
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  lesson.title.isEmpty ? 'Untitled lesson' : lesson.title,
                  style: const TextStyle(
                    fontWeight: FontWeight.w600,
                    color: Color(0xFF17252D),
                    fontSize: 14,
                  ),
                ),
              ),
              Text(
                '${lesson.exercises.length} exercises',
                style: const TextStyle(color: Color(0xFF8A979A), fontSize: 12),
              ),
            ],
          ),
          for (final exercise in lesson.exercises)
            Padding(
              padding: const EdgeInsets.only(left: 25, top: 4),
              child: Text(
                [
                  if (exercise.type.isNotEmpty) exercise.type,
                  if (exercise.question.isNotEmpty) exercise.question,
                ].join(' · '),
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(color: Color(0xFF748087), fontSize: 13),
              ),
            ),
        ],
      ),
    );
  }
}

class _EmptyModules extends StatelessWidget {
  const _EmptyModules({required this.course});

  final Course course;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: const Color(0xFFE4E0D9)),
      ),
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 62,
              height: 62,
              decoration: BoxDecoration(
                color: const Color(0xFFE3EAE5),
                borderRadius: BorderRadius.circular(18),
              ),
              child: const Icon(
                Icons.layers_outlined,
                size: 29,
                color: Color(0xFF2B7771),
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              'Your course is ready to take shape',
              style: TextStyle(
                fontFamily: 'Georgia',
                fontSize: 22,
                fontWeight: FontWeight.w700,
                color: Color(0xFF17252D),
              ),
            ),
            const SizedBox(height: 8),
            const Text(
              'Ask the assistant, or add your first module yourself.',
              style: TextStyle(color: Color(0xFF748087), fontSize: 14),
            ),
            const SizedBox(height: 24),
            FilledButton.icon(
              onPressed: () => Navigator.of(context).push(
                MaterialPageRoute<void>(
                  builder: (_) => ModuleEditingPage(
                    course: course,
                    moduleTitle: 'Module 1',
                  ),
                ),
              ),
              icon: const Icon(Icons.add_rounded, size: 19),
              label: const Text('Add first module'),
            ),
          ],
        ),
      ),
    );
  }
}

class _CourseFact extends StatelessWidget {
  const _CourseFact({required this.label, required this.value});

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 150,
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: const Color(0xFFE4E0D9)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            label,
            style: const TextStyle(color: Color(0xFF8A979A), fontSize: 12),
          ),
          const SizedBox(height: 4),
          Text(
            value,
            style: const TextStyle(
              color: Color(0xFF17252D),
              fontSize: 16,
              fontWeight: FontWeight.w700,
            ),
          ),
        ],
      ),
    );
  }
}
