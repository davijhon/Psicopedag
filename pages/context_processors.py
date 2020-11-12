from decouple import config

def get_tracking_code_google_analytics(request):
    GOOGLE_ANALYTICS_ID = config('GOOGLE_ANALYTICS_ID')
    return {
        'GOOGLE_ANALYTICS_ID': GOOGLE_ANALYTICS_ID,
    }