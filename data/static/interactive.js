function setup() {
    setup_menu_buttons();
}

function setup_menu_buttons() {
    let buttons = document.querySelectorAll(".menu-button");
    let open_menu = null;
    for (const button of buttons) {
        let menu_id = button.getAttribute("menu-name");
        if (menu_id === null)
            continue;

        button.onclick = (evt) => {
            evt.stopPropagation();
            let menu = document.getElementById(menu_id);
            if (menu.classList.contains('hidden')) {
                menu.classList.remove("hidden");
                open_menu = menu_id;
            } else {
                menu.classList.add("hidden");
                open_menu = null;
            }
        };
    }

    window.onclick = (evt) => {
        if (open_menu === null)
            return;

        let menu = document.getElementById(open_menu);
        menu.classList.add("hidden");
    };
}

window.onload = setup;