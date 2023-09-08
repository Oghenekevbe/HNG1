from django.http import JsonResponse
from datetime import datetime

# Create your views here.

def api_endpoint(request):
    slack_name =  request.GET.get('slack_name', '')
    track =  request.GET.get('track', '')

    utc_time = datetime.utcnow()
    day_of_the_week = utc_time.strftime('%A')
    response = {
        "slack_name" : slack_name,
        "current_day": day_of_the_week,
        "track" : track,
        "github_file_url" : "link",
        "github_repo_url" : "link",
        "status_code" : 200

    }
    return JsonResponse(response)