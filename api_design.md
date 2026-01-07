# みかんプロジェクト ウェブサイト API設計書

## 1. API概要

### 1.1 API方針
本プロジェクトは主にサーバーサイドレンダリング（SSR）のWebサイトとして実装するため、APIは必要最小限の機能に限定する。

### 1.2 API仕様
- **形式**: RESTful API
- **データ形式**: JSON
- **認証**: 現時点では不要（将来的に管理画面用の認証を実装）

## 2. エンドポイント一覧

### 2.1 お問い合わせAPI

#### 2.1.1 お問い合わせ送信

**エンドポイント**
```
POST /contact
```

**説明**
お問い合わせフォームから送信された情報を受け取り、データベースに保存する。
現在はWebルートとして実装されており、フォーム送信後にリダイレクトされる。

**リクエスト**

**Headers**
```
Content-Type: application/x-www-form-urlencoded
Accept: text/html
X-CSRF-TOKEN: {csrf_token}
```

**Body（フォームデータ）**
```
name=山田太郎&email=yamada@example.com&message=お問い合わせ内容です。
```

**バリデーションルール**
- `name`: 必須、文字列、最大100文字
- `email`: 必須、メール形式、最大255文字
- `message`: 必須、文字列、最大5000文字

**レスポンス**

**成功時（302 Redirect）**
バリデーション成功後、`/company`にリダイレクトされ、セッションに成功メッセージが保存される。
```
Location: /company
Session: success = "お問い合わせを受け付けました。ありがとうございます。"
```

**バリデーションエラー時（422 Unprocessable Entity）**
バリデーション失敗時、前のページにリダイレクトされ、エラーメッセージがセッションに保存される。
Bladeテンプレートでは`@error`ディレクティブを使用して各フィールドの下にエラーメッセージを表示する。

**エラーメッセージの表示形式**:
- `@error('name')` - お名前フィールドのエラー
- `@error('email')` - メールアドレスフィールドのエラー
- `@error('message')` - お問い合わせ内容フィールドのエラー

**セッションに保存されるエラー形式**:
```php
$errors = [
  "name" => ["お名前は必須です。"],
  "email" => ["メールアドレスの形式が正しくありません。"]
]
```

**Bladeテンプレートでの表示例**:
```blade
@error('name')
    <span id="name-error" class="contact-form__error" role="alert">{{ $message }}</span>
@enderror
```

**エラー時（500 Internal Server Error）**
サーバーエラーが発生した場合、`try-catch`ブロックでエラーをキャッチし、前のページにリダイレクトしてエラーメッセージを表示する。
エラーの詳細はログファイルに記録される（メッセージ内容はセキュリティのためログに含めない）。

**エラーメッセージの表示**:
```blade
@if($errors->has('general'))
    <div class="contact__message contact__message--error" role="alert">
        {{ $errors->first('general') }}
    </div>
@endif
```

**ログ記録**:
エラー発生時、`storage/logs/laravel.log`に以下の形式で記録される。
```
[2024-01-01 12:00:00] local.ERROR: お問い合わせ送信エラー: [エラー内容] 
{"request":{"name":"山田太郎","email":"yamada@example.com"}}
```

### 2.2 作品情報API（将来拡張用）

**注意**: 現在はWebルートとして実装されており、`GET /works`でアクセス可能。
将来的にAPIエンドポイントとして`GET /api/works`を実装する予定。

#### 2.2.1 作品一覧取得

**エンドポイント（将来実装予定）**
```
GET /api/works
```

**説明**
作品一覧を取得する。フィルタリング、ソート、ページネーションに対応。

**クエリパラメータ**
- `category`: カテゴリでフィルタリング（etv_special, 4k_special, nichiyo_bijutsu, other）
- `year`: 年でフィルタリング（例: 2023）
- `page`: ページ番号（デフォルト: 1）
- `per_page`: 1ページあたりの件数（デフォルト: 10、最大: 100）

**レスポンス**

**成功時（200 OK）**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "title": "断らない ある市役所の実践",
      "broadcast_date": "2023-09-01",
      "category": "etv_special",
      "category_label": "ETV特集",
      "description": "神奈川県座間市生活援護課は、「誰も断らない、見捨てない」をモットーに生活困窮者支援に取り組んでいる。",
      "link_url": "https://example.com/link",
      "image_path": "/images/works/work1.jpg",
      "display_order": 1,
      "created_at": "2024-01-01T12:00:00.000000Z",
      "updated_at": "2024-01-01T12:00:00.000000Z"
    }
  ],
  "meta": {
    "current_page": 1,
    "per_page": 10,
    "total": 50,
    "last_page": 5
  }
}
```

#### 2.2.2 作品詳細取得

**エンドポイント**
```
GET /api/works/{id}
```

**説明**
指定されたIDの作品詳細を取得する。

**パスパラメータ**
- `id`: 作品ID（必須）

**レスポンス**

**成功時（200 OK）**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "title": "断らない ある市役所の実践",
    "broadcast_date": "2023-09-01",
    "category": "etv_special",
    "category_label": "ETV特集",
    "description": "詳細な説明...",
    "link_url": "https://example.com/link",
    "image_path": "/images/works/work1.jpg",
    "display_order": 1,
    "created_at": "2024-01-01T12:00:00.000000Z",
    "updated_at": "2024-01-01T12:00:00.000000Z"
  }
}
```

