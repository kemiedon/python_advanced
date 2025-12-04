"""
範例 3：TinyDB 進階查詢

這個範例展示 TinyDB 的進階查詢功能，
包含複雜條件、巢狀查詢、自訂函數等。

生活情境：
管理電影資料庫，包含電影名稱、導演、類型、評分、上映年份等，
並進行各種複雜的查詢操作。
"""

from tinydb import TinyDB, Query, where
from tinydb.operations import add, subtract, set as db_set


def create_movie_database():
    """建立電影資料庫"""
    print("【建立電影資料庫】")

    db = TinyDB("movies.json", indent=2, ensure_ascii=False)
    db.truncate()

    movies = [
        {
            "title": "肖申克的救贖",
            "director": "法蘭克·戴拉邦",
            "year": 1994,
            "genres": ["劇情", "犯罪"],
            "rating": 9.3,
            "box_office": 28.34,  # 百萬美元
            "awards": ["奧斯卡提名"],
        },
        {
            "title": "教父",
            "director": "法蘭西斯·柯波拉",
            "year": 1972,
            "genres": ["劇情", "犯罪"],
            "rating": 9.2,
            "box_office": 134.97,
            "awards": ["奧斯卡最佳影片", "奧斯卡最佳男主角"],
        },
        {
            "title": "黑暗騎士",
            "director": "克里斯多福·諾蘭",
            "year": 2008,
            "genres": ["動作", "犯罪", "劇情"],
            "rating": 9.0,
            "box_office": 534.86,
            "awards": ["奧斯卡最佳男配角"],
        },
        {
            "title": "星際效應",
            "director": "克里斯多福·諾蘭",
            "year": 2014,
            "genres": ["科幻", "劇情"],
            "rating": 8.6,
            "box_office": 677.47,
            "awards": ["奧斯卡最佳視覺效果"],
        },
        {
            "title": "阿甘正傳",
            "director": "勞勃·辛密克斯",
            "year": 1994,
            "genres": ["劇情", "愛情"],
            "rating": 8.8,
            "box_office": 677.95,
            "awards": ["奧斯卡最佳影片", "奧斯卡最佳男主角"],
        },
        {
            "title": "全面啟動",
            "director": "克里斯多福·諾蘭",
            "year": 2010,
            "genres": ["動作", "科幻", "驚悚"],
            "rating": 8.8,
            "box_office": 829.90,
            "awards": ["奧斯卡最佳攝影"],
        },
        {
            "title": "鐵達尼號",
            "director": "詹姆士·卡麥隆",
            "year": 1997,
            "genres": ["劇情", "愛情"],
            "rating": 7.8,
            "box_office": 2187.46,
            "awards": ["奧斯卡最佳影片", "奧斯卡最佳導演"],
        },
    ]

    db.insert_multiple(movies)
    print(f"✓ 已新增 {len(movies)} 部電影\n")

    return db


def basic_queries(db):
    """基本查詢"""
    print("【基本查詢】")

    Movie = Query()

    # 1. 單一條件查詢
    print("\n1. 評分大於等於 9.0 的電影：")
    results = db.search(Movie.rating >= 9.0)
    for movie in results:
        print(f"  - {movie['title']} ({movie['rating']})")

    # 2. 範圍查詢
    print("\n2. 2000 年至 2010 年的電影：")
    results = db.search((Movie.year >= 2000) & (Movie.year <= 2010))
    for movie in results:
        print(f"  - {movie['title']} ({movie['year']})")

    # 3. 字串比對
    print("\n3. 導演是「克里斯多福·諾蘭」的電影：")
    results = db.search(Movie.director == "克里斯多福·諾蘭")
    for movie in results:
        print(f"  - {movie['title']}")


def advanced_queries(db):
    """進階查詢"""
    print("\n【進階查詢】")

    Movie = Query()

    # 1. 複雜邏輯查詢
    print("\n1. 評分 > 8.5 且票房 > 500M 的電影：")
    results = db.search((Movie.rating > 8.5) & (Movie.box_office > 500))
    for movie in results:
        print(f"  - {movie['title']}")
        print(f"    評分: {movie['rating']}, 票房: ${movie['box_office']}M")

    # 2. OR 查詢
    print("\n2. 1990 年代或 2010 年代的電影：")
    results = db.search(
        ((Movie.year >= 1990) & (Movie.year < 2000))
        | ((Movie.year >= 2010) & (Movie.year < 2020))
    )
    for movie in results:
        print(f"  - {movie['title']} ({movie['year']})")

    # 3. 列表包含查詢
    print("\n3. 類型包含「科幻」的電影：")
    results = db.search(Movie.genres.any(["科幻"]))
    for movie in results:
        print(f"  - {movie['title']} ({', '.join(movie['genres'])})")

    # 4. 多個條件的列表查詢
    print("\n4. 同時包含「動作」和「科幻」的電影：")
    results = db.search(Movie.genres.all(["動作", "科幻"]))
    for movie in results:
        print(f"  - {movie['title']} ({', '.join(movie['genres'])})")


