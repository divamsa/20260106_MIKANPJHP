<form action="{{ route('contact.store') }}" method="POST" class="contact-form" novalidate>
    @csrf

    <div class="contact-form__field">
        <label for="name" class="contact-form__label">
            お名前
            <span class="contact-form__required" aria-label="必須">*</span>
        </label>
        <input type="text" 
               id="name" 
               name="name" 
               value="{{ old('name') }}"
               class="contact-form__input @error('name') contact-form__input--error @enderror"
               required
               aria-required="true"
               aria-invalid="{{ $errors->has('name') ? 'true' : 'false' }}"
               aria-describedby="@if($errors->has('name')) name-error @endif">
        @error('name')
            <span id="name-error" class="contact-form__error" role="alert">{{ $message }}</span>
        @enderror
    </div>

    <div class="contact-form__field">
        <label for="email" class="contact-form__label">
            メールアドレス
            <span class="contact-form__required" aria-label="必須">*</span>
        </label>
        <input type="email" 
               id="email" 
               name="email" 
               value="{{ old('email') }}"
               class="contact-form__input @error('email') contact-form__input--error @enderror"
               required
               aria-required="true"
               aria-invalid="{{ $errors->has('email') ? 'true' : 'false' }}"
               aria-describedby="@if($errors->has('email')) email-error @endif">
        @error('email')
            <span id="email-error" class="contact-form__error" role="alert">{{ $message }}</span>
        @enderror
    </div>

    <div class="contact-form__field">
        <label for="message" class="contact-form__label">
            お問い合わせ内容
            <span class="contact-form__required" aria-label="必須">*</span>
        </label>
        <textarea id="message" 
                  name="message" 
                  rows="6"
                  class="contact-form__textarea @error('message') contact-form__textarea--error @enderror"
                  required
                  aria-required="true"
                  aria-invalid="{{ $errors->has('message') ? 'true' : 'false' }}"
                  aria-describedby="@if($errors->has('message')) message-error @endif">{{ old('message') }}</textarea>
        @error('message')
            <span id="message-error" class="contact-form__error" role="alert">{{ $message }}</span>
        @enderror
    </div>

    <div class="contact-form__actions">
        <button type="submit" class="contact-form__submit">
            送信
        </button>
    </div>
</form>


