import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
// Předpokládáme, že máš model Post
import '../../../posts/data/models/post.dart'; 
import '../viewmodels/post_view_model.dart';

class PostCard extends StatelessWidget {
  final Post post;

  const PostCard({super.key, required this.post});

  @override
  Widget build(BuildContext context) {
    final viewModel = Provider.of<PostViewModel>(context, listen: false);

    return Card(
      margin: const EdgeInsets.only(bottom: 16.0),
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // --- 1. HLAVIČKA (Autor a Ověření) ---
            _buildHeader(context),
            const SizedBox(height: 10),

            // --- 2. TĚLO (Popis) ---
            Text(
              post.description,
              style: Theme.of(context).textTheme.bodyLarge,
            ),
            const SizedBox(height: 15),

            // --- 3. PATIČKA (Tlačítka) ---
            _buildActions(context, viewModel),
          ],
        ),
      ),
    );
  }

  Widget _buildHeader(BuildContext context) {
    return Row(
      children: [
        const CircleAvatar(
          child: Icon(Icons.person), // Avatar
        ),
        const SizedBox(width: 10),
        Expanded(
          child: Text(
            post.author, // Název autora
            style: Theme.of(context).textTheme.titleMedium,
            overflow: TextOverflow.ellipsis,
          ),
        ),
        // Indikátor ověření
        if (post.isVerified)
          const Icon(Icons.verified, color: Colors.blue, size: 20),
      ],
    );
  }

  Widget _buildActions(BuildContext context, PostViewModel viewModel) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        // Tlačítko LIKE (Srdíčko)
        Row(
          children: [
            IconButton(
              icon: Icon(
                post.isLiked ? Icons.favorite : Icons.favorite_border,
                color: post.isLiked ? Colors.red : Colors.grey,
              ),
              onPressed: () {
                // Zavolání metody z View Modelu pro odeslání Like
                viewModel.toggleLike(post.id); 
              },
            ),
            Text('${post.likesCount}'),
          ],
        ),

        // Tlačítko VERIFY (Ověření)
        ElevatedButton.icon(
          icon: const Icon(Icons.check_circle_outline, color: Colors.white,),
          label: const Text('Ověřit', style: TextStyle(color: Colors.white),),
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.blueAccent,
          ),
          onPressed: () {
            // Zavolání metody z View Modelu pro ověření příspěvku
            viewModel.verifyPost(post.id);
          },
        ),
      ],
    );
  }
}