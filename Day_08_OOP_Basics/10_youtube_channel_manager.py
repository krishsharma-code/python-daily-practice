class YouTubeChannel:
    """
    Manages stats for the 'Rise and Shine' YouTube channel.
    """
    def __init__(self, channel_name):
        self.channel_name = channel_name
        self.subscribers = 0
        self.videos = []
        self.total_views = 0

    def upload_video(self, title, views):
        self.videos.append(title)
        self.total_views += views
        print(f"Uploaded: '{title}' to {self.channel_name}.")

    def add_subscribers(self, count):
        self.subscribers += count

    def get_engagement_score(self):
        if not self.videos:
            return 0
        return self.total_views / len(self.videos)

# Channel Management
my_channel = YouTubeChannel("Rise and Shine")
my_channel.add_subscribers(1000)
my_channel.upload_video("Python OOP for Beginners", 5000)
my_channel.upload_video("Daily Motivation", 3000)

print(f"Channel: {my_channel.channel_name}")
print(f"Subscribers: {my_channel.subscribers}")
print(f"Average Views (Engagement): {my_channel.get_engagement_score()}")
