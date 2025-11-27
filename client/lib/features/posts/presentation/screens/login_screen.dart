import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodels/account_view_model.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _isLoading = false;

  Future<void> _submit() async {
    if (_formKey.currentState!.validate()) {
      setState(() { _isLoading = true; });
      
      final viewModel = Provider.of<AccountViewModel>(context, listen: false);
      
      // Simulace API volání pro login (Zde bys volal API provider)
      await Future.delayed(const Duration(seconds: 1)); 

      // Po úspěšném loginu (zde simulováno, že je vždy úspěšný)
      viewModel.toggleAuthStatus(); // Přepneme na přihlášený stav
      
      if (mounted) {
        setState(() { _isLoading = false; });
        Navigator.of(context).pop(); // Zavře login formulář
        Navigator.of(context).pop(); // Zavře AccountScreen (pokud byla otevřena)
      }
    }
  }

  @override
Widget build(BuildContext context) {
  // Výška celé obrazovky mínus výška App baru
  final screenHeight = MediaQuery.of(context).size.height;
  final appBarHeight = AppBar().preferredSize.height;
  final finalHeight = screenHeight - appBarHeight;

  return Scaffold(
    appBar: AppBar(
      iconTheme: IconThemeData(color: Colors.white),
        toolbarHeight: 150.0,
        backgroundColor: Colors.blueAccent,
        title: Text("Přihlášení",
        style: const TextStyle(
              color: Colors.white, // Bílý text
              fontSize: 40,
              fontWeight: FontWeight.bold,
            ),),
        centerTitle: true,
      ),
    body: SingleChildScrollView(
      padding: const EdgeInsets.all(24.0),
      child: Center(
        child: ConstrainedBox(
          constraints: const BoxConstraints(maxWidth: 400),
          child: SizedBox( 
            height: finalHeight * 0.9, 
            child: Form(
              key: _formKey,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: <Widget>[
                  TextFormField(
                    controller: _emailController,
                    keyboardType: TextInputType.emailAddress,
                    decoration: const InputDecoration(
                      labelText: 'E-mail',
                      prefixIcon: Icon(Icons.email),
                      border: OutlineInputBorder(),
                    ),
                    validator: (value) {
                      if (value == null || !value.contains('@')) {
                        return 'Zadejte platný e-mail.';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 20),
                  TextFormField(
                    controller: _passwordController,
                    obscureText: true,
                    decoration: const InputDecoration(
                      labelText: 'Heslo',
                      prefixIcon: Icon(Icons.lock),
                      border: OutlineInputBorder(),
                    ),
                    
                    validator: (value) {
                      if (value == null || value.length < 6) {
                        return 'Heslo musí mít alespoň 6 znaků.';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 30),
                  _isLoading
                      ? const Center(child: CircularProgressIndicator())
                      : ElevatedButton(
                          onPressed: _submit,
                          style: ElevatedButton.styleFrom(
                            padding: const EdgeInsets.symmetric(vertical: 20),
                            backgroundColor: Colors.blueAccent,
                          ),
                          child: const Text('Přihlásit se', style: TextStyle(fontSize: 24, color: Colors.white)),
                        ),
                ],
              ),
            ),
          ),
        ),
      ),
    ),
  );
}
}