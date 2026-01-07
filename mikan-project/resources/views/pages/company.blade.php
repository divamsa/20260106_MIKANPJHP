@extends('layouts.app')

@section('title', 'Company - みかんプロジェクト')
@section('description', '株式会社みかんプロジェクトの会社情報とお問い合わせフォームです。')

@section('content')
<section class="company" aria-labelledby="company-heading">
    <div class="company__container">
        <header class="company__header">
            <h1 id="company-heading" class="company__heading">
                <span class="company__heading-text">Company</span>
            </h1>
            <p class="company__subheading">会社情報</p>
        </header>

        <div class="company__content">
            <section class="company-info" aria-labelledby="company-info-heading">
                <h2 id="company-info-heading" class="company-info__heading">会社概要</h2>
                <dl class="company-info__list">
                    <div class="company-info__item">
                        <dt class="company-info__term">商号</dt>
                        <dd class="company-info__description">株式会社みかんプロジェクト</dd>
                    </div>
                    <div class="company-info__item">
                        <dt class="company-info__term">設立</dt>
                        <dd class="company-info__description">2020年10月</dd>
                    </div>
                    <div class="company-info__item">
                        <dt class="company-info__term">資本金</dt>
                        <dd class="company-info__description">500万円</dd>
                    </div>
                    <div class="company-info__item">
                        <dt class="company-info__term">業務内容</dt>
                        <dd class="company-info__description">テレビ番組等の映像作品企画・制作</dd>
                    </div>
                    <div class="company-info__item">
                        <dt class="company-info__term">代表取締役</dt>
                        <dd class="company-info__description">伊槻雅裕</dd>
                    </div>
                </dl>
            </section>

            <section class="contact" aria-labelledby="contact-heading">
                <h2 id="contact-heading" class="contact__heading">Contact</h2>
                <p class="contact__description">番組のご感想、お問い合わせなど</p>

                @if(session('success'))
                    <div class="contact__message contact__message--success" role="alert">
                        {{ session('success') }}
                    </div>
                @endif

                @if($errors->has('general'))
                    <div class="contact__message contact__message--error" role="alert">
                        {{ $errors->first('general') }}
                    </div>
                @endif

                @include('components.contact-form')
            </section>
        </div>
    </div>
</section>
@endsection

