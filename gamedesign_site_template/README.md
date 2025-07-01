# ゲームデザインバイブル – GitHub Pages テンプレート

このリポジトリは **「ゲームデザインバイブル」(全35章) をそのまま閲覧できる社内向け解説サイト** です。
GitHub にプッシュするだけで、GitHub Pages が自動的に公開します。

## 使い方

1. **このフォルダ一式を新しい GitHub リポジトリに push**  
2. リポジトリ → **Settings → Pages** で  
   - **Branch**: `gh-pages` を選択  
   - **/ (root)** を Save  
3. 数十秒後、<https://ユーザー名.github.io/リポジトリ名/> でサイトが閲覧できます。

## 仕組み

- [`mkdocs-material`](https://squidfunk.github.io/mkdocs-material/) で静的サイトを生成
- `.github/workflows/gh-pages.yml` で GitHub Actions が `mkdocs build` を実行し、
  `gh-pages` ブランチへデプロイ

---

> **章構成**: 自動生成された Markdown ファイルが `docs/` に入っています。  
> レイアウト調整は `docs/styles/extra.css` を編集してください。
