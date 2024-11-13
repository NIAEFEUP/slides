import 'dart:ui';

class NewsArticle {
  String? imageUrl;
  String title;
  String subtitle;
  String? content;

  NewsArticle(
      {this.imageUrl,
      required this.title,
      required this.subtitle,
      this.content});
}