**存在しない場合（404 Not Found）**
```json
{
  "success": false,
  "message": "作品が見つかりませんでした。"
}
```

### 2.3 スタッフ情報API（将来拡張用）

**注意**: 現在はWebルートとして実装されており、`GET /staff`でアクセス可能。
将来的にAPIエンドポイントとして`GET /api/staff`を実装する予定。

#### 2.3.1 スタッフ情報取得

**エンドポイント（将来実装予定）**
```
GET /api/staff
```

**説明**
スタッフ情報を取得する。

**レスポンス**

**成功時（200 OK）**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "name": "伊槻雅裕",
    "position": "ディレクター・プロデューサー",
    "profile": "プロフィール内容...",
    "biography": "経歴・略歴...",
    "achievements": "実績・受賞歴...",
    "image_path": "/images/staff/staff1.jpg",
    "created_at": "2024-01-01T12:00:00.000000Z",
    "updated_at": "2024-01-01T12:00:00.000000Z"
  }
}
```

## 3. エラーハンドリング

### 3.1 エラーレスポンス形式

**Webルート（現在の実装）**:
現在はWebルートとして実装されているため、エラーはセッションに保存され、Bladeテンプレートで表示される。

**エラーメッセージの形式**:
```php
// Laravelのバリデーションエラー形式
$errors = [
  "field_name" => ["エラーメッセージ1", "エラーメッセージ2"]
]
```

**Bladeテンプレートでの表示**:
```blade
@error('field_name')
    <span class="error-message" role="alert">{{ $message }}</span>
@enderror
```

**APIエンドポイント（将来実装予定）**:
将来的にAPIエンドポイントを実装する場合、以下のJSON形式でエラーレスポンスを返す。

```json
{
  "success": false,
  "message": "エラーメッセージ",
  "errors": {
    "field_name": ["エラーメッセージ1", "エラーメッセージ2"]
  }
}
```

### 3.2 HTTPステータスコード

| ステータスコード | 説明 | 使用例 |
|----------------|------|--------|
| 200 | OK | 正常なレスポンス |
| 201 | Created | リソースの作成成功 |
| 400 | Bad Request | リクエストが不正 |
| 401 | Unauthorized | 認証が必要 |
| 403 | Forbidden | アクセス権限なし |
| 404 | Not Found | リソースが見つからない |
| 422 | Unprocessable Entity | バリデーションエラー |
| 500 | Internal Server Error | サーバーエラー |

## 4. レート制限（将来拡張）

### 4.1 制限内容
- お問い合わせ送信: 1時間あたり5回まで
- その他のAPI: 1分あたり60回まで

### 4.2 レート制限超過時
```json
{
  "success": false,
  "message": "リクエストが多すぎます。しばらく時間をおいて再度お試しください。",
  "retry_after": 3600
}
```

## 5. CORS設定

### 5.1 設定内容
- 現時点では同一オリジンのみ許可
- 将来的に必要に応じてCORS設定を追加

## 6. APIバージョニング（将来拡張）

### 6.1 バージョン管理
- URLパスにバージョンを含める（例: `/api/v1/contact`）
- デフォルトは`v1`

## 7. セキュリティ

### 7.1 CSRF対策
- Laravel標準のCSRFトークンを使用
- フォーム送信時はCSRFトークンを必須とする
- `@csrf`ディレクティブを使用してBladeテンプレートに自動挿入

### 7.2 入力検証
- サーバーサイドでの厳格なバリデーション（Laravel Validator使用）
- XSS対策（Bladeテンプレートの自動エスケープ）
- SQLインジェクション対策（Eloquent ORM使用）

### 7.3 スパム対策
- IPアドレスの記録（`ip_address`カラムに保存）
- レート制限の実装（将来拡張）
- reCAPTCHAの導入（将来拡張）

**現在の実装状況**:
- IPアドレスの記録: ✅ 実装済み（`ContactController`で`$request->ip()`を使用）
- レート制限: ⏳ 未実装（将来拡張）
- reCAPTCHA: ⏳ 未実装（将来拡張）

## 8. ログ・モニタリング

### 8.1 ログ記録

**現在の実装状況**:
- ✅ エラーログの記録: `ContactController`で`\Log::error()`を使用してエラーを記録
- ⏳ APIリクエストのログ記録: 未実装（将来拡張）
- ⏳ お問い合わせ送信のログ記録: 未実装（将来拡張）

**ログファイルの場所**:
- `storage/logs/laravel.log`

**ログ記録の例**:
```php
\Log::error('お問い合わせ送信エラー: ' . $e->getMessage(), [
    'request' => $request->except(['message']), // メッセージ内容はログに含めない
]);
```

**セキュリティ考慮事項**:
- お問い合わせ内容（`message`フィールド）はログに含めない
- 個人情報（メールアドレスなど）は必要最小限のみ記録

### 8.2 モニタリング
- ⏳ レスポンスタイムの監視: 未実装（将来拡張）
- ⏳ エラー率の監視: 未実装（将来拡張）
- ⏳ API使用状況の監視: 未実装（将来拡張）

## 9. テスト

### 9.1 テスト項目
- 正常系のテスト
- バリデーションエラーのテスト
- エラーハンドリングのテスト
- レート制限のテスト（将来拡張）

### 9.2 テストツール
- PHPUnit（Laravel標準）
- Postman（手動テスト用）


