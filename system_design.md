# みかんプロジェクト ウェブサイト システム設計書

## 1. システムアーキテクチャ

### 1.1 全体構成

```
┌─────────────────────────────────────────┐
│         Client (Browser)                │
│  (Chrome, Firefox, Safari, Edge)       │
└──────────────┬──────────────────────────┘
               │ HTTPS
               │
┌──────────────▼──────────────────────────┐
│      Nginx (Reverse Proxy)              │
│      - SSL/TLS Termination              │
│      - Static File Serving              │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Laravel 12 Application             │
│      - MVC Architecture                 │
│      - Blade Templates                  │
│      - API Endpoints                    │
└──────────────┬──────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
┌──────▼──────┐  ┌────▼──────┐
│   MySQL 8.0 │  │   Redis   │
│  (Database) │  │  (Cache)  │
└─────────────┘  └───────────┘
```

### 1.2 Docker構成

```
docker-compose.yml
├── nginx (Web Server)
├── app (Laravel Application)
├── mysql (Database)
└── redis (Cache/Session)
```

## 2. ディレクトリ構造

```
mikan-project/
├── docker/
│   ├── nginx/
│   │   └── default.conf
│   └── php/
│       └── Dockerfile
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   ├── HomeController.php
│   │   │   ├── WorksController.php
│   │   │   ├── StaffController.php
│   │   │   ├── CompanyController.php
│   │   │   └── ContactController.php
│   │   ├── Requests/
│   │   │   └── ContactRequest.php
│   │   └── Middleware/
│   ├── Models/
│   │   ├── Work.php
│   │   ├── Staff.php
│   │   └── Contact.php
│   └── Services/
│       └── ContactService.php
├── database/
│   ├── migrations/
│   │   ├── 2024_01_01_000001_create_works_table.php
│   │   ├── 2024_01_01_000002_create_staff_table.php
│   │   └── 2024_01_01_000003_create_contacts_table.php
│   └── seeders/
│       ├── WorksSeeder.php
│       └── StaffSeeder.php
├── resources/
│   ├── views/
│   │   ├── layouts/
│   │   │   ├── app.blade.php
│   │   │   ├── header.blade.php
│   │   │   └── footer.blade.php
│   │   ├── pages/
│   │   │   ├── home.blade.php
│   │   │   ├── works.blade.php
│   │   │   ├── staff.blade.php
│   │   │   └── company.blade.php
│   │   └── components/
│   │       ├── navigation.blade.php
│   │       └── contact-form.blade.php
│   ├── css/
│   │   └── app.css
│   └── js/
│       └── app.js
├── routes/
│   ├── web.php
│   └── api.php
├── public/
│   ├── index.php
│   ├── css/
│   ├── js/
│   └── images/
├── tests/
│   ├── Feature/
│   │   ├── HomePageTest.php
│   │   ├── WorksPageTest.php
│   │   ├── StaffPageTest.php
│   │   └── ContactFormTest.php
│   └── Unit/
├── docker-compose.yml
├── Dockerfile
├── .env.example
├── composer.json
└── package.json
```

## 3. 技術スタック詳細

### 3.1 バックエンド

#### Laravel 12
- **フレームワーク**: Laravel 12
- **PHPバージョン**: PHP 8.2以上
- **主要機能**:
  - MVCアーキテクチャ
  - Eloquent ORM
  - Bladeテンプレートエンジン
  - ルーティング
  - ミドルウェア
  - バリデーション
  - メール送信

#### パッケージ（Composer）
- `laravel/framework`: Laravelコア
- `laravel/sanctum`: API認証（将来拡張用）
- `intervention/image`: 画像処理
- `guzzlehttp/guzzle`: HTTPクライアント

### 3.2 フロントエンド

#### Bladeテンプレート
- Laravel標準のBladeテンプレートエンジン
- コンポーネント化による再利用性の向上

#### CSS
- Tailwind CSS または カスタムCSS
- BEM命名規則に準拠
- レスポンシブデザイン

#### JavaScript
- バニラJavaScript（必要最小限）
- 将来的にVue.jsまたはReact導入の可能性

### 3.3 データベース

#### MySQL 8.0
- リレーショナルデータベース
- 文字コード: utf8mb4
- 照合順序: utf8mb4_unicode_ci

### 3.4 キャッシュ・セッション

#### Redis
- セッションストレージ
- キャッシュストレージ
- キュー管理（将来拡張用）

### 3.5 Webサーバー

#### Nginx
- リバースプロキシ
- 静的ファイル配信
- SSL/TLS終端

## 4. データフロー

### 4.1 ページ表示フロー

```
User Request
    ↓
Nginx (Reverse Proxy)
    ↓
Laravel Application
    ↓
Route → Controller
    ↓
Model → Database
    ↓
View (Blade Template)
    ↓
Response (HTML)
    ↓
User Browser
```

### 4.2 お問い合わせ送信フロー

```
User Input (Contact Form)
    ↓
Client-side Validation
    ↓
POST /contact
    ↓
ContactRequest (Validation)
    ↓
ContactController
    ↓
ContactService
    ↓
Database (Save)
    ↓
Email Notification (Queue)
    ↓
Response (Success Message)
```

## 5. セキュリティ設計

### 5.1 認証・認可
- 現時点では公開サイト（認証不要）
- 将来的に管理画面用の認証を実装

### 5.2 セキュリティ対策
- **CSRF対策**: Laravel標準のCSRFトークン
- **XSS対策**: Bladeの自動エスケープ
- **SQLインジェクション対策**: Eloquent ORMの使用
- **入力検証**: Form Requestによるバリデーション
- **ファイルアップロード**: ファイルタイプ・サイズ制限

### 5.3 HTTPS
- SSL/TLS証明書の設定
- HTTPからHTTPSへのリダイレクト

## 6. パフォーマンス最適化

### 6.1 フロントエンド最適化
- 画像の最適化（WebP形式）
- 画像の遅延読み込み（lazy loading）
- CSS/JavaScriptのミニファイ
- ブラウザキャッシュの活用

### 6.2 バックエンド最適化
- データベースクエリの最適化（Eager Loading）
- Redisキャッシュの活用
- レスポンスキャッシュ
- ページネーションの実装

### 6.3 CDN（将来拡張）
- 静的ファイルのCDN配信
- 画像のCDN配信

## 7. エラーハンドリング

### 7.1 エラーページ
- 404 Not Found
- 500 Internal Server Error
- 403 Forbidden

### 7.2 ログ管理
- Laravel標準のログ機能
- エラーログの記録
- アクセスログの記録

## 8. テスト戦略

### 8.1 ユニットテスト
- Modelのテスト
- Serviceのテスト
- バリデーションのテスト

### 8.2 機能テスト
- ページ表示のテスト
- フォーム送信のテスト
- ルーティングのテスト

### 8.3 E2Eテスト（将来拡張）
- ブラウザ自動テスト（Playwright等）

## 9. デプロイメント

### 9.1 開発環境
- Docker Composeによるローカル環境
- ホットリロード対応

### 9.2 本番環境
- 詳細は後日決定
- CI/CDパイプラインの構築（将来拡張）

## 10. モニタリング・運用

### 10.1 ログ監視
- アプリケーションログ
- エラーログ
- アクセスログ

### 10.2 パフォーマンス監視
- レスポンスタイムの監視
- データベースクエリの監視

### 10.3 バックアップ
- データベースの定期バックアップ
- ファイルのバックアップ


