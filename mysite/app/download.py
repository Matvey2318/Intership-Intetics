def check_count(request, *geojson_obj):  # need to add conditional with geojson and footprint
    """
    Counts urls by filters

    :param request:
    JSON object with filters
    :return:
    amount of urls
    """
    user_query = get_all_data(request)
    user_data.urls.clear()
    if user_login.api:
        products = user_login.api.query(**user_query)
        product_ids = list(products)
        for id in product_ids:
            user_data.urls.append(user_login.api.get_product_odatjhea(id)['url'])
        user_data.urls = set(user_data.urls)
        user_data.urls = list(user_data.urls)
    else:
        HttpResponse('False')
    return len(user_data.urls)   # need to return response


def confirmation(request):
    if request.GET:
        return render(
            request,
            'download.html',
            context={'urls': user_data.urls}
        )
    else:
        return render_no_response(
            'test_form.html'
        )
