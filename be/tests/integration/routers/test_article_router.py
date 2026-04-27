from datetime import datetime, timezone

from api.models import Article, PagedArticles


def test_get_articles(test_client, mock_services, consumer):
    mock_services.article_service.get_articles.return_value = PagedArticles(
        articles=[
            Article(
            id=1,
            uuid="article-uuid",
            title="TITLE_1",
            link="LINK_1",
            description="DESCRIPTION_1",
            pub_date=datetime.now(timezone.utc),
            channel_link="CHANNEL_LINK_1",
            likes=1,
            liked_by_user=False,
            channel_logo="https://example.com/logo.png"
        )],
        has_more=False,
        next_cursor=None
    )

    response = test_client.get("/v1/articles/", params={"hours": 2})
    json_data = response.json()

    mock_services.article_service.get_articles.assert_called_once_with(consumer=consumer, hours=2, order_by_likes=True, cursor=None, query=None)
    assert response.status_code == 200
    assert len(json_data["articles"]) == 1
    assert json_data["articles"][0]["uuid"] == "article-uuid"


def test_get_single_article(test_client, mock_services):
    article = Article(
        id=1,
        uuid="article-uuid",
        title="TITLE_1",
        link="LINK_1",
        description="DESCRIPTION_1",
        pub_date=datetime.now(timezone.utc),
        channel_link="CHANNEL_LINK_1",
        likes=1,
        liked_by_user=False,
        channel_logo="https://example.com/logo.png"
    )
    mock_services.article_service.get_article.return_value = article

    response = test_client.get("/v1/articles/article-uuid")
    json_data = response.json()

    mock_services.article_service.get_article.assert_called_once_with("article-uuid")
    assert response.status_code == 200
    assert json_data["article"]["uuid"] == "article-uuid"


def test_like_article(test_client, mock_services, consumer):
    mock_services.article_service.like_article.return_value = True

    response = test_client.post("/v1/articles/article-uuid/like")
    json_data = response.json()

    mock_services.article_service.like_article.assert_called_once_with("article-uuid", consumer)
    assert response.status_code == 200
    assert json_data == {
        "success": True,
        "message": "Article with uuid article-uuid has been liked.",
        "liked": True,
    }
