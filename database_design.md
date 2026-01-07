# みかんプロジェクト ウェブサイト データベース設計書

## 1. データベース概要

### 1.1 データベース名
`mikan_project`

### 1.2 文字コード
- 文字セット: `utf8mb4`
- 照合順序: `utf8mb4_unicode_ci`

### 1.3 エンジン
InnoDB

## 2. ER図

```
┌─────────────┐
│    works    │
├─────────────┤
│ id (PK)     │
│ title       │
│ broadcast_date│
│ category    │
│ description │
│ link_url    │
│ image_path  │
│ display_order│
│ is_published│
│ created_at  │
│ updated_at  │
└─────────────┘

┌─────────────┐
│    staff    │
├─────────────┤
│ id (PK)     │
│ name        │
│ position    │
│ profile     │
│ biography   │
│ achievements│
│ image_path  │
│ created_at  │
│ updated_at  │
└─────────────┘

┌─────────────┐
│  contacts   │
├─────────────┤
│ id (PK)     │
│ name        │
│ email       │
│ message     │
│ status      │
│ ip_address  │
│ created_at  │
│ updated_at  │
└─────────────┘
```

## 3. テーブル定義

### 3.1 works（作品情報）

#### テーブル名
`works`

#### 説明
NHK番組などの制作実績を管理するテーブル

#### カラム定義

| カラム名 | データ型 | 制約 | デフォルト値 | 説明 |
|---------|---------|------|------------|------|
| id | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | - | 作品ID |
| title | VARCHAR(255) | NOT NULL | - | 作品タイトル |
| broadcast_date | DATE | NULL | NULL | 放送日 |
| category | VARCHAR(50) | NOT NULL | - | カテゴリ（etv_special, 4k_special, nichiyo_bijutsu, other） |
| description | TEXT | NULL | NULL | 作品の概要・説明 |
| link_url | VARCHAR(500) | NULL | NULL | 関連リンクURL |
| image_path | VARCHAR(500) | NULL | NULL | 画像ファイルパス |
| display_order | INT | NOT NULL | 0 | 表示順序 |
| is_published | BOOLEAN | NOT NULL | true | 公開フラグ |
| created_at | TIMESTAMP | NULL | NULL | 作成日時 |
| updated_at | TIMESTAMP | NULL | NULL | 更新日時 |

#### インデックス
- PRIMARY KEY (`id`)
- INDEX `idx_category` (`category`)
- INDEX `idx_broadcast_date` (`broadcast_date`)
- INDEX `idx_is_published` (`is_published`)

#### カテゴリの値
- `etv_special`: ETV特集
- `4k_special`: 4K特集
- `nichiyo_bijutsu`: 日曜美術館
- `other`: その他

### 3.2 staff（スタッフ情報）

#### テーブル名
`staff`

#### 説明
スタッフのプロフィール、経歴、実績を管理するテーブル

#### カラム定義

| カラム名 | データ型 | 制約 | デフォルト値 | 説明 |
|---------|---------|------|------------|------|
| id | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | - | スタッフID |
| name | VARCHAR(100) | NOT NULL | - | 氏名 |
| position | VARCHAR(100) | NOT NULL | - | 役職 |
| profile | TEXT | NULL | NULL | プロフィール |
| biography | TEXT | NULL | NULL | 経歴・略歴 |
| achievements | TEXT | NULL | NULL | 実績・受賞歴 |
| image_path | VARCHAR(500) | NULL | NULL | 写真ファイルパス |
| created_at | TIMESTAMP | NULL | NULL | 作成日時 |
| updated_at | TIMESTAMP | NULL | NULL | 更新日時 |

#### インデックス
- PRIMARY KEY (`id`)

### 3.3 contacts（お問い合わせ）

#### テーブル名
`contacts`

#### 説明
お問い合わせフォームから送信された情報を管理するテーブル

#### カラム定義

