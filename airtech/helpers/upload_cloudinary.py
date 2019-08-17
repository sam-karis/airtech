import cloudinary.uploader

default_profile_url = "http://res.cloudinary.com/samkaris/image/upload/v1566004020/airtech-v1/kg71cooxj9cluxxodcap.png"  # noqa E501


def upload_file(file, folder='airtech-v1'):
    try:
        return cloudinary.uploader.upload(file, folder=folder).get('url')
    except Exception:
        pass


def delete_file(image_url, folder='airtech-v1'):
    is_deleted = False
    if not image_url == default_profile_url:
        public_id, extension = image_url.split('/')[-1].split('.')
        try:
            cloudinary.uploader.destroy(f'{folder}/{public_id}')
            is_deleted = True
        except Exception:
            pass
    return is_deleted
