import requests
import settings

API_URL = "https://api.chatwork.com/v2/"
API_KEY = settings.getenv("API_KEY")
CHAT_WORK_TOKEN = {'X-ChatWorkToken': API_KEY}


def get_chatwork(path):
    """get_chatwork
    Chatwork APIに問い合わせを行う(GET)
    引数：エントリーポイント以降のパス(最初のスラッシュは不要)
    """
    url = API_URL + path
    # print(url)
    ret = requests.get(url, headers=CHAT_WORK_TOKEN)
    return ret


def get_rooms():
    """get_rooms
    ルーム一覧を取得する
    返却値はAPIドキュメント参照(http://developer.chatwork.com/ja/endpoint_rooms.html)
    """
    ret = get_chatwork('rooms')
    return ret.json()


def get_messages(id):
    """get_room_messages
    ルーム内のメッセージ一覧を取得する
    返却値はAPIドキュメント参照(http://developer.chatwork.com/ja/endpoint_rooms.html#GET-rooms-room_id-messages)
    """
    # force=1だと最新100件のみ取得
    # force=0の場合は前回取得分の差分取得
    ret = get_chatwork('rooms/{id}/messages?force=1'.format(id=str(id)))
    return ret.json()


def main():
    rooms = get_rooms()

    for room in rooms:
        # マイチャットは飛ばす
        if room['type'] == 'my':
            continue

        id = room['room_id']
        messages = get_messages(id)

        print(room['name'])

        for message in messages:
            user = message['account']['name']
            body = message['body']

            # ユーザー追加等のイベントはスキップ
            if body.find('dtext') > 0:
                continue

            print('    [User]: ' + user)
            print('        ' + body)

        print()


if __name__ == '__main__':
    main()
