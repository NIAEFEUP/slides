import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:workshop_demo/model/news_article.dart';

class NewsDetailsPage extends StatelessWidget {
  final NewsArticle article;

  const NewsDetailsPage(this.article, {super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Theme.of(context).colorScheme.inversePrimary,
          title: Text(article.title),
        ),
        body: ListView(children: [
          if (article.imageUrl != null) Image.network(article.imageUrl!),
          Text(article.title, style: const TextStyle(fontSize: 20),),
          if (article.content != null) Text(article.content!),
        ]));
  }
}
