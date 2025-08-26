import requests

def fetch_hackernews_posts(limit=10):
    """
    Fetch the latest top posts from Hacker News.
    """
    top_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:limit]
    posts = []
    for id in top_ids:
        item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json").json()
        posts.append({"title": item.get("title", ""), "score": item.get("score", 0)})
    return posts


def fetch_trending_topics(limit=10, min_score=100):
    """
    Fetch trending Hacker News topics based on score.
    Args:
        limit: Number of trending topics to return
        min_score: Minimum score threshold for trending
    Returns:
        List of dicts with title, score, and url
    """
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    item_url = "https://hacker-news.firebaseio.com/v0/item/{}.json"

    story_ids = requests.get(top_stories_url).json()
    trending = []

    for story_id in story_ids[:100]:  # scan first 100 top stories
        story = requests.get(item_url.format(story_id)).json()
        if story and story.get("score", 0) >= min_score:
            trending.append({
                "title": story.get("title", ""),
                "score": story.get("score", 0),
                "url": story.get("url", f"https://news.ycombinator.com/item?id={story_id}")
            })
        if len(trending) >= limit:
            break

    return trending
