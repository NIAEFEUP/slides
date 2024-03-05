import 'dart:convert';

import 'package:http/http.dart';

import '../model/news_article.dart';

Future<List<NewsArticle>> fetchArticles(String category) async {
  final response = await get(Uri.parse(
      "https://saurav.tech/NewsAPI/top-headlines/category/$category/in.json"));
  final json = jsonDecode(response.body);
  final articles = (json["articles"] as List).map((article) {
    return NewsArticle(
        title: article["title"],
        subtitle: article["description"],
        content: article["content"],
        imageUrl: article["urlToImage"]);
  }).toList();
  return articles;
}
