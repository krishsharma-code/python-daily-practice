class YouTubeAnalytics:
    """
    Demonstrating static methods for YouTube 'Rise and Shine' channel analytics.
    Static methods are perfect for calculations that don't depend on instance state.
    """
    
    @staticmethod
    def engagement_rate(likes, comments, views):
        """Calculates engagement rate as a percentage."""
        if views == 0:
            return 0
        return ((likes + comments) / views) * 100

    @staticmethod
    def average_views(total_views, total_videos):
        """Calculates average views per video."""
        if total_videos == 0:
            return 0
        return total_views / total_videos

# Testing the implementation
if __name__ == "__main__":
    channel_name = "Rise and Shine"
    views = 15000
    likes = 1200
    comments = 300
    
    # Calculate engagement rate using the static method
    rate = YouTubeAnalytics.engagement_rate(likes, comments, views)
    print(f"Channel: {channel_name}")
    print(f"Engagement Rate: {rate:.2f}%")
    
    # Calculate average views
    avg = YouTubeAnalytics.average_views(500000, 25)
    print(f"Average Views per Video: {avg}")
