<nav class="navigation" role="navigation" aria-label="メインナビゲーション">
    <ul class="navigation__list">
        <li class="navigation__item">
            <a href="{{ route('works') }}" 
               class="navigation__link {{ request()->routeIs('works') ? 'navigation__link--active' : '' }}"
               aria-current="{{ request()->routeIs('works') ? 'page' : 'false' }}">
                Works
            </a>
        </li>
        <li class="navigation__item">
            <a href="{{ route('staff') }}" 
               class="navigation__link {{ request()->routeIs('staff') ? 'navigation__link--active' : '' }}"
               aria-current="{{ request()->routeIs('staff') ? 'page' : 'false' }}">
                Staff
            </a>
        </li>
        <li class="navigation__item">
            <a href="{{ route('company') }}" 
               class="navigation__link {{ request()->routeIs('company') ? 'navigation__link--active' : '' }}"
               aria-current="{{ request()->routeIs('company') ? 'page' : 'false' }}">
                Company
            </a>
        </li>
    </ul>
</nav>


