from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("""
                        <title>Typedia</title>
                        Hello! Welcome to the W site! <img src="https://github.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/blob/master/Emojis/Smilies/Grinning%20Face.png?raw=true" width=20, height=20><img>
                        <hr><br>
                        This is made by HIM, <strong>S.D.</strong> for a blog web-app
                        that can be used by people to spread their
                        personal creative messages! 🔥
                        <br><br><br>
                        <u><strong>*Note:</strong></u> This is still in progress! 👨‍🏭
                        """)
    