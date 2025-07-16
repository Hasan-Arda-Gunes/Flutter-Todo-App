import 'package:flutter_bloc/flutter_bloc.dart';
import '../models/task.dart';
import 'task_event.dart';
import 'task_state.dart';
import '../service/task_service.dart';

class TaskBloc extends Bloc<TaskEvent, TaskState> {
  TaskBloc() : super(TaskLoadingState()) {
    // Load tasks from backend
    on<LoadTasks>((event, emit) async {
      emit(TaskLoadingState());
      try {
        final tasks = await TaskService.fetchTasks();
        emit(TaskLoadedState(tasks));
      } catch (e) {
        emit(TaskErrorState('Failed to load tasks'));
      }
    });

    // Toggle task done status
    on<ToggleTask>((event, emit) async {
      if (state is TaskLoadedState) {
        final currentState = state as TaskLoadedState;

        final success = await TaskService.toggleTask(event.id);
        if (success) {
          // Update the local copy of tasks in Bloc
          final updatedTasks = currentState.tasks.map((task) {
            if (task.id == event.id) {
              return Task(
                id: task.id,
                title: task.title,
                isDone: !task.isDone,
                priority: task.priority,
                dueDate: task.dueDate,
                user_id: task.user_id,
              );
            }
            return task;
          }).toList();

          emit(TaskLoadedState(updatedTasks));
        } else {
          emit(TaskErrorState('Failed to toggle task'));
        }
      }
    });

    on<AddTask>((event, emit) async {
  if (state is TaskLoadedState) {
    final currentState = state as TaskLoadedState;
    final success = await TaskService.addTask(
        event.title, event.priority, event.dueDate,);

    if (success) {
      try {
        final tasks = await TaskService.fetchTasks();
        emit(TaskLoadedState(tasks));
      } catch (_) {
        emit(TaskErrorState("Failed to fetch tasks after adding"));
      }
    } else {
      emit(TaskErrorState("Failed to add task"));
    }
  }
});
  }
}
