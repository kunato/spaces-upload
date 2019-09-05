import boto3
import os
import progressbar
from dotenv import load_dotenv
load_dotenv()


def run():
    session = boto3.session.Session()
    client = session.client('s3',
                            region_name='sgp1',
                            endpoint_url='https://sgp1.digitaloceanspaces.com',
                            aws_access_key_id=os.environ['ACCESS_KEY'],
                            aws_secret_access_key=os.environ['SECRET_KEY'])

    file_path = '/home/kunato/Desktop/test.zip'
    basename = os.path.basename(file_path)
    statinfo = os.stat(file_path)

    up_progress = progressbar.progressbar.ProgressBar(maxval=statinfo.st_size)

    up_progress.start()

    def upload_progress(chunk):
        up_progress.update(up_progress.currval + chunk)

    client.upload_file(file_path,os.environ['BUCKET'], basename, Callback=upload_progress)
    up_progress.finish()


if __name__ == "__main__":
    run()