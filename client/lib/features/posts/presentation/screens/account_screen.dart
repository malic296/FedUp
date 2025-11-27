import 'package:client/features/posts/presentation/screens/login_screen.dart';
import 'package:client/features/posts/presentation/screens/register_screen.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodels/account_view_model.dart'; // Import nového View Modelu

class AccountScreen extends StatelessWidget {
  const AccountScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // Používáme Consumer pro naslouchání stavu přihlášení
    return Consumer<AccountViewModel>(
      builder: (context, accountViewModel, child) {
        return Scaffold(
          appBar: AppBar(
            iconTheme: IconThemeData(color: Colors.white),
            toolbarHeight: 150.0,
            backgroundColor: Colors.blueAccent,
            title: Row(
              children: [
                accountViewModel.isLoggedIn ?  
                Text('Správa účtu',
                style: const TextStyle(
                      color: Colors.white, // Bílý text
                      fontSize: 40,
                      fontWeight: FontWeight.bold,
                      ),
                      textAlign: TextAlign.center,
                    )
                : 
                Image(
                  image: AssetImage('assets/logos/fedup_logo.png'),
                  fit: BoxFit.cover,
                  height: 400,
                  width: 400,
                )
              ],
            ),
            centerTitle: true,
      ),
          body: Padding(
            padding: const EdgeInsets.all(24.0),
            child: accountViewModel.isLoggedIn
                ? const _AccountManagementContent() // Přihlášený obsah
                : const _AuthButtonsContent(), // Nepřihlášený obsah
          ),
        );
      },
    );
  }
}

// --- OBSAH PRO NEPŘIHLÁŠENÉ UŽIVATELE (Login/Register) ---

class _AuthButtonsContent extends StatelessWidget {
  const _AuthButtonsContent();

  @override
  Widget build(BuildContext context) {

    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        
        const Text(
          'Vítej!',
          style: TextStyle(fontSize: 120, fontWeight: FontWeight.bold),
          textAlign: TextAlign.center,
        ),
        const SizedBox(height: 40),
        
        // Tlačítko Přihlášení
        ElevatedButton(
          onPressed: () {
            // NAVIGACE NA LOGIN SCREEN
            Navigator.of(context).push(
              MaterialPageRoute(
                builder: (context) => const LoginScreen(),
              ),
            );
          },
          style: ElevatedButton.styleFrom(
            padding: const EdgeInsets.symmetric(vertical: 15),
            backgroundColor: Colors.blue,
          ),
          child: const Text('Přihlásit se', style: TextStyle(fontSize: 18, color: Colors.white)),
        ),
        const SizedBox(height: 20),

        // Tlačítko Registrace
        OutlinedButton(
          onPressed: () {
            // NAVIGACE NA REGISTER SCREEN
             Navigator.of(context).push(
              MaterialPageRoute(
                builder: (context) => const RegisterScreen(),
              ),
            );
          },
          style: OutlinedButton.styleFrom(
            padding: const EdgeInsets.symmetric(vertical: 15),
            side: const BorderSide(color: Colors.blue),
          ),
          child: const Text('Zaregistrovat se', style: TextStyle(fontSize: 18, color: Colors.blue)),
        ),
      ],
    );
  }
}

// --- OBSAH PRO PŘIHLÁŠENÉ UŽIVATELE (Změna Jména/Hesla) ---

class _AccountManagementContent extends StatefulWidget {
  const _AccountManagementContent();

  @override
  State<_AccountManagementContent> createState() => _AccountManagementContentState();
}

class _AccountManagementContentState extends State<_AccountManagementContent> {
  final _usernameController = TextEditingController();
  final _oldPasswordController = TextEditingController();
  final _newPasswordController = TextEditingController();

  @override
  void dispose() {
    _usernameController.dispose();
    _oldPasswordController.dispose();
    _newPasswordController.dispose();
    super.dispose();
  }

  void _showSnackbar(String message, Color color) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: color,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final viewModel = Provider.of<AccountViewModel>(context);

    // Nastavíme výchozí hodnotu pro editaci jména
    _usernameController.text = viewModel.username;

    return SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Text(
            'Ahoj, ${viewModel.username}!', // Personalizace
            style: Theme.of(context).textTheme.headlineMedium,
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 30),

          // --- SEKCE ZMĚNA JMÉNA ---
          Text(
            'Změnit uživatelské jméno', 
            style: Theme.of(context).textTheme.titleLarge,
          ),
          const SizedBox(height: 10),
          TextField(
            controller: _usernameController,
            decoration: const InputDecoration(
              labelText: 'Nové uživatelské jméno',
              border: OutlineInputBorder(),
            ),
          ),
          const SizedBox(height: 10),
          ElevatedButton(
            onPressed: () async {
              final result = await viewModel.changeUsername(_usernameController.text);
              _showSnackbar(result, result.contains('úspěšně') ? Colors.green : Colors.red);
            },
            child: const Text('Uložit jméno'),
          ),
          const Divider(height: 40),

          // --- SEKCE ZMĚNA HESLA ---
          Text(
            'Změnit heslo', 
            style: Theme.of(context).textTheme.titleLarge,
          ),
          const SizedBox(height: 10),
          TextField(
            controller: _oldPasswordController,
            obscureText: true,
            decoration: const InputDecoration(
              labelText: 'Staré heslo',
              border: OutlineInputBorder(),
            ),
          ),
          const SizedBox(height: 10),
          TextField(
            controller: _newPasswordController,
            obscureText: true,
            decoration: const InputDecoration(
              labelText: 'Nové heslo',
              border: OutlineInputBorder(),
            ),
          ),
          const SizedBox(height: 10),
          ElevatedButton(
            onPressed: () async {
              final result = await viewModel.changePassword(
                _oldPasswordController.text,
                _newPasswordController.text,
              );
              _showSnackbar(result, result.contains('úspěšně') ? Colors.green : Colors.red);
              _oldPasswordController.clear();
              _newPasswordController.clear();
            },
            child: const Text('Uložit heslo'),
          ),
          const SizedBox(height: 50),
          
          // --- TLAČÍTKO ODHLÁSIT SE ---
          OutlinedButton(
            onPressed: () {
              viewModel.toggleAuthStatus(); // Nastaví isLoggedIn na false
              Navigator.of(context).pop(); // Zavře AccountScreen
            },
            style: OutlinedButton.styleFrom(
              padding: const EdgeInsets.symmetric(vertical: 15),
              side: const BorderSide(color: Colors.red),
            ),
            child: const Text('Odhlásit se', style: TextStyle(fontSize: 18, color: Colors.red)),
          ),
        ],
      ),
    );
  }
}