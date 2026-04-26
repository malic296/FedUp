document.addEventListener('click', (event) => {
    const $burger = event.target.closest('.navbar-burger');
    if ($burger) {
        const targetId = $burger.dataset.target;
        const $targetMenu = document.getElementById(targetId);

        if ($targetMenu) {
            $burger.classList.toggle('is-active');
            $targetMenu.classList.toggle('is-active');
        }
    }

    const $delete = event.target.closest('.notification .delete');
    if ($delete) {
        const $notification = $delete.closest('.notification');
        $notification.remove();
    }

    const $navbarLink = event.target.closest('.navbar-link');
    if ($navbarLink && $navbarLink.parentElement.classList.contains('has-dropdown')) {
        const $dropdownMenu = $navbarLink.nextElementSibling; // The .navbar-dropdown div

        if (window.innerWidth <= 1023) {
            $dropdownMenu.classList.toggle('is-hidden-touch');

            $navbarLink.classList.toggle('is-active');
        }
    }
});