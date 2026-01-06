<?php

use App\Http\Controllers\HomeController;
use App\Http\Controllers\WorksController;
use App\Http\Controllers\StaffController;
use App\Http\Controllers\CompanyController;
use App\Http\Controllers\ContactController;
use Illuminate\Support\Facades\Route;

Route::get('/', [HomeController::class, 'index'])->name('home');
Route::get('/works', [WorksController::class, 'index'])->name('works');
Route::get('/staff', [StaffController::class, 'index'])->name('staff');
Route::get('/company', [CompanyController::class, 'index'])->name('company');
Route::post('/contact', [ContactController::class, 'store'])->name('contact.store');
