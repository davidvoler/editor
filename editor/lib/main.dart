import 'package:flutter/material.dart';

void main() {
  runApp(const CourseEditorApp());
}

class CourseEditorApp extends StatelessWidget {
  const CourseEditorApp({super.key});

  @override
  Widget build(BuildContext context) {
    const ink = Color(0xFF17252D);
    return MaterialApp(
      title: 'Lumen Course Editor',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        scaffoldBackgroundColor: const Color(0xFFF5F1EA),
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF2B7771),
          brightness: Brightness.light,
          surface: const Color(0xFFF5F1EA),
        ),
        fontFamily: 'Georgia',
        textTheme: const TextTheme(
          bodyMedium: TextStyle(fontFamily: 'Arial', color: ink),
          labelLarge: TextStyle(
            fontFamily: 'Arial',
            fontWeight: FontWeight.w700,
          ),
        ),
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
    required this.lessons,
    required this.color,
    required this.monogram,
  });

  final String title;
  final String learningLanguage;
  final String studentLanguage;
  final String level;
  final int lessons;
  final Color color;
  final String monogram;
}

const courses = [
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

class CoursesPage extends StatelessWidget {
  const CoursesPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Row(
        children: [
          const _NavigationRail(),
          Expanded(
            child: LayoutBuilder(
              builder: (context, constraints) {
                return SingleChildScrollView(
                  child: Center(
                    child: ConstrainedBox(
                      constraints: const BoxConstraints(maxWidth: 1320),
                      child: Padding(
                        padding: EdgeInsets.symmetric(
                          horizontal: constraints.maxWidth > 900 ? 64 : 28,
                          vertical: 48,
                        ),
                        child: const _CoursesContent(),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

class _NavigationRail extends StatelessWidget {
  const _NavigationRail();

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
          const _NavItem(
            icon: Icons.grid_view_rounded,
            label: 'Courses',
            selected: true,
          ),
          const _NavItem(icon: Icons.insights_rounded, label: 'Insights'),
          const _NavItem(icon: Icons.people_alt_outlined, label: 'Learners'),
          const Spacer(),
          const Divider(color: Color(0xFF3B4A50)),
          const SizedBox(height: 16),
          const _NavItem(icon: Icons.settings_outlined, label: 'Settings'),
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
                style: TextStyle(
                  color: Colors.white70,
                  fontFamily: 'Arial',
                  fontSize: 13,
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _NavItem extends StatelessWidget {
  const _NavItem({
    required this.icon,
    required this.label,
    this.selected = false,
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
            fontFamily: 'Arial',
            fontSize: 13,
            fontWeight: selected ? FontWeight.w700 : FontWeight.w400,
          ),
        ),
      ),
    );
  }
}

class _CoursesContent extends StatelessWidget {
  const _CoursesContent();

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
                    style: TextStyle(
                      fontFamily: 'Arial',
                      color: Color(0xFF748087),
                      fontSize: 14,
                    ),
                  ),
                  SizedBox(height: 8),
                  Text(
                    'Your courses',
                    style: TextStyle(
                      color: Color(0xFF17252D),
                      fontSize: 42,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -1.2,
                    ),
                  ),
                  SizedBox(height: 10),
                  Text(
                    'Shape the next way someone learns a language.',
                    style: TextStyle(
                      fontFamily: 'Arial',
                      color: Color(0xFF65747A),
                      fontSize: 15,
                    ),
                  ),
                ],
              ),
            ),
            FilledButton.icon(
              onPressed: () {},
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
                fontFamily: 'Arial',
                fontSize: 14,
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
                  fontFamily: 'Arial',
                  fontSize: 12,
                  color: Color(0xFF2B7771),
                  fontWeight: FontWeight.w700,
                ),
              ),
            ),
            const Spacer(),
            const Icon(Icons.tune_rounded, size: 18, color: Color(0xFF748087)),
            const SizedBox(width: 8),
            const Text(
              'Recently edited',
              style: TextStyle(
                fontFamily: 'Arial',
                fontSize: 13,
                color: Color(0xFF748087),
              ),
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
              itemCount: courses.length,
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: columns,
                crossAxisSpacing: 18,
                mainAxisSpacing: 18,
                childAspectRatio: 1.45,
              ),
              itemBuilder: (context, index) =>
                  _CourseCard(course: courses[index]),
            );
          },
        ),
      ],
    );
  }
}

class _CourseCard extends StatelessWidget {
  const _CourseCard({required this.course});

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
                          fontFamily: 'Arial',
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
                  fontSize: 21,
                  fontWeight: FontWeight.w700,
                  color: Color(0xFF17252D),
                ),
              ),
              const SizedBox(height: 14),
              Row(
                children: [
                  _CourseMeta(
                    label: 'Learning',
                    value: course.learningLanguage,
                  ),
                  const SizedBox(width: 20),
                  _CourseMeta(label: 'Student', value: course.studentLanguage),
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
                        fontFamily: 'Arial',
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
                      fontFamily: 'Arial',
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

class _CourseMeta extends StatelessWidget {
  const _CourseMeta({required this.label, required this.value});

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label.toUpperCase(),
          style: const TextStyle(
            fontFamily: 'Arial',
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
            fontFamily: 'Arial',
            fontSize: 12,
            color: Color(0xFF42535A),
            fontWeight: FontWeight.w700,
          ),
        ),
      ],
    );
  }
}
