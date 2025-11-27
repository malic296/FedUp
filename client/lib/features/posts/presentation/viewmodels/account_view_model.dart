import 'package:flutter/material.dart';

class AccountViewModel extends ChangeNotifier {
  // --- STAV ---
  bool _isLoggedIn = false;
  String _username = 'Kubix_21';

  bool get isLoggedIn => _isLoggedIn;
  String get username => _username;

  // --- AKCE PRO APP BAR ---

  void toggleAuthStatus() {
    _isLoggedIn = !_isLoggedIn;
    // Resetování jména pro simulaci odhlášení/přihlášení
    _username = _isLoggedIn ? 'Nový Uživatelský Účet' : 'Kubix_21'; 
    notifyListeners();
  }

  // --- AKCE PRO SPRÁVU ÚČTU ---
  
  // Simulace změny uživatelského jména
  Future<String> changeUsername(String newUsername) async {
    await Future.delayed(const Duration(milliseconds: 500)); 
    if (newUsername.isEmpty) return 'Jméno nesmí být prázdné.';
    
    // Zde by bylo volání API
    // if (api_call_success) { ... }
    _username = newUsername;
    notifyListeners();
    return 'Jméno úspěšně změněno.';
  }

  // Simulace změny hesla
  Future<String> changePassword(String currentPassword, String newPassword) async {
    await Future.delayed(const Duration(milliseconds: 500)); 
    if (currentPassword.isEmpty || newPassword.isEmpty) return 'Hesla nesmí být prázdná.';
    
    // Zde by bylo volání API s validací starého hesla
    // ...
    return 'Heslo bylo úspěšně změněno.';
  }
}