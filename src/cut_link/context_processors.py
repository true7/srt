def custom_proc(request):
    return {
        'test': '&copy;&nbspProduction by Oleg Diatlenko.',
        # 'test_ip': request.META['REMOTE_ADDR']
    }
