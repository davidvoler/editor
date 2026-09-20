import 'package:flutter/material.dart';

void main() => runApp(const CourseEditorApp());

class CourseEditorApp extends StatelessWidget {
  const CourseEditorApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Lumen Course Editor',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: const Color(0xFFF5F1EA),
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF2B7771)),
        fontFamily: 'Arial',
      ),
      home: const CoursesPage(),
    );
  }
}

class Course {
  const Course({
    required this.title,
    required this.learningLanguage,
    required this.studentLanguage,
    required this.level,
    this.lessons = 0,
    this.color = const Color(0xFFE7A37A),
    this.monogram = 'CO',
  });

  final String title;
  final String learningLanguage;
  final String studentLanguage;
  final String level;
  final int lessons;
  final Color color;
  final String monogram;
}

const sampleCourses = [
  Course(
    title: 'Everyday Spanish',
    learningLanguage: 'Spanish',
    studentLanguage: 'English',
    level: 'A1',
    lessons: 18,
    color: Color(0xFFE7A37A),
    monogram: 'ES',
  ),
  Course(
    title: 'German for Curious Minds',
    learningLanguage: 'German',
    studentLanguage: 'English',
    level: 'A2',
    lessons: 12,
    color: Color(0xFF9BC3B2),
    monogram: 'DE',
  ),
  Course(
    title: 'French in Context',
    learningLanguage: 'French',
    studentLanguage: 'English',
    level: 'B1',
    lessons: 24,
    color: Color(0xFFA7B9DB),
    monogram: 'FR',
  ),
  Course(
    title: 'Japanese Foundations',
    learningLanguage: 'Japanese',
    studentLanguage: 'English',
    level: 'A1',
    lessons: 9,
    color: Color(0xFFE0A0AA),
    monogram: '日',
  ),
];

class CoursesPage extends StatefulWidget {
  const CoursesPage({super.key});

  @override
  State<CoursesPage> createState() => _CoursesPageState();
}

