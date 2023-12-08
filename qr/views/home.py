from django.shortcuts import render

def home(request):
    user_agent_info = request.META.get('HTTP_USER_AGENT', '')
    browser_info = get_browser_info(user_agent_info)
    return render(request, 'home.html', {'browser_info': browser_info})

def get_browser_info(user_agent_info):
    if 'Chrome' in user_agent_info and 'Android' not in user_agent_info:
        return "Estás usando navegador web Windows"
    elif 'Linux' in user_agent_info:
        return "Estás usando navegador movil Android"
    elif 'iPad' in user_agent_info:
        return "Estás usando navegador iPad"
    elif 'iPhone' in user_agent_info:
        return "Estás usando un navegador movil iPhone"
    elif 'Android' in user_agent_info:
        return "Estás usando navegador movil Android"
    elif 'Windows' in user_agent_info:
        return "Estás usando un dispositivo Windows"
    else:
        return f"Información del User-Agent: {user_agent_info}"
