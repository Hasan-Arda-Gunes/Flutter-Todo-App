import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';


class AuthService {
  static Future<bool> register(String username, String password) async {
  final url = Uri.parse('http://localhost:8000/users/register/');

  final response = await http.post(
    url,
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'username': username, 'password': password}),
  );

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    final token = data['access_token'];

    // Save token locally
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('token', token);

    return true;
  } else {
    print("Login failed: ${response.body}");
    return false;
  }
}


  static Future<bool> login(String username, String password) async {
  final url = Uri.parse('http://localhost:8000/users/login/');

  final response = await http.post(
    url,
    headers: {'Content-Type': 'application/json'},
    body: jsonEncode({'username': username, 'password': password}),
  );

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body);
    final token = data['access_token'];

    // Save token locally
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('token', token);

    return true;
  } else {
    print("Login failed: ${response.body}");
    return false;
  }
}


}