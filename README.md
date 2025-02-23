# TF-IDF를 활용한 팝송 검색
- 검색 기능 구현 시 간단하게 활용할 수 있는 TF-IDF를 활용하여 팝송 검색 기능 구현
- TF-IDF는 모든 문서에 자주 등장하는 단어는 중요도가 낮다고 판단하고, 특정 문서에서만 자주 등장하는 단어는 중요도가 높다고 판단
- 장점: 가볍고 빠르게 검색 기능을 적용할 수 있다.
- 단점: 빈도 수를 기준으로 계산하므로 단어의 의미를 반영하지 못한다.

# 데이터셋
Spotify Million Song Dataset

[Kaggle](https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset)

[Hugging Face](https://huggingface.co/datasets/vishnupriyavr/spotify-million-song-dataset)

# 소스파일 다운로드
```
# git bash
git clone https://github.com/finale22/tfidf_search.git
cd tfidf_search
```
패키지 설치
```
python -m venv myenv
source myenv/Scripts/activate
pip install -r requirements.txt
```

# 사용법
```
python main.py --mode search
```
실행 후 검색하고 싶은 팝송 검색

"검색 종료" 입력 시 검색 종료