class _CoursesPageState extends State<CoursesPage> {
  Future<void> _createCourse() async {
    final course = await showDialog<Course>(
      context: context,
      builder: (_) => const CreateCourseDialog(),
    );
    if (!mounted || course == null) return;
    Navigator.of(context).push(
      MaterialPageRoute<void>(
        builder: (_) => CourseAuthoringPage(course: course),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          const NavigationRailPanel(),
          Expanded(
            child: SingleChildScrollView(
              child: Center(
                child: ConstrainedBox(
                  constraints: const BoxConstraints(maxWidth: 1320),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 64,
                      vertical: 48,
                    ),
                    child: CoursesContent(onAddCourse: _createCourse),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class NavigationRailPanel extends StatelessWidget {
  const NavigationRailPanel({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 232,
      color: const Color(0xFF17252D),
      padding: const EdgeInsets.fromLTRB(24, 30, 18, 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                width: 34,
                height: 34,
                decoration: BoxDecoration(
                  color: const Color(0xFFE7A37A),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: const Icon(
                  Icons.auto_stories_rounded,
                  color: Color(0xFF17252D),
                  size: 19,
                ),
              ),
              const SizedBox(width: 10),
              const Text(
                'lumen',
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 22,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ],
          ),
          const SizedBox(height: 66),
          const NavItem(
            icon: Icons.grid_view_rounded,
            label: 'Courses',
            selected: true,
          ),
          const NavItem(icon: Icons.insights_rounded, label: 'Insights'),
          const NavItem(icon: Icons.people_alt_outlined, label: 'Learners'),
          const Spacer(),
          const Divider(color: Color(0xFF3B4A50)),
          const SizedBox(height: 16),
          const NavItem(icon: Icons.settings_outlined, label: 'Settings'),
          const SizedBox(height: 16),
          Row(
            children: [
              CircleAvatar(
                radius: 17,
                backgroundColor: const Color(0xFF9BC3B2),
                child: const Text(
                  'DL',
                  style: TextStyle(
                    fontSize: 11,
                    fontWeight: FontWeight.w700,
                    color: Color(0xFF17252D),
                  ),
                ),
              ),
              const SizedBox(width: 10),
              const Text(
                'David Lee',
                style: TextStyle(color: Colors.white70, fontSize: 13),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class NavItem extends StatelessWidget {
  const NavItem({
    required this.icon,
    required this.label,
    this.selected = false,
    super.key,
  });

  final IconData icon;
  final String label;
  final bool selected;

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      decoration: BoxDecoration(
        color: selected ? const Color(0xFF2B7771) : Colors.transparent,
        borderRadius: BorderRadius.circular(10),
      ),
      child: ListTile(
        dense: true,
        contentPadding: const EdgeInsets.symmetric(horizontal: 12),
        leading: Icon(
          icon,
          size: 19,
          color: selected ? Colors.white : Colors.white54,
        ),
        title: Text(
          label,
          style: TextStyle(
            color: selected ? Colors.white : Colors.white60,
            fontSize: 13,
            fontWeight: selected ? FontWeight.w700 : FontWeight.w400,
          ),
        ),
      ),
    );
  }
}

class CoursesContent extends StatelessWidget {
  const CoursesContent({required this.onAddCourse, super.key});

  final VoidCallback onAddCourse;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    'Good morning, David',
                    style: TextStyle(color: Color(0xFF748087), fontSize: 14),
                  ),
                  SizedBox(height: 8),
                  Text(
                    'Your courses',
                    style: TextStyle(
                      fontFamily: 'Georgia',
                      color: Color(0xFF17252D),
                      fontSize: 42,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  SizedBox(height: 10),
                  Text(
                    'Shape the next way someone learns a language.',
                    style: TextStyle(color: Color(0xFF65747A), fontSize: 15),
                  ),
                ],
              ),
            ),
            FilledButton.icon(
              onPressed: onAddCourse,
              icon: const Icon(Icons.add_rounded, size: 20),
              label: const Text('Add course'),
              style: FilledButton.styleFrom(
                backgroundColor: const Color(0xFF2B7771),
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(
                  horizontal: 20,
                  vertical: 16,
                ),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(9),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: 48),
        Row(
          children: [
            const Text(
              'All courses',
              style: TextStyle(
                fontWeight: FontWeight.w700,
                color: Color(0xFF17252D),
              ),
            ),
            const SizedBox(width: 12),
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
              decoration: BoxDecoration(
                color: const Color(0xFFE3EAE5),
                borderRadius: BorderRadius.circular(20),
              ),
              child: const Text(
                '4',
                style: TextStyle(
                  color: Color(0xFF2B7771),
                  fontSize: 12,
                  fontWeight: FontWeight.w700,
                ),
              ),
            ),
            const Spacer(),
            const Icon(Icons.tune_rounded, size: 18, color: Color(0xFF748087)),
            const SizedBox(width: 8),
            const Text(
              'Recently edited',
              style: TextStyle(color: Color(0xFF748087), fontSize: 13),
            ),
          ],
        ),
        const SizedBox(height: 16),
        LayoutBuilder(
          builder: (context, constraints) {
            final columns = constraints.maxWidth > 1050
                ? 3
                : constraints.maxWidth > 650
                ? 2
                : 1;
            return GridView.builder(
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              itemCount: sampleCourses.length,
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: columns,
                crossAxisSpacing: 18,
                mainAxisSpacing: 18,
                childAspectRatio: 1.45,
              ),
              itemBuilder: (_, index) =>
                  CourseCard(course: sampleCourses[index]),
            );
          },
        ),
      ],
    );
  }
}

class CourseCard extends StatelessWidget {
  const CourseCard({required this.course, super.key});

  final Course course;

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.white,
      borderRadius: BorderRadius.circular(14),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: () {},
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(
                      color: course.color,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Center(
                      child: Text(
                        course.monogram,
                        style: const TextStyle(
                          fontSize: 13,
                          fontWeight: FontWeight.w800,
                          color: Color(0xFF17252D),
                        ),
                      ),
                    ),
                  ),
                  const Spacer(),
                  const Icon(
                    Icons.more_horiz_rounded,
                    color: Color(0xFF97A1A4),
                  ),
                ],
              ),
              const Spacer(),
              Text(
                course.title,
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(
                  fontFamily: 'Georgia',
                  fontSize: 21,
                  fontWeight: FontWeight.w700,
                  color: Color(0xFF17252D),
                ),
              ),
              const SizedBox(height: 14),
              Row(
                children: [
                  CourseMeta(label: 'Learning', value: course.learningLanguage),
                  const SizedBox(width: 20),
                  CourseMeta(label: 'Student', value: course.studentLanguage),
                  const Spacer(),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 9,
                      vertical: 5,
                    ),
                    decoration: BoxDecoration(
                      color: const Color(0xFFF2EEE8),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(
                      course.level,
                      style: const TextStyle(
                        fontSize: 12,
                        fontWeight: FontWeight.w800,
                        color: Color(0xFF53636A),
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 15),
              Row(
                children: [
                  const Icon(
                    Icons.menu_book_outlined,
                    size: 16,
                    color: Color(0xFF8A979A),
                  ),
                  const SizedBox(width: 6),
                  Text(
                    '${course.lessons} lessons',
                    style: const TextStyle(
                      color: Color(0xFF8A979A),
                      fontSize: 12,
                    ),
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

class CourseMeta extends StatelessWidget {
  const CourseMeta({required this.label, required this.value, super.key});

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) => Column(
    crossAxisAlignment: CrossAxisAlignment.start,
    children: [
      Text(
        label.toUpperCase(),
        style: const TextStyle(
          fontSize: 9,
          letterSpacing: .7,
          color: Color(0xFF9AA4A6),
          fontWeight: FontWeight.w700,
        ),
      ),
      const SizedBox(height: 4),
      Text(
        value,
        style: const TextStyle(
          fontSize: 12,
          color: Color(0xFF42535A),
          fontWeight: FontWeight.w700,
        ),
      ),
    ],
  );
}

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
                                    onPressed: () {
                                      Navigator.of(context).push(
                                        MaterialPageRoute<void>(
                                          builder: (_) => ModuleEditingPage(
                                            course: course,
                                            moduleTitle: 'Module 1',
                                          ),
                                        ),
                                      );
                                    },
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

class ModuleEditingPage extends StatelessWidget {
  const ModuleEditingPage({
    required this.course,
    required this.moduleTitle,
    super.key,
  });

  final Course course;
  final String moduleTitle;

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
                        tooltip: 'Back to course',
                        onPressed: () => Navigator.of(context).pop(),
                        icon: const Icon(Icons.arrow_back_rounded),
                      ),
                      const SizedBox(width: 16),
                      Text(
                        course.title,
                        style: const TextStyle(
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
                        moduleTitle,
                        style: const TextStyle(
                          color: Color(0xFF17252D),
                          fontSize: 13,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                      const Spacer(),
                      const Text(
                        'Unsaved changes',
                        style: TextStyle(
                          color: Color(0xFF9A6B45),
                          fontSize: 12,
                        ),
                      ),
                      const SizedBox(width: 18),
                      FilledButton(onPressed: () {}, child: const Text('Save')),
                    ],
                  ),
                ),
                Expanded(
                  child: Row(
                    children: [
                      Container(
                        width: 260,
                        color: const Color(0xFFFBF8F3),
                        padding: const EdgeInsets.fromLTRB(26, 30, 20, 24),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text(
                              'MODULE OUTLINE',
                              style: TextStyle(
                                color: Color(0xFF9AA4A6),
                                fontSize: 10,
                                fontWeight: FontWeight.w700,
                                letterSpacing: 1,
                              ),
                            ),
                            const SizedBox(height: 16),
                            Container(
                              padding: const EdgeInsets.all(12),
                              decoration: BoxDecoration(
                                color: const Color(0xFFE3EAE5),
                                borderRadius: BorderRadius.circular(9),
                              ),
                              child: Row(
                                children: [
                                  const Icon(
                                    Icons.layers_outlined,
                                    size: 18,
                                    color: Color(0xFF2B7771),
                                  ),
                                  const SizedBox(width: 10),
                                  Expanded(
                                    child: Text(
                                      moduleTitle,
                                      style: const TextStyle(
                                        fontWeight: FontWeight.w700,
                                        color: Color(0xFF17252D),
                                      ),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 12),
                            const Text(
                              'No lessons yet',
                              style: TextStyle(
                                color: Color(0xFF8A979A),
                                fontSize: 13,
                              ),
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
                              const Text(
                                'Module 1',
                                style: TextStyle(
                                  fontFamily: 'Georgia',
                                  fontSize: 34,
                                  fontWeight: FontWeight.w700,
                                  color: Color(0xFF17252D),
                                ),
                              ),
                              const SizedBox(height: 8),
                              const Text(
                                'Build a sequence of lessons for your learners.',
                                style: TextStyle(
                                  color: Color(0xFF748087),
                                  fontSize: 14,
                                ),
                              ),
                              const SizedBox(height: 34),
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
                                          width: 58,
                                          height: 58,
                                          decoration: BoxDecoration(
                                            color: const Color(0xFFFFE8D9),
                                            borderRadius: BorderRadius.circular(
                                              17,
                                            ),
                                          ),
                                          child: const Icon(
                                            Icons.menu_book_outlined,
                                            color: Color(0xFFB86F46),
                                            size: 27,
                                          ),
                                        ),
                                        const SizedBox(height: 18),
                                        const Text(
                                          'Start with your first lesson',
                                          style: TextStyle(
                                            fontFamily: 'Georgia',
                                            fontSize: 21,
                                            fontWeight: FontWeight.w700,
                                            color: Color(0xFF17252D),
                                          ),
                                        ),
                                        const SizedBox(height: 8),
                                        const Text(
                                          'Lessons will become the building blocks of this module.',
                                          style: TextStyle(
                                            color: Color(0xFF748087),
                                            fontSize: 14,
                                          ),
                                        ),
                                        const SizedBox(height: 22),
                                        FilledButton.icon(
                                          onPressed: () {},
                                          icon: const Icon(
                                            Icons.add_rounded,
                                            size: 18,
                                          ),
                                          label: const Text('Add lesson'),
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
          ),
        ],
      ),
    );
  }
}
