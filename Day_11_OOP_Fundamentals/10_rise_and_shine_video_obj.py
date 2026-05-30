# Day 11: Rise and Shine Video Object
# Concept: Class to handle YouTube video metadata, SEO tags, and view counts.

class YouTubeVideo:
    def __init__(self, title, channel, tags):
        self.title = title
        self.channel = channel
        self.tags = list(tags)
        self.views = 0
        self.is_published = False

    def publish(self):
        self.is_published = True
        print(f"Video '{self.title}' is now LIVE on {self.channel}!")

    def add_view(self, count=1):
        if self.is_published:
            self.views += count
        else:
            print("Cannot add views to an unpublished video.")

    def get_seo_report(self):
        print(f"\n--- SEO Report for '{self.title}' ---")
        print(f"Tags: {', '.join(self.tags)}")
        print(f"Total Views: {self.views}")

# Creating a video object
morning_vlog = YouTubeVideo(
    "Rise and Shine: 5AM Coding Routine", 
    "Krish Python Dev", 
    ["Python", "Productivity", "Coding", "RiseAndShine"]
)

morning_vlog.publish()
morning_vlog.add_view(1500)
morning_vlog.get_seo_report()
