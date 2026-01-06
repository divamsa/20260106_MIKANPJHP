FROM php:8.4-fpm

# システムパッケージのインストール
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# PHP拡張機能のインストール
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd

# Composerのインストール
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# 作業ディレクトリの設定
WORKDIR /var/www/html

# ユーザーとグループの設定
RUN groupadd -g 1000 www
RUN useradd -u 1000 -ms /bin/bash -g www www

# ファイルの所有権を変更
RUN chown -R www:www /var/www/html

# ユーザーを切り替え
USER www

# デフォルトコマンド
CMD ["php-fpm"]

