import requests
import shutil

FILENAME = "urls.txt"
FILE_PATH = "images/"


def save_url_image(url_image, path):
    filename = url_image.split("/")[-1]
    resp = requests.get(url_image, stream=True)
    print(resp.status_code)
    if resp.status_code == 200:
        resp.raw.decode_content = True
        with open('{}{}'.format(path, filename), 'wb') as f:
            shutil.copyfileobj(resp.raw, f)
        print('Image sucessfully Downloaded: ', filename)
    else:
        print('Error')
    del resp
    return None


def main():
    with open(FILENAME) as urls:
        for url in urls:
            save_url_image(url.rstrip(), FILE_PATH)


if __name__ == "__main__":
    main()
