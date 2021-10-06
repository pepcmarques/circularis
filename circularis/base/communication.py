from django.conf import settings


# Subjects

SBJ_REQUEST = f"[{settings.SYSTEM_NAME}] Book Request"
SBJ_REJECT = f"[{settings.SYSTEM_NAME}] Your book request was rejected"
SBJ_ACCEPT = f"[{settings.SYSTEM_NAME}] Your book request was accepted"


# Messages

MSG_REQUEST = "Hi! Could I take this book?\n\n%s\n\nThanks for that,\n%s\n\n* Automatically generated by the system"
MSG_REJECT = "Hi! So sorry for that, but I had to reject your request for\n\n%s\n\nThanks for understanding,\n%s" \
             "\n\n* Automatically generated by the system"
MSG_ACCEPT = "Hi! Send me an email to schedule the book pick up\n\n%s\n\nHave a good reading,\n%s" \
             "\n\n* Automatically generated by the system"