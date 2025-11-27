import 'package:flutter/material.dart';
import 'package:collection/collection.dart'; // Můžeš přidat do pubspec.yaml pro snazší práci se seznamy
import '../../data/models/post.dart';
// Předpokládáme, že vytvoříš provider pro API komunikaci
// import '../../data/providers/post_api_provider.dart'; 

class PostViewModel extends ChangeNotifier {
  // --- STAV A DATA ---
  List<Post> _posts = [];
  bool _isLoading = false;

  List<Post> get posts => _posts;
  bool get isLoading => _isLoading;

  // Předpokládaná instance API provideru pro volání backendu
  // final PostApiProvider _apiProvider = PostApiProvider();

  // --- LOGIKA NAČÍTÁNÍ ---

  Future<void> fetchPosts() async {
    if (_posts.isNotEmpty) return; // Načítat jen jednou
    
    _isLoading = true;
    notifyListeners();

    // Simulace API volání a načtení dat
    // Zde bys volal _apiProvider.fetchPosts()
    await Future.delayed(const Duration(seconds: 1)); 

    // Simulace načtených dat s DŮLEŽITÝMI NOVÝMI PARAMETRY:
    _posts = [
      Post(
        id: 1, 
        author: 'Kuba', 
        description: 'Máme hotový backend pro summarizaci!', 
        
        // --- NOVÉ POVINNÉ PARAMETRY ---
        publicationDate: DateTime.now().subtract(const Duration(hours: 1)),
        category: 'Development',
        validationText: 'Tento příspěvek je pravdivý!',
        // -----------------------------
        
        likesCount: 42, 
        isVerified: true, 
        isLiked: false
      ),
      Post(
        id: 2, 
        author: 'Kamarád', 
        description: 'Právě pracuji na Flutter frontend UI. Bude to super.', 
        
        // --- NOVÉ POVINNÉ PARAMETRY ---
        publicationDate: DateTime.now().subtract(const Duration(minutes: 30)),
        category: 'Design',
        validationText: 'Pravděpodobně pravdivý.',
        // -----------------------------
        
        likesCount: 15, 
        isVerified: false, 
        isLiked: true
      ),
      Post(
        id: 3, 
        author: 'Uživatel 1', 
        description: 'První testovací příspěvek z nové AI appky.', 
        
        // --- NOVÉ POVINNÉ PARAMETRY ---
        publicationDate: DateTime.now().subtract(const Duration(minutes: 5)),
        category: 'AI/ML',
        validationText: 'Potřebuje ověřit.',
        // -----------------------------
        
        likesCount: 5, 
        isVerified: false, 
        isLiked: false
      ),
    ];
    
    _isLoading = false;
    notifyListeners(); // Oznámí widgetům, že data jsou připravena
  }

  // --- LOGIKA TLAČÍTEK (Zůstává beze změny) ---

  Future<void> toggleLike(int postId) async {
    // 1. Najdi příspěvek v seznamu
    final postIndex = _posts.indexWhere((p) => p.id == postId);
    if (postIndex == -1) return;

    final currentPost = _posts[postIndex];
    final bool newLikedStatus = !currentPost.isLiked;

    // 2. Simulace volání API pro odeslání Like
    // Zde bys volal _apiProvider.sendLike(postId);
    await Future.delayed(const Duration(milliseconds: 300)); 

    // 3. Aktualizace lokálního stavu
    _posts[postIndex] = currentPost.copyWith(
      isLiked: newLikedStatus,
      likesCount: currentPost.likesCount + (newLikedStatus ? 1 : -1),
    );
    
    notifyListeners(); // Oznámí UI, že má překreslit srdíčko a počet
  }
  
  Future<void> verifyPost(int postId) async {
    // 1. Najdi příspěvek v seznamu
    final postIndex = _posts.indexWhere((p) => p.id == postId);
    if (postIndex == -1) return;

    // Zabráníme ověření, pokud už je ověřen
    if (_posts[postIndex].isVerified) return;

    // 2. Simulace volání API pro odeslání Ověření
    // Zde bys volal _apiProvider.verifyPost(postId);
    await Future.delayed(const Duration(milliseconds: 500)); 

    // 3. Aktualizace lokálního stavu
    _posts[postIndex] = _posts[postIndex].copyWith(isVerified: true);
    
    notifyListeners(); // Oznámí UI, že se má zobrazit ikona ověření
  }
}