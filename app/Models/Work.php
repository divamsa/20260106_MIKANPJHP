<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Casts\Attribute;

class Work extends Model
{
    protected $fillable = [
        'title',
        'broadcast_date',
        'category',
        'description',
        'link_url',
        'image_path',
        'display_order',
        'is_published',
    ];

    protected $casts = [
        'broadcast_date' => 'date',
        'is_published' => 'boolean',
        'display_order' => 'integer',
    ];

    /**
     * カテゴリのラベルを取得
     */
    public function getCategoryLabelAttribute(): string
    {
        return match($this->category) {
            'etv_special' => 'ETV特集',
            '4k_special' => '4K特集',
            'nichiyo_bijutsu' => '日曜美術館',
            'other' => 'その他',
            default => $this->category,
        };
    }
}
