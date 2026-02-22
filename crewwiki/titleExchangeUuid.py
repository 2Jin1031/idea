import pymysql
import pandas as pd
import re
import urllib.parse as ul
import sys
import configparser
import os

# title → uuid 매핑
mapping = dict(pd.read_csv("sorted-title-uuid.csv").values)

def find_uuid(name: str):
    name = name.strip()
    if name in mapping:
        return mapping[name], name
    base, _, rest = name.partition('(')
    base = base.strip()
    suffix = '(' + rest if rest else ''
    cands = [(k, v) for k, v in mapping.items() if k.startswith(base)]
    if not cands:
        return None, None
    if suffix:
        for k, v in cands:
            if k.endswith(suffix):
                return v, k
    return cands[0][1], cands[0][0]

# 이미지 URL 패턴
pat = r"(https://wooteco-crew-wiki\.s3\.ap-northeast-2\.amazonaws\.com)/([^/]+)/([^\s)]+)"

def replace_links(content, doc_title):
    def repl(m):
        base_url = m.group(1)
        folder = ul.unquote(m.group(2))  # 디코딩 필요
        filename = m.group(3)

        uuid, src_title = find_uuid(folder)
        if not uuid and doc_title:
            uuid, src_title = find_uuid(doc_title)
        if not uuid:
            return m.group(0)

        new_url = f"{base_url}/{uuid}/{filename}"
        print(f"replace: {m.group(0)}  ->  {new_url}   (uuid from '{src_title}')\n")
        return new_url

    return re.sub(pat, repl, content)


# 설정 파일 읽기
config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
if not os.path.exists(config_path):
    print(f"[ERROR] 설정 파일을 찾을 수 없습니다: {config_path}")
    print("config.ini.example 파일을 참고하여 config.ini 파일을 생성해주세요.")
    sys.exit(1)

config.read(config_path)

# DB 연결
try:
    conn = pymysql.connect(
        host=config['database']['host'],
        port=int(config['database']['port']),
        user=config['database']['user'],
        password=config['database']['password'],
        db=config['database']['database'],
        charset=config['database']['charset']
    )
except pymysql.MySQLError as e:
    print(f"[ERROR] DB 연결 실패: {e}")
    sys.exit(1)

cur = conn.cursor()

cur.execute("SELECT id, title, contents FROM document")
rows = cur.fetchall()


for doc_id, title, content in rows:
    new_content = replace_links(content, title)
    if new_content != content:
        cur.execute("UPDATE document SET contents=%s WHERE id=%s", (new_content, doc_id))
        print(f"Updated document id={doc_id}, title='{title}'")

conn.commit()
cur.close()
conn.close()