import 'package:flutter/material.dart';

import '../../../core/widgets/navigation_rail_panel.dart';
import '../../courses/data/course.dart';
import '../../courses/pages/course_authoring_page.dart';
import '../data/chat_responder.dart';
import '../widgets/chat_panel.dart';

class ChatPage extends StatefulWidget {
  const ChatPage({super.key});

  @override
  State<ChatPage> createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  Course course = sampleCourses.first;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          const NavigationRailPanel(selected: NavSection.chat),
          Expanded(
            child: Column(
              children: [
                _buildHeader(),
                Expanded(
                  child: Row(
                    children: [
                      Expanded(
                        child: ChatPanel(
                          responder: ChatResponder(course: course),
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

  Widget _buildHeader() {
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
            items: sampleCourses
                .map(
                  (course) => DropdownMenuItem(
                    value: course,
                    child: Text(course.title),
                  ),
                )
                .toList(),
            onChanged: (value) => setState(() => course = value!),
          ),
        ],
      ),
    );
  }
}
