# Internal Guide Site (MkDocs + GitHub Pages)

このリポジトリは **Word (.docx) ファイルをそのまま置いて push するだけ** で  
GitHub Pages に検索付きドキュメントサイトを自動公開するテンプレートです。

## 使い方

1. `docs_src/` フォルダに章ごとの `.docx` ファイルを入れる  
   - 例: `docs_src/第1章：始めにゲームデザイナーありき.docx`
2. `main` ブランチへ push  
3. 数分後、 Actions が `https://<ユーザー名>.github.io/<レポジトリ名>/` にサイトを公開

> **補足:** `docs/` 以下と `site/` 以下は自動生成物ですので、通常は commit しない運用で問題ありません。

## ローカルプレビュー（任意）

```bash
pip install mkdocs-material pypandoc
python convert.py
mkdocs serve
```
