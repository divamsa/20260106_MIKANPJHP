@extends('layouts.app')

@section('title', 'Staff - みかんプロジェクト')
@section('description', 'みかんプロジェクトのスタッフをご紹介します。')

@section('content')
<section class="staff" aria-labelledby="staff-heading">
    <div class="staff__container">
        <header class="staff__header">
            <h1 id="staff-heading" class="staff__heading">
                <span class="staff__heading-text">Staff</span>
            </h1>
            <p class="staff__subheading">スタッフ紹介</p>
        </header>

        @if($staffList && $staffList->count() > 0)
            <ul class="staff__list">
                @foreach($staffList as $staff)
                    <li class="staff__item">
                        <article class="staff-card">
                            @if($staff->image_path)
                                <div class="staff-card__image-wrapper">
                                    <img src="{{ asset($staff->image_path) }}" 
                                         alt="{{ $staff->name }}" 
                                         class="staff-card__image"
                                         loading="lazy">
                                    <div class="staff-card__overlay"></div>
                                </div>
                            @endif
                            <div class="staff-card__content">
                                <div class="staff-card__header">
                                    <h2 class="staff-card__name">{{ $staff->name }}</h2>
                                    @if($staff->role)
                                        <span class="staff-card__role-badge">{{ $staff->role }}</span>
                                    @endif
                                </div>
                                
                                @if($staff->profile)
                                    <div class="staff-card__section">
                                        <h3 class="staff-card__section-heading">プロフィール</h3>
                                        <div class="staff-card__text">
                                            {!! nl2br(e($staff->profile)) !!}
                                        </div>
                                    </div>
                                @endif

                                @if($staff->achievements)
                                    <div class="staff-card__section">
                                        <h3 class="staff-card__section-heading">これまでの主な仕事</h3>
                                        <div class="staff-card__text">
                                            @if(is_array($staff->achievements) || is_string($staff->achievements))
                                                @if(is_string($staff->achievements))
                                                    {!! nl2br(e($staff->achievements)) !!}
                                                @else
                                                    <ul class="staff-card__achievements-list">
                                                        @foreach($staff->achievements as $achievement)
                                                            <li>{{ $achievement }}</li>
                                                        @endforeach
                                                    </ul>
                                                @endif
                                            @endif
                                        </div>
                                    </div>
                                @endif
                            </div>
                        </article>
                    </li>
                @endforeach
            </ul>
        @else
            <p class="staff__empty">スタッフ情報が見つかりませんでした。</p>
        @endif
    </div>
</section>
@endsection

