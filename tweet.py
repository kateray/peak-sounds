from twython import Twython
import yaml, json, datetime

def get_twitter_instance():
    with open('config.yaml') as f:
        config = yaml.load(f)

    twitter_app_key = config['twitter_app_key']
    twitter_app_secret = config['twitter_app_secret']
    twitter_oauth_token = config['twitter_oauth_token']
    twitter_oauth_token_secret = config['twitter_oauth_token_secret']

    return Twython(twitter_app_key, twitter_app_secret, twitter_oauth_token, twitter_oauth_token_secret)

def get_next_image():
    with open('image-list.json','r') as f:
        images = json.load(f)
    return next(x for x in images if x['tweeted'] == 'false')

def update_image_list(file_name):
    with open('image-list.json', 'r+') as f:
        images = json.load(f)
        image = next(x for x in images if x['name'] == file_name)
        image['tweeted'] = str(datetime.datetime.now())
        f.seek(0)
        json.dump(images, f, indent=4)
        f.truncate()

def main():
    twitter = get_twitter_instance()

    image_file = get_next_image()['name']
    image = open('images/' + image_file, 'rb')

    response = twitter.upload_media(media=image)

    twitter.update_status(status="bud", media_ids=[response['media_id']])

    update_image_list(image_file)

if __name__ == '__main__':
    main()
