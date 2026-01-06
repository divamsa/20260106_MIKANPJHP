<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HomeController extends Controller
{
    /**
     * トップページを表示
     */
    public function index()
    {
        return view('pages.home');
    }
}
