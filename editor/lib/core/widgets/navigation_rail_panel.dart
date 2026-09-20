import 'package:flutter/material.dart';

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
