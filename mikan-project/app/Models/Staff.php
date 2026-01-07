<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Staff extends Model
{
    protected $fillable = [
        'name',
        'position',
        'profile',
        'biography',
        'achievements',
        'image_path',
    ];
}
