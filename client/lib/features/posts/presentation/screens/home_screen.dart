import 'package:client/features/posts/presentation/screens/account_screen.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../viewmodels/post_view_model.dart';
import '../widgets/post_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

// Přidáme TickerProviderStateMixin pro práci s AnimationController
class _HomeScreenState extends State<HomeScreen> with SingleTickerProviderStateMixin {
  
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    // Inicializace kontroleru animace
    _controller = AnimationController(
      duration: const Duration(seconds: 2), // Délka animace
      vsync: this,
    );
    
    // Nastavení animace: Fade a Scale
    _animation = Tween<double>(begin: 0.8, end: 1.0)
        .animate(CurvedAnimation(parent: _controller, curve: Curves.easeInOut));

    // Opakování animace (pulsní efekt)
    _controller.repeat(reverse: true);

    // Načtení dat (přesunuto sem z build metody)
    WidgetsBinding.instance.addPostFrameCallback((_) {
      Provider.of<PostViewModel>(context, listen: false).fetchPosts();
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Pozor: Zde již nevoláme fetchPosts, voláme ho v initState!

    return Scaffold(
      appBar: AppBar(
        iconTheme: IconThemeData(color: Colors.white),
        toolbarHeight: 150.0,
        backgroundColor: Colors.blueAccent,
        title: 
        
        ScaleTransition(
          scale: _animation, 
          child: Opacity( 
            opacity: _animation.value,
            child: Image(image: AssetImage('assets/logos/fedup_logo.png'))
          ),
        ),
        
        actions: [
          
          Tooltip(
            message: 'Můj účet', 
            verticalOffset: 60, 
            decoration: BoxDecoration(
              color: Colors.black87, 
              borderRadius: BorderRadius.circular(8),
            ),
            textStyle: const TextStyle(
              color: Colors.white, 
              fontSize: 16,
              fontWeight: FontWeight.bold,
            ),
            child: IconButton(
              icon: const Icon(Icons.account_circle, size: 80, color: Colors.white,),
              onPressed: () {
                Navigator.of(context).push(
                  MaterialPageRoute(
                    builder: (context) => const AccountScreen(),
                  ),
                );
              },
            ),
          ),
          const SizedBox(width: 8),
        ],
      ),
   
      body: Consumer<PostViewModel>( 
        builder: (context, viewModel, child) {
          if (viewModel.isLoading) {
            return const Center(child: CircularProgressIndicator()); 
          }

          if (viewModel.posts.isEmpty) {
            return const Center(child: Text('Nebyly nalezeny žádné příspěvky.')); 
          }

          return ListView.builder(
            padding: const EdgeInsets.all(8.0),
            itemCount: viewModel.posts.length,
            itemBuilder: (context, index) {
              final post = viewModel.posts[index];
              return PostCard(post: post);
            },
          );
        },
      ),
    );
  }
}