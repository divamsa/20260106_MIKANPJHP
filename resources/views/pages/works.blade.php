@extends('layouts.app')

@section('title', 'Works - みかんプロジェクト')
@section('description', 'みかんプロジェクトの制作実績をご紹介します。NHK番組などの映像作品を制作しています。')

@section('content')
<section class="works" aria-labelledby="works-heading">
    <div class="works__container">
        <header class="works__header">
            <h1 id="works-heading" class="works__heading">
                <span class="works__heading-text">Works</span>
            </h1>
            <p class="works__subheading">制作実績</p>
        </header>

        <div class="works__filters">
            <form method="GET" action="{{ route('works') }}" class="works__filter-form">
                <div class="works__filter-group">
                    <label for="category" class="works__filter-label">カテゴリで絞り込む</label>
                    <select name="category" id="category" class="works__filter-select" aria-label="カテゴリでフィルタリング">
                        <option value="">すべてのカテゴリ</option>
                        <option value="etv_special" {{ $selectedCategory === 'etv_special' ? 'selected' : '' }}>ETV特集</option>
                        <option value="4k_special" {{ $selectedCategory === '4k_special' ? 'selected' : '' }}>4K特集</option>
                        <option value="nichiyo_bijutsu" {{ $selectedCategory === 'nichiyo_bijutsu' ? 'selected' : '' }}>日曜美術館</option>
                        <option value="other" {{ $selectedCategory === 'other' ? 'selected' : '' }}>その他</option>
                    </select>
                </div>
                <button type="submit" class="works__filter-button" aria-label="フィルタを適用">
                    <span class="works__filter-button-text">フィルタ</span>
                </button>
            </form>
        </div>

        <div class="works__list">
            @forelse($worksByCategory as $category => $categoryWorks)
                <section class="works__category" aria-labelledby="category-{{ $category }}">
                    <h2 id="category-{{ $category }}" class="works__category-heading">
                        @if($category === 'etv_special')
                            ETV特集
                        @elseif($category === '4k_special')
                            4K特集
                        @elseif($category === 'nichiyo_bijutsu')
                            日曜美術館
                        @else
                            その他
                        @endif
                    </h2>
                    <ul class="works__items">
                        @foreach($categoryWorks as $work)
                            <li class="works__item">
                                <article class="work-card">
                                    @if($work->image_path)
                                        <div class="work-card__image-wrapper">
                                            <img src="{{ asset($work->image_path) }}" 
                                                 alt="{{ $work->title }}" 
                                                 class="work-card__image"
                                                 loading="lazy">
                                            <div class="work-card__overlay"></div>
                                        </div>
                                    @endif
                                    <div class="work-card__content">
                                        <div class="work-card__header">
                                        @if($work->broadcast_date)
                                            <time datetime="{{ $work->broadcast_date->format('Y-m-d') }}" class="work-card__date">
                                                {{ $work->broadcast_date->format('Y年n月') }}
                                            </time>
                                        @endif
                                            <span class="work-card__category-badge">{{ $work->category_label }}</span>
                                        </div>
                                        <h3 class="work-card__title">{{ $work->title }}</h3>
                                        @if($work->description)
                                            <p class="work-card__description">{{ $work->description }}</p>
                                        @endif
                                        @if($work->link_url)
                                            <div class="work-card__footer">
                                                <a href="{{ $work->link_url }}" 
                                                   target="_blank" 
                                                   rel="noopener noreferrer"
                                                   class="work-card__link"
                                                   aria-label="{{ $work->title }}の詳細を見る（新しいウィンドウで開きます）">
                                                    <span class="work-card__link-text">関連リンク</span>
                                                    <span class="work-card__link-icon" aria-hidden="true">→</span>
                                                </a>
                                            </div>
                                        @endif
                                    </div>
                                </article>
                            </li>
                        @endforeach
                    </ul>
                </section>
            @empty
                <p class="works__empty">作品が見つかりませんでした。</p>
            @endforelse
        </div>
    </div>
</section>
@endsection

