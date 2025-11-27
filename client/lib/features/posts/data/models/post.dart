class Post {
  final int id;
  // Mapování: DTO 'generatedText' -> Post 'description'
  final String description; 
  
  // Mapování: DTO 'link' -> Post 'author' (Používáme 'link' jako zástupce autora/zdroje)
  final String author; 
  
  // Nová pole z DTO
  final DateTime publicationDate;
  final String category;
  final String validationText;

  // Pole pro stav (frontend-only, v DTO neexistují, proto mají defaultní hodnoty)
  final int likesCount; 
  final bool isVerified;
  final bool isLiked;

  Post({
    required this.id,
    required this.author,
    required this.description,
    required this.publicationDate,
    required this.category,
    required this.validationText,
    this.likesCount = 0,
    this.isVerified = false,
    this.isLiked = false,
  });

  // Metoda pro vytvoření nové instance Post s aktualizovanými daty
  // (Potřebné pro Provider / Immutabilitu)
  Post copyWith({
    int? id,
    String? author,
    String? description,
    DateTime? publicationDate,
    String? category,
    String? validationText,
    int? likesCount,
    bool? isVerified,
    bool? isLiked,
  }) {
    return Post(
      id: id ?? this.id,
      author: author ?? this.author,
      description: description ?? this.description,
      publicationDate: publicationDate ?? this.publicationDate,
      category: category ?? this.category,
      validationText: validationText ?? this.validationText,
      likesCount: likesCount ?? this.likesCount,
      isVerified: isVerified ?? this.isVerified,
      isLiked: isLiked ?? this.isLiked,
    );
  }

  // --- FACTORY METODA PRO PARSOVÁNÍ JSONU (DTO) ---
  factory Post.fromJson(Map<String, dynamic> json) {
    // Pydantic datetime odesílá datum jako ISO 8601 string, 
    // který Dart umí jednoduše převést.
    final String dateString = json['publicationDate'] as String;
    final DateTime parsedDate = DateTime.parse(dateString);

    return Post(
      // 1. Mapování klíčů z DTO na Dart vlastnosti
      id: json['id'] as int,
      author: json['link'] as String, // DTO 'link' -> Post 'author' (jako zdroj/url)
      description: json['generatedText'] as String, // DTO 'generatedText' -> Post 'description'
      
      // 2. Přímé mapování z DTO
      publicationDate: parsedDate,
      category: json['category'] as String,
      validationText: json['validationText'] as String,
      
      // 3. Frontend stavy (defaultní hodnoty, protože nejsou v DTO)
      likesCount: 0, 
      isVerified: false, 
      isLiked: false,
    );
  }
}