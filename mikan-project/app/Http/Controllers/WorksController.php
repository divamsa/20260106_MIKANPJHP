<?php

namespace App\Http\Controllers;

use App\Models\Work;
use Illuminate\Http\Request;

class WorksController extends Controller
{
    /**
     * 作品一覧を表示
     */
    public function index(Request $request)
    {
        $query = Work::query()
            ->orderBy('broadcast_date', 'desc')
            ->orderBy('created_at', 'desc');

        // カテゴリでフィルタリング
        if ($request->has('category') && $request->category) {
            $query->where('category', $request->category);
        }

        $works = $query->get();

        // カテゴリラベルのマッピング
        $categoryLabels = [
            'etv_special' => 'ETV特集',
            '4k_special' => '4K特集',
            'nichiyo_bijutsu' => '日曜美術館',
            'other' => 'その他',
        ];

        // 各作品にカテゴリラベルを追加
        $works->each(function ($work) use ($categoryLabels) {
            $work->category_label = $categoryLabels[$work->category] ?? $work->category;
        });

        // カテゴリ別にグループ化
        $worksByCategory = $works->groupBy('category');

        return view('pages.works', [
            'works' => $works,
            'worksByCategory' => $worksByCategory,
            'selectedCategory' => $request->category ?? '',
        ]);
    }
}
