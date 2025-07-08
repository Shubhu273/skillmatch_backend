from youtubesearchpython import VideosSearch

def get_courses_for_skill(skill):
    search = VideosSearch(f"{skill} tutorial for beginners", limit=3)
    results = search.result()['result']
    return [{'title': v['title'], 'url': v['link']} for v in results]
