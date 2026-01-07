<?php

namespace App\Http\Controllers;

use App\Models\Contact;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Validator;

class ContactController extends Controller
{
    /**
     * お問い合わせフォームを送信
     */
    public function store(Request $request)
    {
        $validator = Validator::make($request->all(), [
            'name' => 'required|string|max:100',
            'email' => 'required|email|max:255',
            'message' => 'required|string|max:5000',
        ]);

        if ($validator->fails()) {
            return back()
                ->withErrors($validator)
                ->withInput();
        }

        try {
            Contact::create([
                'name' => $request->name,
                'email' => $request->email,
                'message' => $request->message,
                'status' => 'unread',
                'ip_address' => $request->ip(),
            ]);

            return redirect()->route('company')
                ->with('success', 'お問い合わせを受け付けました。ありがとうございます。');
        } catch (\Exception $e) {
            \Log::error('お問い合わせ送信エラー: ' . $e->getMessage(), [
                'request' => $request->except(['message']), // メッセージ内容はログに含めない
            ]);

            return back()
                ->withInput()
                ->withErrors(['general' => 'サーバーエラーが発生しました。しばらく時間をおいて再度お試しください。']);
        }
    }
}
