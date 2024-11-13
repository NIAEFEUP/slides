import 'package:flutter/material.dart';
import 'package:workshop_demo/model/news_article.dart';
import 'package:workshop_demo/view/news_details.dart';

class NewsCard extends StatelessWidget {
  const NewsCard(this.article, {super.key});

  final NewsArticle article;

  @override
  Widget build(BuildContext context) {
    return InkWell(
        onTap: () => Navigator.push(context,
            MaterialPageRoute(builder: (context) => NewsDetailsPage(article))),
        child: Card(
            child: Row(
          children: [
            Container(
                padding: const EdgeInsets.all(10),
                width: 150,
                height: 150,
                child: Image.network(
                    article.imageUrl ??
                        "https://image.cnbcfm.com/api/v1/image/105692413-1548173252068gettyimages-450710900.jpeg?v=1548173273",
                    fit: BoxFit.cover)),
            const SizedBox(
              width: 5,
            ),
            // We need to "expand this widget" to give it intrinsic width in the row
            // Otherwise the text would overflow
            Expanded(
                child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  article.title,
                  style: const TextStyle(fontSize: 20),
                ),
                Text(article.subtitle),
              ],
            ))
          ],
        )));
  }
}
