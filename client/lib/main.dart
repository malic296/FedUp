import 'package:flutter/material.dart';
import 'package:client/api/generated/openapi.dart';
import 'package:dio/dio.dart';
import 'package:provider/provider.dart';
import 'features/posts/presentation/screens/home_screen.dart';
import 'features/posts/presentation/viewmodels/post_view_model.dart';
import 'features/posts/presentation/viewmodels/account_view_model.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // -------------------------------------------------------------
  // 👉 UPDATE THIS LINE according to the device you run on:
  //   - Chrome (web)          → http://127.0.0.1:8000
  //   - Android emulator      → http://10.0.2.2:8000
  //   - Physical device LAN  → http://<YOUR_PC_IP>:8000
  // -------------------------------------------------------------
  static final _openapi = Openapi(
    basePathOverride: 'http://127.0.0.1:8000', // change if needed
  );

  static final UsersApi _usersApi = _openapi.getUsersApi();
  static final NewsApi  _newsApi  = _openapi.getNewsApi();

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        // Zaregistrujeme View Model
        ChangeNotifierProvider(create: (_) => PostViewModel()),
        
        // ZAREGISTRUJEME NOVÝ VIEW MODEL PRO ÚČET
        ChangeNotifierProvider(create: (_) => AccountViewModel()),
      ],
      child: MaterialApp(
        title: 'FedUp App',
        theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
        home: const HomeScreen(),
      ),
    );
  }
}

// =============================================================
//  ApiDemoWidget – fetches data and shows it
// =============================================================
class ApiDemoWidget extends StatefulWidget {
  final UsersApi usersApi;
  final NewsApi newsApi;

  const ApiDemoWidget({
    super.key,
    required this.usersApi,
    required this.newsApi,
  });

  @override
  State<ApiDemoWidget> createState() => _ApiDemoWidgetState();
}

class _ApiDemoWidgetState extends State<ApiDemoWidget> {
  bool _loading = true;
  String? _error;
  dynamic _usersResult;
  dynamic _newsResult;

  @override
  void initState() {
    super.initState();
    _loadFromServer();
  }

  Future<void> _loadFromServer() async {
    try {
      // NOTE: These are the exact method names generated from your spec
      final users = await widget.usersApi.getUsernameUsersGet();
      final news  = await widget.newsApi.testNewsNewsGet();

      setState(() {
        _usersResult = users;
        _newsResult  = news;
        _loading     = false;
      });
    } on DioException catch (e) {
      // Show a detailed error so you can see what went wrong
      setState(() {
        _error = '''
❌ DioException:
  type: ${e.type}
  message: ${e.message}
  uri: ${e.requestOptions.uri}
  statusCode: ${e.response?.statusCode}
  data: ${e.response?.data}
''';
        _loading = false;
      });
    } catch (e) {
      setState(() {
        _error = 'Unexpected error: $e';
        _loading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_loading) {
      return const Center(child: CircularProgressIndicator());
    }
    if (_error != null) {
      return Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(_error!,
              style: const TextStyle(color: Colors.red, fontSize: 14)),
        ),
      );
    }
    return SingleChildScrollView(
      padding: const EdgeInsets.all(16),
      child: Text(_formatResult(),
          style: const TextStyle(fontFamily: 'monospace', fontSize: 14)),
    );
  }

  String _formatResult() {
    final sb = StringBuffer();
    sb.writeln('=== Users ===');
    sb.writeln(_usersResult?.toString() ?? 'No users returned');
    sb.writeln('\n=== News ===');
    sb.writeln(_newsResult?.toString() ?? 'No news returned');
    return sb.toString();
  }
}