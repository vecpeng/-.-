import json

# 此处手动更换文件名称 换成小组内各个组员的json文件 依次运行一遍
with open("chenpeng.json", 'r', encoding='UTF-8') as f:
    load_dict = json.load(f)

def write_data(news_name, news_content):
    with open(news_name, 'a', encoding="utf-8") as file_handle:
        file_handle.write(news_content)


for i in range(0, len(load_dict)):
    news_subject = load_dict[i]['news_position']

    if (news_subject == "neutral"):
        try:
            news_content = load_dict[i]['news_content_translate_en']
            news_name = "./neutral/" + load_dict[i]['id'] + ".txt"
            write_data(news_name, news_content)
        except Exception:
            continue
    elif (news_subject == "positive"):
        try:
            news_content = load_dict[i]['news_content_translate_en']
            news_name = "./positive/" + load_dict[i]['id'] + ".txt"
            write_data(news_name, news_content)
        except Exception:
            continue
    else:
        try:
            news_content = load_dict[i]['news_content_translate_en']
            news_name = "./negative/" + load_dict[i]['id'] + ".txt"
            write_data(news_name,news_content)
        except Exception:
            continue

