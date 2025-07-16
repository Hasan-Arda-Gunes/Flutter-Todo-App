import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/task.dart';

class TaskService {
  static const String baseUrl = 'http://localhost:8000/tasks';

  // Fetch all tasks for the current user
  static Future<List<Task>> fetchTasks() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('token');

    final url = Uri.parse('$baseUrl/get');
    final response = await http.get(
    url,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer $token',
    },
  );

    if (response.statusCode == 200) {
      final List<dynamic> jsonList = jsonDecode(response.body);
      return jsonList.map((json) => Task.fromJson(json)).toList();
    } else {
      throw Exception('Failed to load tasks');
    }
  }

  // Toggle task by title
  static Future<bool> toggleTask(int id) async {
    final url = Uri.parse('$baseUrl/toggle');
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('token');


    final response = await http.post(
      url,
      headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer $token',
    },
      body: jsonEncode({'id': id}),
    );

    if (response.statusCode == 200 )  {
      return true;
    } else {
      print('Toggle failed: ${response.body}');
      return false;
    }
  }

  static Future<bool> addTask(String title, int priority, DateTime? dueDate) async {
  final url = Uri.parse('$baseUrl/create');  // or whatever your endpoint is

  final prefs = await SharedPreferences.getInstance();
  final token = prefs.getString('token');

  final response = await http.post(
    url,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer $token',
    },
    body: jsonEncode({
      'title': title,
      'priority': priority,
      if (dueDate != null) 'due_date': dueDate.toIso8601String(),
    }),
  );

  if ((response.statusCode == 200 || response.statusCode == 201)) {
    return true;
  } else {
    print('Add task failed: ${response.body}');
    return false;
  }
}

}
