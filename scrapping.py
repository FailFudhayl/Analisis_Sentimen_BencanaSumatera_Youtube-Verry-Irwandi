import pandas as pd
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_RECENT
import time

def scrap_youtube_comments():
    downloader = YoutubeCommentDownloader()
    # Link video Ferry Irwandi yang kamu pilih
    video_url = 'https://youtu.be/4loaVrhp75Q?si=rpKINJGkxkb2bxq0Q'
    
    print("--- Memulai Scraping Komentar YouTube ---")
    print(f"Target: {video_url}")
    
    try:
        # Mengambil generator komentar
        comments = downloader.get_comments_from_url(video_url, sort_by=SORT_BY_RECENT)
        
        comment_list = []
        limit = 2500  # Kita batasi 500 komentar dulu untuk latihan
        
        for i, comment in enumerate(comments):
            if i >= limit:
                break
            
            # Mengambil data penting: Penulis, Teks, dan Jumlah Like komentar
            comment_list.append({
                'author': comment['author'],
                'text': comment['text'],
                'likes': comment['votes'],
                'time': comment['time']
            })
            
            # Print progres setiap 50 komentar agar kamu tahu program tidak macet
            if (i + 1) % 50 == 0:
                print(f"Berhasil mengambil {i + 1} komentar...")

        # Simpan ke DataFrame
        df = pd.DataFrame(comment_list)
        
        # Simpan ke CSV
        output_file = 'komentar_videoSumatera_ferry_irwandi.csv'
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print("-" * 30)
        print(f"SELESAI! {len(df)} komentar disimpan di: {output_file}")
        print("-" * 30)

    except Exception as e:
        print(f"Terjadi error: {e}")

if __name__ == "__main__":
    scrap_youtube_comments()