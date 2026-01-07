# みかんプロジェクト セットアップガイド

## 完了した作業

✅ Laravel 12プロジェクトの作成
✅ Docker環境の構築（docker-compose.yml、Dockerfile、Nginx設定）
✅ 環境設定ファイル（.env）の準備
✅ データベースマイグレーションの作成（works, staff, contacts）
✅ モデルの作成（Work, Staff, Contact）
✅ シーダーの作成（WorksSeeder, StaffSeeder）
✅ コントローラーの作成（HomeController, WorksController, StaffController, CompanyController, ContactController）
✅ ルーティングの設定

## Docker環境の起動方法

### 1. Dockerコンテナのビルドと起動

```bash
cd mikan-project
docker-compose up -d --build
```

### 2. データベースマイグレーションの実行

```bash
docker-compose exec app php artisan migrate
```

### 3. シーダーの実行（初期データの投入）

```bash
docker-compose exec app php artisan db:seed
```

### 4. アプリケーションへのアクセス

ブラウザで以下のURLにアクセス：
- http://localhost:8080

## 次のステップ

### 1. ビューの作成

以下のBladeテンプレートを作成する必要があります：

- `resources/views/layouts/app.blade.php` - メインレイアウト
- `resources/views/layouts/header.blade.php` - ヘッダー
- `resources/views/layouts/footer.blade.php` - フッター
- `resources/views/components/navigation.blade.php` - ナビゲーション
- `resources/views/pages/home.blade.php` - トップページ
- `resources/views/pages/works.blade.php` - 作品一覧ページ
- `resources/views/pages/staff.blade.php` - スタッフページ
- `resources/views/pages/company.blade.php` - 会社情報ページ
- `resources/views/components/contact-form.blade.php` - お問い合わせフォーム

### 2. CSS/スタイリング

- Tailwind CSSの設定、またはカスタムCSSの実装
- BEM命名規則に従ったクラス名の使用
- レスポンシブデザインの実装

### 3. アクセシビリティ対応

- WAI-ARIA属性の追加
- セマンティックHTMLの使用
- キーボードナビゲーション対応

### 4. 画像の準備

- 作品画像の配置
- スタッフ写真の配置
- 画像の最適化（WebP形式への変換）

## データベース接続情報

- **ホスト**: mysql（Docker内）または localhost:3306（ホストから）
- **データベース名**: mikan_project
- **ユーザー名**: mikan_user
- **パスワード**: mikan_password
- **ルートパスワード**: root

## よく使うコマンド

### Dockerコンテナの操作

```bash
# コンテナの起動
docker-compose up -d

# コンテナの停止
docker-compose down

# コンテナの再起動
docker-compose restart

# ログの確認
docker-compose logs -f app

# コンテナ内でコマンドを実行
docker-compose exec app php artisan [command]
```

### Laravelコマンド

```bash
# マイグレーションの実行
docker-compose exec app php artisan migrate

# シーダーの実行
docker-compose exec app php artisan db:seed

# キャッシュのクリア
docker-compose exec app php artisan cache:clear
docker-compose exec app php artisan config:clear
docker-compose exec app php artisan view:clear

# ルートの確認
docker-compose exec app php artisan route:list
```

## トラブルシューティング

### ポートが既に使用されている場合

`docker-compose.yml`のポート番号を変更してください：
```yaml
ports:
  - "8081:80"  # 8080から8081に変更
```

### データベース接続エラー

`.env`ファイルのデータベース設定を確認してください：
```
DB_CONNECTION=mysql
DB_HOST=mysql
DB_PORT=3306
DB_DATABASE=mikan_project
DB_USERNAME=mikan_user
DB_PASSWORD=mikan_password
```

### コンテナが起動しない場合

```bash
# コンテナのログを確認
docker-compose logs

# コンテナを再ビルド
docker-compose up -d --build --force-recreate
```

## 開発環境の確認

- PHP: 8.2
- Laravel: 12.44.0
- MySQL: 8.0
- Redis: Alpine版
- Nginx: Alpine版

