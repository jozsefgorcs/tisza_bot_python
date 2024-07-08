def construct_filter_url(main_url, size_filter):
    if not main_url.endswith('/'):
        main_url += '/'

    return main_url + '?filter%5B0%5D=' + str(size_filter)