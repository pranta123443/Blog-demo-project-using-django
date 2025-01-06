from datetime import date

from django.shortcuts import render

all_posts = [
{
  "slug": "hike-in-the-mountains",
  "image": "1.png",
  "date": date(2025, 1, 1),
  "title": "Mountain Hiking",
  "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
  "content": """ Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """
},
{
  "slug": "all-about-me",
  "image": "2.jpg",
  "date": date(2025, 2, 12),
  "title": "Cycling",
  "excerpt": "dw There's nothLorem ipsum dolor sit amsn't even prepared for what happened whilst I was enjoying the view!",
  "content": """ Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """
},
{
  "slug": "all-right",
  "image": "3.jpg",
  "date": date(2025, 2, 14),
  "title": "Swiming",
  "excerpt": "dwad There's notem ipsum dolor sit amet, consectetur adipisI wasn't even prepared for what happened whilst I was enjoying the view!",
  "content": """ repared for what happened whilst I was enjolit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. """
}
]
def get_date(post):
  return post['date']
# Create your views here.

def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date)
  latest_posts = sorted_posts[-3:]
  return render(request, "blog_content/index.html", {
    "posts": latest_posts
  })

def posts(request):
  return render(request, "blog_content/all-post.html", {
    "all_posts": all_posts
  })

def post_detail(request, slug):
  identified_post = next(post for post in all_posts if post['slug'] == slug)
  return render(request, "blog_content/post-detail.html", {
    "post": identified_post

  })