| カラム名 | データ型 | 制約 | デフォルト値 | 説明 |
|---------|---------|------|------------|------|
| id | BIGINT UNSIGNED | PRIMARY KEY, AUTO_INCREMENT | - | お問い合わせID |
| name | VARCHAR(100) | NOT NULL | - | お名前 |
| email | VARCHAR(255) | NOT NULL | - | メールアドレス |
| message | TEXT | NOT NULL | - | お問い合わせ内容 |
| status | VARCHAR(20) | NOT NULL | 'unread' | ステータス（unread, read, replied） |
| ip_address | VARCHAR(45) | NULL | NULL | IPアドレス（スパム対策用） |
| created_at | TIMESTAMP | NULL | NULL | 作成日時 |
| updated_at | TIMESTAMP | NULL | NULL | 更新日時 |

#### インデックス
- PRIMARY KEY (`id`)
- INDEX `idx_status` (`status`)
- INDEX `idx_created_at` (`created_at`)

#### ステータスの値
- `unread`: 未読
- `read`: 既読
- `replied`: 返信済み

## 4. マイグレーション

### 4.1 worksテーブルのマイグレーション

```php
Schema::create('works', function (Blueprint $table) {
    $table->id();
    $table->string('title');
    $table->date('broadcast_date')->nullable();
    $table->string('category');
    $table->text('description')->nullable();
    $table->string('link_url', 500)->nullable();
    $table->string('image_path', 500)->nullable();
    $table->integer('display_order')->default(0);
    $table->boolean('is_published')->default(true);
    $table->timestamps();
    
    $table->index('category');
    $table->index('broadcast_date');
    $table->index('is_published');
});
```

### 4.2 staffテーブルのマイグレーション

```php
Schema::create('staff', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('position');
    $table->text('profile')->nullable();
    $table->text('biography')->nullable();
    $table->text('achievements')->nullable();
    $table->string('image_path', 500)->nullable();
    $table->timestamps();
});
```

### 4.3 contactsテーブルのマイグレーション

```php
Schema::create('contacts', function (Blueprint $table) {
    $table->id();
    $table->string('name');
    $table->string('email');
    $table->text('message');
    $table->string('status')->default('unread');
    $table->string('ip_address', 45)->nullable();
    $table->timestamps();
    
    $table->index('status');
    $table->index('created_at');
});
```

## 5. シーダー

### 5.1 WorksSeeder

初期データとして、PDFから抽出した作品情報を登録する。

主な作品:
- ETV特集: 「断らない ある市役所の実践」（2023.9）
- ETV特集: 「迷える女性たちの家」（2022.6）
- ETV特集: 「この国で生きてゆく ～大阪 外国ルーツの子どもたち」（2021.5）
- 4K特集: 「すべてのものが幸福にしかなれない處 ～京都・五条坂 河井寬次郎家の人々」（2023.5）
- 日曜美術館: 「だからあんな不思議な絵を 〜夭折の画家・有元利夫と家族〜」（2025.9）
- その他多数

### 5.2 StaffSeeder

初期データとして、伊槻雅裕のプロフィール情報を登録する。

## 6. データ整合性

### 6.1 外部キー制約
現時点では外部キー制約は設定しない（将来的に拡張する可能性あり）

### 6.2 データ検証
- Laravelのバリデーションルールでデータ整合性を確保
- データベースレベルでのNOT NULL制約
- カテゴリ・ステータスはENUMまたはCHECK制約で制限（将来拡張）

## 7. パフォーマンス考慮事項

### 7.1 インデックス
- 検索頻度の高いカラムにインデックスを設定
- `works.category`, `works.broadcast_date`, `works.is_published`
- `contacts.status`, `contacts.created_at`

### 7.2 クエリ最適化
- Eager Loadingの活用
- N+1問題の回避
- ページネーションの実装

### 7.3 キャッシュ戦略
- 作品一覧のキャッシュ
- スタッフ情報のキャッシュ
- キャッシュの無効化タイミングの設計

## 8. バックアップ・復旧

### 8.1 バックアップ方針
- 日次バックアップ（本番環境）
- バックアップファイルの外部保存

### 8.2 復旧手順
- バックアップからのリストア手順書の作成


