social_media = {}

def add_platform(platform_name):
    if platform_name not in social_media:
        social_media[platform_name] = {}
    else:
        print(f"{platform_name} already exists.")

def add_post_type(platform_name, post_type):
    if platform_name in social_media:
        if post_type not in social_media[platform_name]:
            social_media[platform_name][post_type] = []
        else:
            print(f"{post_type} already exists for {platform_name}.")
    else:
        print(f"{platform_name} does not exist. Please add the platform first.")

def add_post(platform_name, post_type, post_content):
    if platform_name in social_media and post_type in social_media[platform_name]:
        social_media[platform_name][post_type].append(post_content)
    else:
        print(f"Unable to add post. Please check if {platform_name} and {post_type} exist.")

def display_all():
    for platform, post_types in social_media.items():
        print(f"\n{platform}:")
        for post_type, posts in post_types.items():
            print(f"  {post_type}:")
            for post in posts:
                print(f"    - {post}")

if __name__ == "__main__":
    # Example usage:
    add_platform("Facebook")
    add_platform("Instagram")
    
    add_post_type("Facebook", "Text")
    add_post_type("Facebook", "Image")
    add_post_type("Instagram", "Image")
    add_post_type("Instagram", "Video")
    
    add_post("Facebook", "Text", "Feeling blessed today! 🌟")
    add_post("Facebook", "Image", "sunset.jpg")
    add_post("Instagram", "Image", "food_pic.jpg")
    add_post("Instagram", "Video", "travel_vlog.mp4")
    
    display_all()

