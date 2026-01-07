# Render デプロイ手順

## 1. Renderアカウント作成
1. https://render.com にアクセス
2. 「Get Started for Free」をクリック
3. GitHubアカウントでログイン

## 2. データベース作成
1. Renderダッシュボードで「New +」→「PostgreSQL」を選択
   - **注意**: Renderの無料プランではMySQLがないため、PostgreSQLを使用します
   - または、外部の無料MySQLサービス（PlanetScale、Aivenなど）を使用

## 3. Webサービス作成
1. Renderダッシュボードで「New +」→「Web Service」を選択
2. GitHubリポジトリ `divamsa/20260106_MIKANPJHP` を選択
3. 以下の設定を入力：
   - **Name**: `mikan-project`
   - **Region**: `Singapore` (日本に近い)
   - **Branch**: `main`
   - **Root Directory**: `mikan-project`
   - **Runtime**: `Docker` ⚠️ **重要：必ずDockerを選択**
   - **Dockerfile Path**: `Dockerfile.render`
   - **Docker Context**: `.`
   - **Build Command**: `echo "Building with Docker..."` （必須フィールドなのでダミーコマンドを入力）
   - **Start Command**: ⚠️ **空欄のまま（何も入力しない）**

## 4. 環境変数設定
Webサービスの「Environment」タブで以下を追加：

```
APP_NAME=MikanProject
APP_ENV=production
APP_KEY=（自動生成される）
APP_DEBUG=false
APP_URL=https://your-app-name.onrender.com

DB_CONNECTION=postgresql
DB_HOST=（データベースのInternal Database URLから取得）
DB_PORT=5432
DB_DATABASE=（データベース名）
DB_USERNAME=（データベースユーザー名）
DB_PASSWORD=（データベースパスワード）

LOG_CHANNEL=stderr
LOG_LEVEL=error
```

## 5. ビルドコマンド（自動）
Renderが自動的にDockerイメージをビルドします。

## 6. デプロイ
1. 「Save Changes」をクリック
2. 自動的にデプロイが開始されます（5-10分かかります）
3. デプロイ完了後、URLが発行されます（例: `https://mikan-project.onrender.com`）

## 7. データベースマイグレーション
デプロイ後、Webサービスの「Shell」タブで以下を実行：

```bash
php artisan migrate --force
php artisan db:seed --force
```

## 8. 完了！
URLを共有すれば、誰でもアクセスできます。

---

## トラブルシューティング

### デプロイが失敗する場合
- ログを確認（「Logs」タブ）
- 環境変数が正しく設定されているか確認
- データベース接続情報を確認

### データベース接続エラー
- PostgreSQLのInternal Database URLを使用
- 環境変数の`DB_HOST`、`DB_PORT`、`DB_DATABASE`、`DB_USERNAME`、`DB_PASSWORD`を確認