def custom_queries(db):
    """自訂查詢函數"""
    print("\n【自訂查詢函數】")

    Movie = Query()

    # 1. 使用 test 方法自訂查詢邏輯
    print("\n1. 票房是評分 100 倍以上的電影：")
    # TinyDB 的 test 只接受一個參數，所以改用列表推導式
    results = [
        movie for movie in db.all() if movie["box_office"] > movie["rating"] * 100
    ]
    for movie in results:
        print(f"  - {movie['title']}")
        print(f"    評分: {movie['rating']}, 票房: ${movie['box_office']}M")

    # 2. 使用 where 簡化查詢
    print("\n2. 獲得超過 2 個奧斯卡獎項的電影：")
    results = db.search(where("awards").test(lambda x: len(x) >= 2))
    for movie in results:
        print(f"  - {movie['title']}: {len(movie['awards'])} 個獎項")
        for award in movie["awards"]:
            print(f"    • {award}")

    # 3. 正則表達式查詢
    print("\n3. 標題包含「騎士」或「效應」的電影：")
    results = db.search(Movie.title.matches(".*騎士.*|.*效應.*"))
    for movie in results:
        print(f"  - {movie['title']}")


def update_operations(db):
    """更新操作"""
    print("\n【更新操作】")

    Movie = Query()

    # 1. 使用自訂函數更新數值
    print("\n1. 將所有電影的票房增加 10%")

    def increase_box_office(doc):
        doc["box_office"] = doc["box_office"] * 1.1

    db.update(increase_box_office)

    movie = db.get(Movie.title == "鐵達尼號")
    print(f"  鐵達尼號新票房: ${movie['box_office']:.2f}M")

    # 2. 使用 set 設定新值
    print("\n2. 標記 1990 年代的電影為「經典」")
    db.update(db_set("tag", "經典"), (Movie.year >= 1990) & (Movie.year < 2000))

    results = db.search(Movie.tag.exists())
    for movie in results:
        print(f"  - {movie['title']} ({movie['year']}) - {movie.get('tag', '')}")

    # 3. 條件更新
    print("\n3. 為高評分電影（>= 9.0）加上「神作」標籤")

    def add_masterpiece_tag(movie):
        if "tags" not in movie:
            movie["tags"] = []
        if "神作" not in movie["tags"]:
            movie["tags"].append("神作")

    db.update(add_masterpiece_tag, Movie.rating >= 9.0)

    results = db.search(Movie.tags.exists())
    for movie in results:
        print(f"  - {movie['title']}: {', '.join(movie.get('tags', []))}")


def aggregate_queries(db):
    """聚合查詢（統計）"""
    print("\n【統計查詢】")

    Movie = Query()

    # 1. 計數
    total = len(db)
    high_rating = len(db.search(Movie.rating >= 9.0))
    print(f"\n1. 電影統計：")
    print(f"  總電影數: {total} 部")
    print(f"  高評分電影 (>= 9.0): {high_rating} 部")

    # 2. 平均值計算
    all_movies = db.all()
    avg_rating = sum(m["rating"] for m in all_movies) / len(all_movies)
    avg_box_office = sum(m["box_office"] for m in all_movies) / len(all_movies)

    print(f"\n2. 平均統計：")
    print(f"  平均評分: {avg_rating:.2f}")
    print(f"  平均票房: ${avg_box_office:.2f}M")

    # 3. 最大最小值
    max_rating_movie = max(all_movies, key=lambda m: m["rating"])
    max_box_office_movie = max(all_movies, key=lambda m: m["box_office"])

    print(f"\n3. 極值統計：")
    print(f"  最高評分: {max_rating_movie['title']} ({max_rating_movie['rating']})")
    print(
        f"  最高票房: {max_box_office_movie['title']} (${max_box_office_movie['box_office']}M)"
    )

    # 4. 分組統計
    print(f"\n4. 導演作品數統計：")
    directors = {}
    for movie in all_movies:
        director = movie["director"]
        directors[director] = directors.get(director, 0) + 1

    for director, count in sorted(directors.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {director}: {count} 部")


def main():
    """主程式"""
    print("TinyDB 進階查詢範例：電影資料庫")
    print("=" * 80)

    # 建立資料庫
    db = create_movie_database()

    # 基本查詢
    basic_queries(db)

    # 進階查詢
    advanced_queries(db)

    # 自訂查詢
    custom_queries(db)

    # 更新操作
    update_operations(db)

    # 統計查詢
    aggregate_queries(db)

    # 關閉資料庫
    db.close()
    print("\n" + "=" * 80)
    print("✓ 資料庫已關閉")


if __name__ == "__main__":
    main()
