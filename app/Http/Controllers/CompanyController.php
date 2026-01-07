<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class CompanyController extends Controller
{
    /**
     * 会社情報ページを表示
     */
    public function index()
    {
        return view('pages.company');
    }
}
