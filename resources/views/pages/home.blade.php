@extends('layouts.app')

@section('title', 'みかんプロジェクト')
@section('description', 'みかんプロジェクトは映像制作会社です。世の中に埋もれた大切な忘れものを届けることが出来たら、そんな思いで番組を作っています。')

@section('content')
<section class="hero" aria-labelledby="hero-heading">
    <div class="hero__container">
        <div class="hero__image-wrapper">
            <img src="{{ asset('images/表紙.png') }}" 
                 alt="みかんプロジェクト - 世の中に埋もれた大切な忘れものを届けることが出来たら、そんな思いで番組を作っています" 
                 class="hero__image"
                 loading="eager">
        </div>
    </div>
</section>
@endsection

