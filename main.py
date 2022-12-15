import yaml
import webbrowser
from typing import List
from typing import Tuple


def parse_config() -> Tuple[str, List[str]] :
    """
        yamlファイルを読み込んで設定を返す
    """
    with open('./settings.yaml', mode="r") as file:
        yaml_data = yaml.safe_load(file.read())

    path = None
    urls = None
    for conf in yaml_data.get("settings"):
        if conf.get("browser_path") is not None:
            path = conf.get("browser_path")
        if conf.get("urls") is not None:
            urls = conf.get("urls")

    if path is None:
        raise SettingError("not find browser_path in settings")
    if urls is None:
        raise SettingError("not find urls in settings")
    return path, urls

def open_urls(browser: webbrowser, urls: List[str]):
    try:
        for i, url in enumerate(urls):
            if i == 0:
                browser.open(url)
            else:
                browser.open(url)
    except Exception as e:
        raise e

def main():

    # 設定ファイル読み込み
    path, urls = parse_config()

    # ブラウザを決定
    # windows環境のみ動作確認済み
    # &を入れないと開いたウェブページを閉じるまで次のページが開かない
    browser = webbrowser.get('"{path}" %s &'.format(path=path))

    # ページを開く
    open_urls(browser, urls)

if __name__ == "__main__":
    main()

class SettingError(Exception):
    pass