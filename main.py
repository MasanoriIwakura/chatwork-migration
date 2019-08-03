import requests
import settings

API_URL = "https://api.chatwork.com/v2/"
API_KEY = settings.getenv("API_KEY")
CHAT_WORK_TOKEN = {'X-ChatWorkToken': API_KEY}


def get_rooms():
    """get_rooms
    ルーム一覧を取得する
    返却値はAPIドキュメント参照(http://developer.chatwork.com/ja/endpoint_rooms.html)
    """

    ret = requests.get(API_URL + 'rooms', headers=CHAT_WORK_TOKEN)
    return ret.json()


def main():
    get_rooms()


if __name__ == '__main__':
    main()
