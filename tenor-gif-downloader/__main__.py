from net_utils import InternetUtils


def main():
    folder_path = R"E:\gif"
    with open('search_phrases.csv', 'r') as f:
        search_words = f.read()
        search_items = search_words.split('\n')
    for search_item in search_items:
        net_u = InternetUtils(search_item=search_item)
        final_gifs = net_u.get_all_img_tags()
        print (f'{search_item}: {len(final_gifs)}')
        net_u.files_downloader(folder_path=folder_path, final_gifs=final_gifs)
if __name__ == "__main__":
    main()