abstract class TaskEvent {}

class LoadTasks extends TaskEvent {
  final String userId;

  LoadTasks({required this.userId});
}

class ToggleTask extends TaskEvent {
  final int id;

  ToggleTask(this.id);
}

class AddTask extends TaskEvent {
  final String title;
  final int priority;

  AddTask({
    required this.title,
    required this.priority,
  });
}

