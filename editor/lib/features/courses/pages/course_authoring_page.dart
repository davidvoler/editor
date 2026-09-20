import 'package:flutter/material.dart';

import '../../../core/widgets/navigation_rail_panel.dart';
import '../../modules/pages/module_editing_page.dart';
import '../data/course.dart';

class CourseAuthoringPage extends StatelessWidget {
  const CourseAuthoringPage({required this.course, super.key});

  final Course course;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          const NavigationRailPanel(),
          Expanded(
            child: Column(
              children: [
                Container(
                  height: 78,
                  padding: const EdgeInsets.symmetric(horizontal: 42),
                  decoration: const BoxDecoration(
                    color: Colors.white,
                    border: Border(
                      bottom: BorderSide(color: Color(0xFFE4E0D9)),
                    ),
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
                        style: TextStyle(
                          color: Color(0xFF8A979A),
                          fontSize: 13,
                        ),
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
                ),
                Expanded(
                  child: Padding(
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
                          style: const TextStyle(
                            color: Color(0xFF748087),
                            fontSize: 14,
                          ),
                        ),
                        const SizedBox(height: 38),
                        Expanded(
                          child: Container(
                            width: double.infinity,
                            decoration: BoxDecoration(
                              color: Colors.white,
                              borderRadius: BorderRadius.circular(14),
                              border: Border.all(
                                color: const Color(0xFFE4E0D9),
                              ),
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
                                    'Add your first module to begin authoring lessons.',
                                    style: TextStyle(
                                      color: Color(0xFF748087),
                                      fontSize: 14,
                                    ),
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
                                    icon: const Icon(
                                      Icons.add_rounded,
                                      size: 19,
                                    ),
                                    label: const Text('Add first module'),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
