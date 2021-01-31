label before_main_menu:
    $ ASBootloader.boot()
    return

label main_menu:
    $ ASDesktop._callDesktop()
    return

label start:
    $ ASDesktop._callDesktop()
    return
