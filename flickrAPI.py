import flickr_api, time, os.path, keys

api_key = keys.keys['flickr_api_key']
api_secret = keys.keys['flickr_api_secret']
flickr_api.set_keys(api_key, api_secret)

# Runs if auth.txt file is empty and populates it with key info.
if (os.path.getsize("auth.txt") == 0):
    a = flickr_api.auth.AuthHandler()
    perms = "delete"
    url = a.get_authorization_url(perms)
    print(url)
    verifier = input('')
    a.set_verifier(verifier)
    a.save('auth.txt')
    print('Oauth info has been written to file for later reference.')

flickr_api.set_auth_handler('auth.txt')
print('Session: Authorized')

# Function uploads photo to Flickr and returns link
def uploadToFlickr():
    # Uploads Image
    uploaded_image = flickr_api.upload(photo_file = 'assets/post_images/image.jpg', title='Auto-upload.', description=f'Daily Dinner Menu for Carson Dining Hall, University of Oregon.\nTime of Upload: {str(time.ctime())}', is_public = '1', hidden = '2')
    print('Image: Uploaded')
    photo_id = uploaded_image['id']

    # Returns the photo's link
    base_url = 'https://www.flickr.com/photos/197834213@N08/'
    web_url = f'{base_url}{photo_id}'

    download_info = (flickr_api.Photo.getSizes(uploaded_image))  #no worky! docs say needs to be called as flickr?
    download_url = download_info['Original']['source']
    print(f'Image Source URL: {download_url}')
    return download_url