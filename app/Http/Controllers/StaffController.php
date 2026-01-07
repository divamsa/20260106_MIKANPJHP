<?php

namespace App\Http\Controllers;

use App\Models\Staff;
use Illuminate\Http\Request;

class StaffController extends Controller
{
    /**
     * スタッフ情報を表示
     */
    public function index()
    {
        $staffList = Staff::orderBy('created_at', 'asc')->get();

        return view('pages.staff', [
            'staffList' => $staffList,
        ]);
    }
}
