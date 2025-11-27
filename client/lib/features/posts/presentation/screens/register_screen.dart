import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodels/account_view_model.dart';

class RegisterScreen extends StatefulWidget {
  const RegisterScreen({super.key});

  @override
  State<RegisterScreen> createState() => _RegisterScreenState();
}

class _RegisterScreenState extends State<RegisterScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();
  bool _isLoading = false;

  Future<void> _submit() async {
    if (_formKey.currentState!.validate()) {
      setState(() { _isLoading = true; });

      final viewModel = Provider.of<AccountViewModel>(context, listen: false);

      // Simulace API volání pro registraci (Zde bys volal API provider)
      await Future.delayed(const Duration(seconds: 1)); 

      // Po úspěšné registraci (zde simulováno, že je vždy úspěšná)
      // Často se po registraci rovnou přihlásíš
      viewModel.toggleAuthStatus(); 
      
      if (mounted) {
        setState(() { _isLoading = false; });
        // Informujeme uživatele
        ScaffoldMessenger.of(context).showSnackBar(
           const SnackBar(content: Text('Registrace úspěšná! Byli jste přihlášeni.')),
        );
        Navigator.of(context).pop(); // Zavře registrační formulář
        Navigator.of(context).pop(); // Zavře AccountScreen
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    // 1. Získáme výšku obrazovky a App Baru pro správné centrování
    final screenHeight = MediaQuery.of(context).size.height;
    final appBarHeight = AppBar().preferredSize.height;
    // Výška, kterou má k dispozici tělo (body)
    final availableHeight = screenHeight - appBarHeight;
    
    return Scaffold(
      appBar: AppBar(
        iconTheme: IconThemeData(color: Colors.white),
        toolbarHeight: 150.0,
        backgroundColor: Colors.blueAccent,
        title: Text("Registrace",
        style: const TextStyle(
              color: Colors.white, 
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
              height: availableHeight * 0.9, 
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
                      validator: (value) => (value == null || !value.contains('@')) ? 'Zadejte platný e-mail.' : null,
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
                      validator: (value) => (value == null || value.length < 6) ? 'Heslo musí mít alespoň 6 znaků.' : null,
                    ),
                    const SizedBox(height: 20),
                    
               
                    TextFormField(
                      controller: _confirmPasswordController,
                      obscureText: true,
                      decoration: const InputDecoration(
                        labelText: 'Potvrzení hesla',
                        prefixIcon: Icon(Icons.lock_reset),
                        border: OutlineInputBorder(),
                      ),
                      validator: (value) {
                        if (value != _passwordController.text) {
                          return 'Hesla se neshodují.';
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
                            child: const Text('Registrovat se', style: TextStyle(fontSize: 24, color: Colors.white)), 
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