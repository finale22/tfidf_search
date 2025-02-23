from query_vectorizer import search

def print_results():
    s = search()
    while True:
        print("검색어를 입력하세요. 종료하려면 \"검색 종료\"를 입력하세요.")
        query = input()
        if query == "검색 종료":
            print("검색을 종료합니다. . .")
            break
        data, similarities, sorted_indices = s.calculate_similarity(query)
        print(f"검색어: {query}")
        print('\n')
        for idx in sorted_indices:
            if similarities[idx] >= 0.5:
                print(f"아티스트: {data.iloc[idx]['artist']}")
                print(f"곡명: {data.iloc[idx]['song']}")
                print(f"유사도: {similarities[idx]:.4f}")
                print('\n')