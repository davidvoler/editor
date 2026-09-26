import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import '../../../core/widgets/navigation_rail_panel.dart';
import '../../courses/data/course.dart';
import '../../courses/data/courses_repository.dart';
import '../../courses/pages/course_authoring_page.dart';
import '../data/prompt_router_responder.dart';
import '../widgets/chat_panel.dart';

class ChatPage extends ConsumerStatefulWidget {
  const ChatPage({super.key});

  @override
  ConsumerState<ChatPage> createState() => _ChatPageState();
}

class _ChatPageState extends ConsumerState<ChatPage> {
  Course? selected;

  @override
  Widget build(BuildContext context) {
    final courses = ref.watch(coursesProvider);
    return Scaffold(
      body: Row(
        children: [
          const NavigationRailPanel(selected: NavSection.chat),
          Expanded(
            child: courses.when(
              data: (courses) => courses.isEmpty
                  ? const Center(
                      child: Text('No courses yet. Add one from Courses.'),
                    )
                  : _buildChat(
                      courses,
                      courses.contains(selected) ? selected! : courses.first,
                    ),
              loading: () => const Center(child: CircularProgressIndicator()),
              error: (error, _) => Center(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text('Could not load courses from the server.\n$error'),
                    const SizedBox(height: 16),
                    OutlinedButton(
                      onPressed: () => ref.invalidate(coursesProvider),
                      child: const Text('Retry'),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildChat(List<Course> courses, Course course) {
    return Column(
      children: [
        _buildHeader(courses, course),
        Expanded(
          child: Row(
            children: [
              Expanded(
                // A new course starts a new conversation.
                child: ChatPanel(
                  key: ObjectKey(course),
                  responder: ref.watch(responderFactoryProvider)(course),
                ),
              ),
              const VerticalDivider(width: 1, color: Color(0xFFE4E0D9)),
              Expanded(child: CourseDataPane(course: course)),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildHeader(List<Course> courses, Course course) {
    return Container(
      height: 78,
      padding: const EdgeInsets.symmetric(horizontal: 42),
      decoration: const BoxDecoration(
        color: Colors.white,
        border: Border(bottom: BorderSide(color: Color(0xFFE4E0D9))),
      ),
      child: Row(
        children: [
          const Text(
            'Chat',
            style: TextStyle(
              color: Color(0xFF17252D),
              fontSize: 13,
              fontWeight: FontWeight.w700,
            ),
          ),
          const Spacer(),
          const Text(
            'Course',
            style: TextStyle(color: Color(0xFF8A979A), fontSize: 13),
          ),
          const SizedBox(width: 12),
          DropdownButton<Course>(
            value: course,
            underline: const SizedBox.shrink(),
            items: courses
                .map(
                  (course) => DropdownMenuItem(
                    value: course,
                    child: Text(course.title),
                  ),
                )
                .toList(),
            onChanged: (value) => setState(() => selected = value),
          ),
        ],
      ),
    );
  }
}
