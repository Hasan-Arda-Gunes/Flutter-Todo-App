class Task {
  final int id;
  final String title;
  final bool isDone;
  final int priority;
  final String? dueDate;
  final String user_id;

  Task({
    required this.id,
    required this.title,
    required this.isDone,
    required this.priority,
    this.dueDate,
    required this.user_id
  });

  factory Task.fromJson(Map<String, dynamic> json) {
    return Task(
      id: json['id'],
      title: json['title'],
      isDone: json['isDone'],
      priority: json['priority'],
      dueDate: json['due_date'],
      user_id: json["user_id"],
    );
  }
}
